import requests

def getData():
  '''
  Function for notifying admin via Facebook messenger.
  @param {void}\n
  @return {void}\n
  '''
  get_response = requests.get(url='http://<LINK_API_HERE>')
  return get_response.json()
