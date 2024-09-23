import openai
import os
from dotenv import load_dotenv
# Función que carga ENV
load_dotenv()
# igualación de variable Key OpenAI
openai.api_key = os.getenv('API_KEY')

# Function de ChatCompletions
def question_openai(in_pregunta):
    response = openai.completions.create(
    model="davinci-002",
    prompt=in_pregunta,
    temperature=0.7,
    max_tokens=1000,
    )
    return response.choices[0].text.strip()

pregunta = "dame una estructura de html"
respuesta = question_openai(in_pregunta=pregunta)
print(respuesta)

