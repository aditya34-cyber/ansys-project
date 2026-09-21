from dotenv import load_dotenv
import os

from agent.gemini import GeminiAgent


load_dotenv()

api_key = os.getenv("MY_GEMINI_KEY")

if not api_key:
    raise ValueError("MY_GEMINI_KEY is not set.")


agent = GeminiAgent(api_key)


while True:

    user_prompt = input("\nYou: ")

    if user_prompt.lower() in {"exit", "quit"}:
        break

    response = agent.get_response(user_prompt)

    print("\nGemini:")
    print(response.text)
    
