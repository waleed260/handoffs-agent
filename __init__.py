from re import M
from agents import Agent ,Runner ,AsyncOpenAI,OpenAIChatCompletionsModel, handoff , set_tracing_disabled
import os 
from httpx import Client
from rich import print
from dotenv import load_dotenv,find_dotenv
from agents import handoff
import asyncio
load_dotenv()
set_tracing_disabled(True)


key = os.getenv("GEMINI_API_KEY")
base_url= os.getenv("BASE_URL")
gemini_client=AsyncOpenAI(api_key=key , base_url=base_url)
Model = OpenAIChatCompletionsModel( model= "gemini-2.5-flash", openai_client= gemini_client)



calculate = Agent(name="calculater ",
                instructions= " you are helpful calculater agent which can calculate any number ",
                model= Model,
                )
chines = Agent(name="chines agent",
             instructions="""you are helpful chines agent ."Always translate the user’s text into natural,
             easy-to-understand chines while keeping the original meaning accurate and fluent.""",
             model=Model
             )

coach  = Agent(name = " assistant",
              instructions = """you are helpful  assistant.""",
              model = Model,
              handoffs=[ chines ,calculate])
              

result = Runner.run_sync(coach ,"what is 37 +32=? ")
print(result.final_output)


