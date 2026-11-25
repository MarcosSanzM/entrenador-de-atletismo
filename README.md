# Entrenador de atletismo

Agente conversacional de atletismo en Python, ejecutable desde Visual Studio Code o una terminal. Usa la API de OpenAI y no tiene herramientas externas.

## Requisitos

- Python 3.10 o posterior
- Una clave de API de OpenAI

## Preparar el proyecto

1. Abre esta carpeta en Visual Studio Code.
2. Crea y activa un entorno virtual:

   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Instala las dependencias:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Copia `.env.example` a `.env` y añade tu clave de API en `OPENAI_API_KEY`. El archivo `.env` está excluido de Git; no compartas ni publiques la clave.
5. (Opcional) Cambia `OPENAI_MODEL` en `.env`; por defecto se usa `gpt-4o-mini`.

## Conversar

Con el entorno virtual activado, ejecuta:

```powershell
python app.py
```

Escribe una consulta y pulsa Intro. Usa `salir` o `exit` para terminar. También puedes abrir `app.py` en VS Code y ejecutarlo con la extensión de Python, asegurándote de seleccionar el intérprete de `.venv`.

## Pruebas

Las pruebas usan un cliente simulado, no hacen llamadas a la API y no necesitan una clave:

```powershell
python -m unittest discover -s tests -v
```

## Alcance y seguridad

No se ha proporcionado documentación de entrenamiento al agente. Por ello, debe ser transparente sobre esa limitación y no afirmar que sus recomendaciones se basan en documentos cargados. Para diseñar un plan personalizado, debe recabar objetivo, experiencia/nivel, disponibilidad, equipamiento e historial o lesiones relevantes. No diagnostica ni sustituye la atención profesional; ante dolor, lesión, síntomas o condiciones médicas, recomienda consultar a un profesional cualificado.
