import RPi.GPIO as GPIO
from time import sleep
import threading

# Format: {container_num : gpio pin}
CONTAINER_PINS = {1 : 19, 2 : 11, 3 : 22, 4 : 27, 5 : 12, 6 : 1}
STIR_PIN = 7
STIR_TIME = 4 # seconds
CLEAN_PIN = 4
CLEAN_TIME = 4 # seconds
DRAIN_PIN = 20
# Format: {flavor_num : [gpio actuator_out, gpio actuator_in]}
FLAVOR_PINS = {1 : [14, 26], 2 : [24, 23], 3 : [5, 6], 4 : [7,8]}
FLAVOR_TIME = 0.3 # seconds

FLOW_RATE = 1.0 # oz/sec

'''
Initialize our pumping system
'''
def init_pumping_system():
	GPIO.setmode(GPIO.BCM)
	for i in range(27):
		GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

'''
Externally called by the drink server. Will fill in a flavor object which
is through an actuator.
'''
def flavor_out(flavor_num):
	GPIO.setup(FLAVOR_PINS[flavor_num][0],GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(FLAVOR_PINS[flavor_num][1],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	sleep(FLAVOR_TIME)
	GPIO.setup(FLAVOR_PINS[flavor_num][0],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(FLAVOR_PINS[flavor_num][1],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	return 0

# Function to clean the system upon request from server
def clean_system():
	global CLEAN_PIN, CLEAN_TIME
	GPIO.setup(CLEAN_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	sleep(CLEAN_TIME)
	GPIO.setup(CLEAN_PIN,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(DRAIN_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	sleep(CLEAN_TIME)
	GPIO.setup(DRAIN_PIN,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# This is the server's main function. It will pump out the drink
def pump_handler(order_array):
	threads = []
	order_time = 0
	for order in order_array:
		order_time += order[1] / FLOW_RATE
		thread = threading.Thread(target=pump_out, args=(order[0], order[1]))
		threads.append(thread)

	for thread in threads:
		thread.start()

	for thread in threads:
		thread.join()
	
	stir()
	drain(order_time)

# This is a helper function for pump_handler to stir the drink
def stir():
	GPIO.setup(STIR_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	sleep(STIR_TIME)
	GPIO.setup(STIR_PIN,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# This is a helper function for pump_handler to dispense the drink
def drain(order_time):
	GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(DRAIN_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP)
	sleep(order_time)
	GPIO.setup(DRAIN_PIN,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# This is a helper function for pump_handler to pump out a drink
def pump_out(container_num, ounces_requested):
	time_on = ounces_requested / FLOW_RATE
	GPIO.setup(CONTAINER_PINS[container_num],GPIO.IN, pull_up_down=GPIO.PUD_UP)
	sleep(time_on)
	GPIO.setup(CONTAINER_PINS[container_num],GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	return 0