from sense_hat import SenseHat
from wia import Wia
import time
import config
import json
import urllib2

WRITE_API_KEY=config.api_key

baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

wia = Wia()
wia.access_token = config.wia_token
sense = SenseHat()
sense.clear()

#Define below colours to display on sensehat
green = (0,255,0)
orange = (255,165,0)
red = (255,0,0)

#writeData defined to send temp data to Thingspeak
def writeData(temp):
  #Send data to Thingspeak in the query string
  conn = urllib2.urlopen(baseURL + '&field1=%s' % (temp))
  print(conn.read())
  #Connection closed
  conn.close()

#While loop that displays text based on the tempature read from sensehat
while True:
  #temperature is rounded to 2 deicmals
  temp=round(sense.get_temperature(),2)
  #if temp is over 50 or more user is alerted to fire by tweet & sensehat
  if temp >=50:
    sense.show_message("FIRE!",text_colour = red)
    writeData(temp)
  #if temp is 35 or more sensehat displays warning signal
  elif temp >=35:
    sense.show_message("warning",text_colour = orange)
  #else if temp is none of the above Fine in green is displayed on sensehat
  else:
    sense.show_message("Fine!",text_colour = green)
  #for demonstrative purposes loop will run every 10 seconds
  time.sleep(10)
  #temp is published to WIA & data stored
  wia.Event.publish(name="temperature",data=temp)
