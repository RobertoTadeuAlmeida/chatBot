import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_openai_response(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Erro ao conectar com a API OpenAI: {str(e)}"
    
print(get_openai_response("Quem e voce?"))

