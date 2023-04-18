import RPi.GPIO as GPIO
from time import sleep

# Format: {container_num : gpio pin}
CONTAINER_PINS = {1 : 27, 2 : 3, 3 : 4, 4 : 2, 5 : 22, 6 : 10, 7 : 6, 8 : 0}

# Format: {flavor_num : [gpio actuator_out, gpio actuator_in]}
FLAVOR_PINS = {1 : [1, 2], 2 : [3, 4], 3 : [5, 6], 4 : [7,8]}
FLAVOR_TIME = 1.0 # seconds

FLOW_RATE = 1.0 # oz/sec

'''
Initialize our pumping system
'''
def init_pumping_system():
	GPIO.setmode(GPIO.BCM)
	for i in range(27):
		GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	'''
	for _, pin in CONTAINER_PINS.items():
		GPIO.setup(pin, GPIO.OUT)
		GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
		GPIO.output(pin, )
	for _, pin_set in FLAVOR_PINS.items():
		for pin in pin_set:
			GPIO.setup(pin, GPIO.OUT)
			GPIO.output(pin, 0)
	'''

'''
Externally called by the drink server. Will fill in a flavor object which
is through an actuator.
'''
def flavor_out(flavor_num):
	GPIO.setup(FLAVOR_PINS[flavor_num][0],GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.output(FLAVOR_PINS[flavor_num][1],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	sleep(FLAVOR_TIME)
	GPIO.output(FLAVOR_PINS[flavor_num][0],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.output(FLAVOR_PINS[flavor_num][1],GPIO.IN, pull_up_down=GPIO.PUD_UP)
	sleep(FLAVOR_TIME)
	GPIO.output(FLAVOR_PINS[flavor_num][1],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	return 0


'''
Externally called by the drink server. Will fill in a container object
and then will determine the sleep time from the ounces_requested.
'''
def pump_out(container_num, ounces_requested):
	time_on = ounces_requested / FLOW_RATE
	GPIO.setup(CONTAINER_PINS[container_num],GPIO.IN, pull_up_down=GPIO.PUD_UP)
	sleep(time_on)
	GPIO.output(CONTAINER_PINS[container_num],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	return 0
