from google import genai
from config import Config

config = Config()

class LLM_service:
    def __init__(self):
        self.client = genai.Client(api_key=config.LLM_KEY)

    async def ask_question(self, instructions: str, context: list[str], question: str):
        try:
            messages = [
                {"role": "user", "parts": [{"text": instructions}]},
                {"role": "user", "parts": [{"text": f"Pergunta: {question}"}]}
            ]

            for ctx in context:
                messages[-1]["parts"].append({"text": ctx})

            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=messages,
            )
            return response.text
        except Exception as e:
            raise LLMServiceError(f"Erro na API do Gemini: {str(e)}")

    async def generate_embedding(self, question):
        return [1, 1, 1, 1]


class LLMServiceError(Exception):
    pass
