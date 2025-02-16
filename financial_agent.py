from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

from dotenv import load_dotenv
load_dotenv()
# websearch agent
websearch_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id = "llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

# Financial Agent

financial_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id = "llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        )
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[websearch_agent, financial_agent],
    instructions=["Always include sources", 
                  "Use tables to display the data",
                  "If provided any company, search for the corresponding ticker symbol before searching YFinance."],
    show_tool_calls=True,
    markdown=True,
    model=Groq(id = "llama-3.3-70b-versatile"),
)

multi_ai_agent.print_response(
    "Summarize analyst recommendations and share the latest news for the company NVIDIA",
    stream=True,
)
