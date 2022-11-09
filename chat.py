import os
from google.cloud import dialogflow_v2 as dialogflow

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "claves.json"
client  = dialogflow.SessionsClient()
session = client.session_path(project="python-9vll" , session="me")

def get_response(msg):
    text_input = dialogflow.TextInput(text=msg, language_code = "es")
    query_input = dialogflow.QueryInput(text=text_input)
    response =  client.detect_intent(query_input=query_input , session=session)
    return response.query_result.fulfillment_text
   # print(response.query_result.fulfillment_text)





