import os
from openai import OpenAI as AsyncOpenAI
import chainlit as cl


api_key= os.environ.get("NVIDIA_API_KEY")
client = AsyncOpenAI(base_url="https://integrate.api.nvidia.com/v1", api_key=api_key)
cl.instrument_openai()
settings={
    "model":"meta/llama-3.1-405b-instruct",
    "temperature":0.5,
    "top_p":0.7,
    "max_tokens":1024,
 }
@cl.on_chat_start
def start_chart():
    cl.user_session.set(
"message_history",
[{"role":"system","content":"You are a helpful assistent."}]   
)
async def async_generator(sync_gen):
    for item in sync_gen:
        yield item
@cl.on_message
async def run_conversation(message:cl.Message):
    
    message_history = cl.user_session.get("message_history")
    message_history.append({"role":"user","content": message.content})
    
    msg = cl.Message(content="")
    await msg.send()
   
    stream = client.chat.completions.create(
             messages= message_history,stream=True, **settings
     )
    async for part in async_generator(stream):
        if token := part.choices[0].delta.content or "":
            await msg.stream_token(token)
    message_history.append({"role":"assistant","content":msg.content})
    await msg.update()  
           
