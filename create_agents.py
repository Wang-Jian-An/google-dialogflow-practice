import os
import uuid
import pytest
from google.cloud.dialogflowcx_v3.services.agents.client import AgentsClient
from google.cloud.dialogflowcx_v3.types.agent import Agent

# PROJECT_ID = os.getenv("create-agent-with-api-6343d801abf5.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "create-agent-with-api-6343d801abf5.json"
pytest.AGENT_PATH = ""

def create_agent(project_id, display_name):

    parent = "projects/" + project_id + "/locations/global"

    agents_client = AgentsClient()

    agent = Agent(
        display_name=display_name,
        default_language_code="en",
        time_zone="America/Los_Angeles",
    )

    response = agents_client.create_agent(request={"agent": agent, "parent": parent})

    return response

agentName = f"fake_agent_{uuid.uuid4()}"
response = create_agent("create-agent-with-api", agentName)
print(response)