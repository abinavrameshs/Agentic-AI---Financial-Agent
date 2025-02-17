"""
For using Crawl4ai, you need to run `crawl4ai-setup` in the terminal.
Documentation : https://docs.crawl4ai.com/core/installation/
"""
from agno.models.groq import Groq
from agno.agent import Agent
from agno.tools.crawl4ai import Crawl4aiTools
from dotenv import load_dotenv
from agno.models.google import Gemini

load_dotenv()

# url = "https://github.com/microsoft/playwright/issues/17930"
url = "https://abinavrameshs.github.io/"

agent = Agent(
    tools=[Crawl4aiTools(max_length=1000)],
    model=Gemini(),
    instructions=["Crawl the given website and find out all information you can. Answer the user's questions."],
    show_tool_calls=True,
    markdown=True,
)
agent.print_response(f"Crawl the URL {url} and extract as much information as you can from the website. Be as elaborate as possible. Do not give short answers", stream=True)
