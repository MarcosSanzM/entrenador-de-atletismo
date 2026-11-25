"""Conversational athletics coach powered by the OpenAI API."""

import os


INSTRUCTIONS = """\
Eres «Entrenador de atletismo», un experto conversacional en entrenamiento de atletismo.
Responde en el idioma de la persona y ofrece orientación clara, práctica y prudente.

No se ha proporcionado documentación de entrenamiento en esta aplicación. Dilo con
claridad cuando sea pertinente y nunca afirmes haber consultado documentos cargados
ni atribuyas recomendaciones a documentación inexistente.

Antes de crear un plan personalizado, asegúrate de conocer el objetivo deportivo,
el nivel y experiencia, los días y tiempo disponibles, el equipamiento disponible
y el historial o lesiones relevantes. Si falta información, pregunta por ella
primero en vez de asumirla. Adapta el plan a los datos que la persona proporcione.

No diagnostiques ni sustituyas la atención profesional. Si la persona menciona una
lesión, dolor, síntomas o una condición médica, recomiéndale consultar a un
profesional cualificado antes de seguir o modificar el entrenamiento. No propongas
que entrene a través del dolor.
"""


class AthleticCoachAgent:
    """Keep conversational context and request replies from an OpenAI client."""

    def __init__(self, client, model):
        self.client = client
        self.model = model
        self.history = []

    def reply(self, message):
        message = message.strip()
        if not message:
            raise ValueError("El mensaje no puede estar vacío.")

        response = self.client.responses.create(
            model=self.model,
            instructions=INSTRUCTIONS,
            input=self.history + [{"role": "user", "content": message}],
        )
        answer = response.output_text
        self.history.extend(
            [
                {"role": "user", "content": message},
                {"role": "assistant", "content": answer},
            ]
        )
        return answer


def main():
    from dotenv import load_dotenv

    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit(
            "Falta OPENAI_API_KEY. Configúrala en el archivo .env; "
            "consulta las instrucciones de README.md."
        )

    from openai import OpenAI

    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
    agent = AthleticCoachAgent(OpenAI(), model)

    print("Entrenador de atletismo. Escribe 'salir' o 'exit' para terminar.")
    while True:
        try:
            message = input("\nTú: ").strip()
        except EOFError:
            print()
            break
        if message.lower() in {"salir", "exit"}:
            break
        if not message:
            continue

        answer = agent.reply(message)
        print("\nEntrenador: " + answer)


if __name__ == "__main__":
    main()
