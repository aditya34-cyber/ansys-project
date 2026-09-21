from google import genai
:q
:qa

from agent.prompts import SYSTEM_PROMPT
from agent.tools import TOOLS


class GeminiAgent:

    def __init__(self, api_key: str):

        self.client = genai.Client(
            api_key=api_key
        )

        self.tools = TOOLS

        self.system_prompt = SYSTEM_PROMPT


    def get_response(self, user_prompt: str):

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_prompt,
            config={
                "system_instruction": self.system_prompt,
                "tools": self.tools,
            },
        )

        return response
