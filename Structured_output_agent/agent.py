from google.adk.agents.llm_agent import Agent
from pydantic import BaseModel, Field
from typing import Literal

class Enquiry(BaseModel):
    name: str | None = Field(default=None, description="Name of the student in capital letters")
    email: str | None = Field(default=None, description="Email address of the student")
    interested_in: list[Literal["Bachelor's Degree", "Master's Degree", "PhD"]] | None = Field(default=None, description="List of courses the student is interested in")
    budget: int = Field(default=None, ge=0, le=100000, description="The budget for the student's enquiry")

root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='extract student enquiry details from the message',
    instruction='read the student enquiry message and extract the details into a structured format',
    output_schema=Enquiry,
    output_key='enquiry', #state the key in which the output will be stored in the agent's memory
)
