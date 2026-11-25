import unittest

from app import AthleticCoachAgent, INSTRUCTIONS


class FakeResponse:
    output_text = "Para preparar un plan, cuéntame tu objetivo y disponibilidad."


class FakeResponses:
    def __init__(self):
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return FakeResponse()


class FakeClient:
    def __init__(self):
        self.responses = FakeResponses()


class AthleticCoachAgentTests(unittest.TestCase):
    def setUp(self):
        self.client = FakeClient()
        self.agent = AthleticCoachAgent(self.client, "test-model")

    def test_sends_instructions_and_returns_response(self):
        answer = self.agent.reply("  Quiero empezar a correr  ")

        self.assertEqual(
            answer,
            "Para preparar un plan, cuéntame tu objetivo y disponibilidad.",
        )
        request = self.client.responses.calls[0]
        self.assertEqual(request["model"], "test-model")
        self.assertIn("lesión", request["instructions"])
        self.assertEqual(
            request["input"],
            [{"role": "user", "content": "Quiero empezar a correr"}],
        )

    def test_preserves_context_between_messages(self):
        self.agent.reply("Quiero preparar una carrera.")
        self.agent.reply("Puedo entrenar tres días.")

        second_input = self.client.responses.calls[1]["input"]
        self.assertEqual(
            [item["role"] for item in second_input],
            ["user", "assistant", "user"],
        )
        self.assertEqual(second_input[-1]["content"], "Puedo entrenar tres días.")

    def test_rejects_empty_message_without_api_call(self):
        with self.assertRaises(ValueError):
            self.agent.reply("  ")

        self.assertEqual(self.client.responses.calls, [])

    def test_instructions_cover_documentation_and_safety_limits(self):
        self.assertIn("No se ha proporcionado documentación", INSTRUCTIONS)
        self.assertIn("profesional cualificado", INSTRUCTIONS)
        self.assertIn("equipamiento", INSTRUCTIONS)


if __name__ == "__main__":
    unittest.main()
