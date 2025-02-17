from agno.agent import Agent
from agno.tools.searxng import Searxng
from agno.models.google import Gemini
from dotenv import load_dotenv
from agno.models.groq import Groq

load_dotenv()
# Initialize Searxng with your Searxng instance URL
searxng = Searxng(
    host="http://localhost:53153",
    engines=[],
    fixed_max_results=5,
    news=True,
    science=True
)

# Create an agent with Searxng
agent = Agent(tools=[searxng],model=Groq(id="llama-3.3-70b-versatile"),show_tool_calls=True,markdown=True, retries=5)


# Example: Ask the agent to search using Searxng : WORKED
# agent.print_response("""
# Please search for information about artificial intelligence
# and summarize the key points from the top results
# """)

# Crawl a website : DOES not work
agent.print_response("""
Can you please crawl this website https://github.com/agno-agi/agno and summarize the key points?
""")