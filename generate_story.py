import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_KEY"]

def generate_story(tags,caption):
    print(tags,caption)
    prompt= f'''I'll give you an array of tags and a short caption. Provide me with a descriptive story connecting those tags and the caption {str(tags)} ,caption: {caption}'''
    print(prompt)
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0, max_tokens=1000)
    print(response)