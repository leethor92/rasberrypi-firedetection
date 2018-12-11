from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()
green = (0,255,0)
orange = (255,165,0)
red = (255,0,0)
while True:
  temp = sense.get_temperature()
  if temp >=50:
    sense.show_message("FIRE!",text_colour = red)
  elif temp >=35:
    sense.show_message("warning",text_colour = orange)
  else:
    sense.show_message("Fine!",text_colour = green)
  print(temp)
  time.sleep(10)
