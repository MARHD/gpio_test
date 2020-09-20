#This makes led go on wen switch pres, ghghh

import RPi.GPIO as GPIO;
from time import sleep;

GPIO.setmode(GPIO.BOARD);
GPIO.setwarnings(False);

ini = 31;
out = 29;

GPIO.setup(ini, GPIO.IN, pull_up_down=GPIO.PUD_UP);
GPIO.setup(out, GPIO.OUT, initial=0);

pressed = 0;
def b_cb(channel):
	pressed = 1;
	print("button pressed");

	if pressed == 1:
        	GPIO.output(out, 1);
        	pressed=0;
		sleep(0.01)
	if pressed == 0:
        	GPIO.output(out, 0);
        	pressed=0;
		sleep(0.01);

GPIO.add_event_detect(ini, GPIO.RISING, callback=b_cb, bouncetime=200);
message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup();

