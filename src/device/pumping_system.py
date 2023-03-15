import RPi.GPIO as GPIO
from time import sleep
import Container

CONTAINER_PINS = {1 : 2, 2 : 3, 3 : 4, 4 : 15, 5 : 27}
FLOW_RATE = 1.0 # oz/sec

'''
Initialize our pumping system
'''
def init_pumping_system():
	GPIO.setmode(GPIO.BCM)
	for _, pin in CONTAINER_PINS:
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, 0)
	

'''
Externally called by the drink server. Will fill in a container object
and then will determine the sleep time from the ounces_requested.
'''
def pump_out(container_obj, ounces_requested):
	if(ounces_requested > container_obj.container_level):
		return -1
	time_on = ounces_requested / FLOW_RATE;
	GPIO.output(CONTAINER_PINS[container_obj.container_num],1); 
	sleep(time_on);
	GPIO.output(CONTAINER_PINS[container_obj.container_num],0);
	return 0