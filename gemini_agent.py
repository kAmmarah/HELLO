# gemini_agent.py
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()  # This loads the .env file from the current directory

# Now you can access variables 
gemini_api_key = os.getenv("GEMINI_API_KEY")
print(gemini_api_key)


def ask_gemini(prompt: str) -> str:
    prompt = {
        "prompt": prompt
    }
    print(prompt)
    """
    Sends a prompt to the Gemini generative AI model and returns the generated response as text.

    Args:
        prompt (str): The input prompt to send to the Gemini model.

    Returns:
        str: The generated text response from the Gemini model.
    """
    api_key = os.getenv("GEMINI_API_KEY", "YOUR_REAL_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text