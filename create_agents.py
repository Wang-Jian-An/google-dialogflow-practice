import os
import uuid
import pytest
from google.cloud.dialogflowcx_v3.services.agents.client import AgentsClient
from google.cloud.dialogflowcx_v3.types.agent import Agent
from google.cloud.dialogflowcx_v3.types import CreateAgentRequest

# PROJECT_ID = os.getenv("create-agent-with-api-6343d801abf5.json")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "create-agent-with-api-6343d801abf5.json"
pytest.AGENT_PATH = ""
agentName = f"fake_agent_{uuid.uuid4()}"

# 建立服務機制
agents_client = AgentsClient()


# 設定服務基本架構
agent = Agent(
    display_name=agentName,
    default_language_code="en",
    time_zone="America/Los_Angeles"
)

# 設定服務需求
project_id = "create-agent-with-api"
parent = f"projects/{project_id}/locations/global"
agent_request = CreateAgentRequest(parent=parent, agent=agent)

response = agents_client.create_agent(agent_request)
print(response)