from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.integrations.langchain import LangchainTool
from langchain_tavily import TavilySearch


# 1.create a TavilySearch tool instance
tavily_search = TavilySearch(
    max_results=5,
    topic="general",
)

# 2.wrap it so ADK can use it
tavily_search_tool = LangchainTool(tool=tavily_search, name="tavily_search", description="Search the web using Tavily.")

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that can search the web using Tavily.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[tavily_search_tool],
)
