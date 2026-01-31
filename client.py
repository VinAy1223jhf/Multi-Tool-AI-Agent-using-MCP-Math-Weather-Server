from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq
# from langchain_core

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    # here we will list the name of mcp server clients(tools which we created earlier)
    client=MultiServerMCPClient({
        "Math":{
            "command":"python",
            "args":["mathserver.py"],
            "transport":"stdio",
        },
        "Weather":{
            "url":"http://127.0.0.1:8000/mcp",
            "transport":"streamable-http",
        }
    })

    import os
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

    tools=await client.get_tools()
    model=ChatGroq(model="qwen/qwen3-32b")
    agent=create_agent(
        model,tools
    )

    math_response=await agent.ainvoke(
        {"messages":[{"role":"user","content":"what's (3+4)*12?"}]}
    )

    print("math_response:",math_response["messages"][-1].content)

    weather_response=await agent.ainvoke(
        {"messages":[{"role":"user","content":"what's the weather in dwarka sec-3 today?"}]}
    )

    print("weather_response:",weather_response["messages"][-1].content)


asyncio.run(main())