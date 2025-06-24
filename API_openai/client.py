import openai
from django.conf import settings

openai.api_key = (settings.OPENAI_API_KEY)
def get_filme_sinopse(titulo, ano, diretor, atores):
    prompt = f"Crie um prompt em apenas 200 caracteres para o filme '{titulo}' do ano {ano}, dirigido por {diretor} e estrelado por {atores}."

    response = openai.chat.completions.create(
        model='gpt-4',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
