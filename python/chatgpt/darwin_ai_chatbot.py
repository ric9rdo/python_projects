import openai
import gradio as gr

openai.api_key = "<YOUR API HERE>"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

# Supported language codes
LANGUAGES = {
    "English": "en",
    "Portuguese": "pt",
    "Spanish": "es"
}

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with Darwin AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Darwin AI Chatbot",
             description="",
             theme="default").launch(share=True)
