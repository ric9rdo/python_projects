import openai
import os

openai.api_key = "<YOUR API HERE>"

def chat(prompt, model, temperature):
    response = openai.Completion.create(
      engine=model,
      prompt=prompt,
      temperature=temperature,
      max_tokens=1024,
      n=1,
      stop=None,
      frequency_penalty=0,
      presence_penalty=0
    )

    message = response.choices[0].text.strip()
    return message

while True:
    prompt = input("You: ")
    response = chat(prompt, "davinci", 0.5)
    print("ChatGPT: " + response)
