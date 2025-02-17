# Agentic-AI Financial Agent

Agentic AI - Financial Agent with `agno`

## Project Description

Agentic-AI Financial Agent is a project that leverages various AI tools to provide financial insights, web search capabilities, web scraping, and YouTube video summarization. The project uses the `agno` library along with other dependencies to create agents that can fetch financial data, perform web searches, scrape websites, summarize YouTube videos, and present the information in a structured format.

## Features

- **Web Search Agent**: Searches the web for information and includes sources in the results using DuckDuckGo.
- **Financial Agent**: Fetches stock prices, analyst recommendations, stock fundamentals, and company news using YFinance.
- **Multi-Agent System**: Combines the capabilities of both agents to provide comprehensive financial insights.
- **Web Scraping Agent**: Crawls websites and extracts information using Crawl4ai.
- **YouTube Summarizing Agent**: Summarizes YouTube videos by gathering captions and video information.
- **Searxng Integration**: Agent capable of using a Searxng instance for web searches.
- **Playground**: Interactive web interface to interact with the agents.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/abinavrameshs/Agentic-AI-Financial-Agent.git
    cd Agentic-AI-Financial-Agent
    ```

2. Install dependencies using PDM:
    ```sh
    pdm install
    ```

3. Create a [.env](http://_vscodecontentref_/0) file with the necessary environment variables:
    ```sh
    PHI_API_KEY=<PHIDATA_API_KEY>
    GROQ_API_KEY=<GROK_API_KEY>
    OPENAI_API_KEY=<OPENAI_API_KEY> # Optional, if using OpenAI models
    GOOGLE_API_KEY=<GOOGLE_API_KEY> # Optional, if using Google models
    ```
   Make sure to obtain the API keys from the respective services and replace the placeholders with your actual keys.

## Usage

### Running the Playground

To run the playground application, execute the following command:
```sh
python playground.py
```
This will start the application and serve it using Uvicorn. You can then access the playground in your web browser.

## Running other agents

You can run the other agents directly from the command line:

`python financial_agent.py`

`python web_scraping.py`

`python youtube_summarizing.py`

`python web_scraping_searxyng.py`


## Project Structure

- `.env`: Contains environment variables for API keys and other configurations.
- `financial_agent.py`: Defines the financial agent and its capabilities, including web search and financial data retrieval.
- `playground.py`: Sets up the playground application with the defined agents, allowing interactive experimentation.
- `LICENSE`: Contains the GNU General Public License.
- `pdm.lock`: A lock file used by PDM to ensure consistent dependency resolution across different environments.
- `pyproject.toml`: Configuration file for the project, including dependencies, build system, and project metadata.
- `README.md`: The current file, providing an overview of the project.
- `web_scraping_searxyng.py`: Defines an agent that uses Searxng for web searches and Crawl4ai for web scraping.
- `web_scraping.py`: Defines an agent that uses Crawl4ai to crawl and extract information from websites.
youtube_summarizing.py: Defines an agent that summarizes YouTube videos using the YouTubeTools.

## Authors

Abinav Ramesh - abinavrameshs@gmail.com

## References

[Agno](https://docs.agno.com/introduction)
