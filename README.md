Chatbot with Chainlit and NVIDIA API
This project demonstrates how to build an asynchronous chatbot using OpenAI's API and Chainlit. The chatbot is designed to provide helpful responses to user queries by leveraging the meta/llama-3.1-405b-instruct model. The project includes setting up the environment, initializing the OpenAI client, and handling user messages asynchronously.

Features
Asynchronous Communication: Utilizes asynchronous programming to handle user messages and OpenAI responses efficiently.
OpenAI Integration: Connects to OpenAI's API to generate responses based on the meta/llama-3.1-405b-instruct model.
Chainlit Integration: Uses Chainlit to manage user sessions and message history.
Customizable Settings: Allows customization of model parameters such as temperature, top_p, and max_tokens.
Requirements
Python 3.7+
openai library
chainlit library
An NVIDIA API key
Installation
Clone the repository:

Sh
Insert in terminal

git clone https://github.com/yourusername/async-openai-chatbot.git
cd async-openai-chatbot
Install the required libraries:

Sh
Insert in terminal

pip install openai chainlit
Set up your NVIDIA API key:

Sh
Insert in terminal

export NVIDIA_API_KEY=your_api_key_here
Usage
Run the chatbot:

Sh
Insert in terminal

python chatbot.py
Interact with the chatbot through the Chainlit interface.

Code Overview
Initialization: The OpenAI client is initialized with the base URL and API key.
Settings: Model parameters such as model, temperature, top_p, and max_tokens are defined.
Session Management: Chainlit is used to manage user sessions and maintain message history.
Message Handling: User messages are processed asynchronously, and responses are generated using the OpenAI API.
Example
Python
Run code
Insert code

import os
from openai import OpenAI as AsyncOpenAI
import chainlit as cl

api_key = os.environ.get("NVIDIA_API_KEY")
client = AsyncOpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=api_key)
cl.instrument_openai()

settings = {
    "model": "meta/llama-3.1-405b-instruct",
    "temperature": 0.5,
    "top_p": 0.7,
    "max_tokens": 1024,
}

@cl.on_chat_start
def start_chart():
    cl.user_session.set(
        "message_history",
        [{"role": "system", "content": "You are a helpful assistant."}]
    )

async def async_generator(sync_gen):
    for item in sync_gen:
        yield item

@cl.on_message
async def run_conversation(message: cl.Message):
    message_history = cl.user_session.get("message_history")
    message_history.append({"role": "user", "content": message.content})

    msg = cl.Message(content="")
    await msg.send()

    stream = client.chat.completions.create(
        messages=message_history, stream=True, **settings
    )
    async for part in async_generator(stream):
        if token := part.choices[0].delta.content or "":
            await msg.stream_token(token)
    message_history.append({"role": "assistant", "content": msg.content})
    await msg.update()




Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize this README file to better suit your project's needs.

1 of 8

Reload
Upgrade to a plan to unlock more features and increase your daily interactions.

Upgrade



GPT-4o


GPT-4o-mini


Claude 3.5 Sonnet V2


Gemini 2.0 Flash


Llama 3.1 - 70B


GPT-3.5-Turbo


Llama 3.1 - 405B


Mistral Large 2


Llama 3.1 - 70B by Groq


Llama 3.2 - 90B by Groq


Claude 3.5 Haiku


Codestral


Gemini 1.5 Pro


COMMAND R +


Gemini 2.0 Flash Thinking

main
