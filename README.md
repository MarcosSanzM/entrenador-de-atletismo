# Entrenador de atletismo

Definición portable de un agente de entrenamiento de atletismo para configurar
manualmente en Axet Flows. Axet selecciona y ejecuta el modelo; este repositorio
no incluye un cliente de inferencia, integración nativa ni herramientas externas.

## Configurarlo en Axet Flows

1. Crea o configura un agente en Axet Flows.
2. Copia el nombre, la descripción y las instrucciones del campo `AGENT` de
   [`agent_definition.py`](agent_definition.py) en los campos equivalentes de
   Axet: `name`, `description` y `system_instructions`.
3. Selecciona el modelo en Axet Flows.
4. Añade allí la documentación de entrenamiento que quieras asignar al agente.
   No se ha proporcionado documentación todavía.

El formato de importación nativo de Axet no está especificado aquí, por lo que
este proyecto no afirma ofrecer un archivo importable directamente. No necesitas
una clave de API de OpenAI ni instalar dependencias. Para usarlo en Axet, no
ejecutes `python app.py`: no hay una aplicación local ni una conexión a modelo.

## Pruebas locales de la definición

Las pruebas usan solo la biblioteca estándar de Python y no hacen llamadas de
red ni requieren credenciales:

```powershell
python -m unittest discover -s tests -v
```

