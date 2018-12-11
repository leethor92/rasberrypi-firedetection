from sense_hat import SenseHat
from wia import Wia
import time

wia = Wia()
wia.access_token = "d_sk_A0AZjrtuvsYqWmp1WbVXStVS"
sense = SenseHat()
sense.clear()
green = (0,255,0)
orange = (255,165,0)
red = (255,0,0)
while True:
  temp=round(sense.get_temperature(),2)
  if temp >=50:
    sense.show_message("FIRE!",text_colour = red)
  elif temp >=35:
    sense.show_message("warning",text_colour = orange)
  else:
    sense.show_message("Fine!",text_colour = green)
  time.sleep(10)
  wia.Event.publish(name="temperature",data=temp)
