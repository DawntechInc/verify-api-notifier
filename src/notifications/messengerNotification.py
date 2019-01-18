import requests

def notifyUser():
  '''
  Function for notifying admin via Facebook messenger.
  @param {void}\n
  @return {void}\n
  '''
  headers = {
      "content-type": "application/json"
  }
  data = {
    "recipient": {
      "id": <PAGE-SCOPED-ID-USER-HERE>
    },
    "message": {
      "text": "API has stopped working :("
    },
    "messaging_type":"RESPONSE"
  }

  requests.post(
      url="https://graph.facebook.com/v2.6/me/messages?access_token=<PAGE_ACCESS_TOKEN_HERE>",
      headers=headers,
      json=data
  )
