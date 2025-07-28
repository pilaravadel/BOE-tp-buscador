# BOE TP Buscador

Aplicación web para consultar ofertas públicas diarias del BOE, con filtros por comunidad, provincia, localidad y exportación a Excel. Incluye resúmenes automáticos con GPT.

## Cómo desplegar

1. Sube esta carpeta a un repositorio privado en GitHub.
2. Entra en https://streamlit.io/cloud
3. Conecta tu cuenta de GitHub y despliega este repositorio.
4. Ve a Settings > Manage Access y añade los correos autorizados.
5. En Settings > Secrets añade:
   ```
   OPENAI_API_KEY = "tu_clave"
   ```
6. Para convertirlo en app móvil: accede desde móvil y pulsa “Añadir a pantalla de inicio”.

¡Listo!
