# coding: utf-8
#Librerias
import openai

# Establecer la API key de OpenAI
# https://beta.openai.com/account/api-keys
openai.api_key = "YOUR_API_KEY"

# Definir el modelo de lenguaje que se va a utilizar
model_engine = "text-davinci-002"

# Generar una respuesta a una pregunta dada
prompt = (input('\nNew Chat: '))
completions = openai.Completion.create(engine=model_engine,
                                      prompt=prompt,
                                      max_tokens=1024,
                                      n=1,
                                      stop=None,
                                      temperature=0.5)

# Imprimir la respuesta generada
print(completions.choices[0].text)
