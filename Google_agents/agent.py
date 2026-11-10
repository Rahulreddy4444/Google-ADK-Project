from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search
from google.adk.code_executors import BuiltInCodeExecutor

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that can search the web for information.',
    instruction='Answer user questions to the best of your knowledge',
    tools=[google_search],
    code_executor=BuiltInCodeExecutor(),
)
