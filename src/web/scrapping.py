import requests

def getData():
  '''
  Function for notifying admin via Facebook messenger.
  @param {void}\n
  @return {void}\n
  '''
  get_response = requests.get(url='https://api.sandbox.amadeus.com/v1.2/airports/autocomplete')
  return get_response.json()
