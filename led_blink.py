import RPi.GPIO as GPIO
import time
import argparse
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

parser = argparse.ArgumentParser(description="Flash LED on Pin 7 (GPIO04) at specific frequency.")
parser.add_argument('f', type=int, help="Frequency in Hz (cycles-per-second). Integer.")
args = parser.parse_args()

Freq = args.f
#Freq = input("Enter frequency in Hz: ") #Frequency you want light to flash in Hz
print("Flashing LED at " + str(Freq) + " Hz")
T = (1.0/Freq) #Converts to  period (sec/cycle)
while True:
	try:
		GPIO.output(7,True)
		time.sleep(T)
		GPIO.output(7,False)
		time.sleep(T)
	except KeyboardInterrupt:
		GPIO.cleanup()
		print "\n led_blink.py: Stopping Program"
