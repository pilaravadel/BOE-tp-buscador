import streamlit as st
import pandas as pd
from datetime import date
import openai

st.set_page_config(page_title="BOE TP Buscador", layout="wide")

st.title("📜 BOE TP Buscador")
st.markdown("Filtra ofertas de empleo público del BOE y descarga resultados en Excel.")

# Parámetros ficticios de ejemplo
data = pd.DataFrame({
    "Fecha": ["2025-07-01", "2025-07-01", "2025-07-01"],
    "Título": ["Convocatoria A", "Convocatoria B", "Convocatoria C"],
    "Organismo": ["Ministerio de Justicia", "Junta de Andalucía", "Diputación de Valencia"],
    "Comunidad Autónoma": ["Madrid", "Andalucía", "Comunidad Valenciana"],
    "Provincia": ["Madrid", "Sevilla", "Valencia"],
    "Localidad": ["Madrid", "Sevilla", "Valencia"],
    "Enlace": ["http://boe.es/a", "http://boe.es/b", "http://boe.es/c"],
    "Resumen GPT": ["", "", ""]
})

# Filtros
with st.sidebar:
    st.header("🔍 Filtros")
    comunidad = st.selectbox("Comunidad Autónoma", ["Todas"] + sorted(data["Comunidad Autónoma"].unique().tolist()))
    provincia = st.selectbox("Provincia", ["Todas"] + sorted(data["Provincia"].unique().tolist()))
    localidad = st.selectbox("Localidad", ["Todas"] + sorted(data["Localidad"].unique().tolist()))

# Aplicar filtros
df = data.copy()
if comunidad != "Todas":
    df = df[df["Comunidad Autónoma"] == comunidad]
if provincia != "Todas":
    df = df[df["Provincia"] == provincia]
if localidad != "Todas":
    df = df[df["Localidad"] == localidad]

# Mostrar resultados
st.write(f"Resultados encontrados: {len(df)}")
st.dataframe(df)

# Exportar a Excel
st.download_button("📥 Descargar Excel", df.to_csv(index=False).encode('utf-8'), file_name="boe_tp_resultados.csv", mime="text/csv")

# GPT resumen
if "OPENAI_API_KEY" in st.secrets:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    for i in df.index:
        if not df.at[i, "Resumen GPT"]:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Resume esta convocatoria del BOE en lenguaje claro."},
                    {"role": "user", "content": df.at[i, "Título"]}
                ]
            )
            df.at[i, "Resumen GPT"] = response["choices"][0]["message"]["content"]
else:
    st.warning("🔑 Añade tu clave OpenAI en la configuración de secretos para activar los resúmenes GPT.")
