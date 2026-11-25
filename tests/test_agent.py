import unittest

from agent_definition import AGENT


class AgentDefinitionTests(unittest.TestCase):
    def test_definition_has_fields_for_axet_configuration(self):
        self.assertEqual(
            set(AGENT),
            {"name", "description", "system_instructions"},
        )
        self.assertEqual(AGENT["name"], "Entrenador de atletismo")
        self.assertIn("atletismo", AGENT["description"])
        self.assertTrue(AGENT["system_instructions"].strip())

    def test_instructions_cover_documentation_personalization_and_safety(self):
        instructions = AGENT["system_instructions"]

        for expected in (
            "No se ha proporcionado documentación",
            "objetivo deportivo",
            "nivel y la experiencia",
            "días y el tiempo disponibles",
            "equipamiento",
            "historial o lesiones",
            "profesional cualificado",
            "recomiendes entrenar a través del dolor",
        ):
            with self.subTest(expected=expected):
                self.assertIn(expected, instructions)


if __name__ == "__main__":
    unittest.main()
