# rasberrypi-firedetection
Rasberry Pi Fire detection system 

Lee Thornton, 20041034

Tools, Technologies and Equipment
The target of this project is to build a smart fire alarm system based on heat. I would like to detect if heat goes to a certain temperature similar to what sprinkler systems use. When detected it will display a warning on the raspberry pi sensehat. Heat readings will be taken intermittently & the information will be stored in via Wia & the information is viewable via website. I would also like to enable the user to be notified by phone if the heat goes above 50 degrees celcius thingtweet is utilized to notify of the possibility of a fire.
 I would propose that the script files used to control the program be developed using python & JavaScript. The information generated by this will be stored on WIA with a display graph. Information would also be available via website & I would like to try & make some UX changes using HTML, possibly with CSS. As for notifying users I would propose using MQTT & possibly Blynk for mobile display information.
 
Hardware
Rasberry Pi *2
Sense-Hat
(Possibly MQ2 sensor for smoke detection)

Programming Languages
Python
HTML
Javascript
CSS

to Run scripts used commands
python heat.py
node fire-blynk.js

Temperature data can be viewed below
https://raspberrypi-firealarm.glitch.me/

The fire-blynk.js file is designed to be used in conjuction with the Blynk mobile app to control & on/off vitrual pin of a smart sprinkler system, once the user is notified of a fire the user can remotely trigger the sprinkler system using their mobile phone.
