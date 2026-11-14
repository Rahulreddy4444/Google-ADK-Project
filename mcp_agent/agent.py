from google.adk.agents.llm_agent import Agent
from pathlib import Path
from google.adk.tools.mcp_tool import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters


folder = Path(__file__).parent.joinpath("files").resolve()
folder.mkdir(exist_ok=True)




root_agent = Agent(
    model='gemini-3.5-flash',
    name='filesystem_agent',
    instruction=f"Help the user with files in the {folder} folder. You can read and write files in this folder. You can also list the files in this folder.",
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="npx",
                    args=["-y", "@modelcontextprotocol/server-filesystem", str(folder)],
                )
            )
        )
    ]
)
