import time
from src.web import scrapping
from src.notifications import messengerNotification as notifications

while (True):
  print("API is Up and Running")
  feraApiDict = scrapping.getData()
  '''The return of the used API for this project has only one key in
     the returned JSON'''
  if (len(feraApiDict.keys()) < 1):
    notifications.notifyUser()
    print("API has Stopped Running")
    break
  time.sleep(1)
