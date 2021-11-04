import os
import dialogflow
from google.api_core.exceptions import InvalidArgument

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'booking-room-lesq-f3f6a4258a59.json'
DIALOGFLOW_PROJECT_ID = 'booking-room-lesq'
DIALOGFLOW_LANGUAGE_CODE = 'zh-TW'
SESSION_ID = 'anything'



session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

while True:
    text_to_be_analyzed = input("請輸入文字：")
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        print("回應的話:", response.query_result.fulfillment_text)
    except InvalidArgument:
        raise

print("輸入文字:", response.query_result.query_text)
print("得到的 intent:", response.query_result.intent.display_name)
print("偵測到 intent 的 confidence:", response.query_result.intent_detection_confidence)
print("回應的話:", response.query_result.fulfillment_text)
