from agno.models.groq import Groq
from agno.agent import Agent
from agno.tools.youtube import YouTubeTools
from dotenv import load_dotenv

load_dotenv()
agent = Agent(
    tools=[YouTubeTools()],
    show_tool_calls=True,
    description="You are a very powerful YouTube agent who can gather captions, and video information from any youtube video."
     "Obtain all information from a YouTube video and answer questions.",
    model=Groq(id="llama-3.3-70b-versatile"),
)

# Doesnt work properly
agent.print_response(
    "Summarize this video https://www.youtube.com/watch?v=Iv9dewmcFbs", markdown=True
)
