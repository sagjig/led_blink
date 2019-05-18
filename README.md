For use on a Raspberry Pi (developed on RPi 2B+). Flashes an LED using a 3.3v pin at a specified frequency.


LED must be on Pin 7, A.K.A. GPIO04.
Run with "python led_blink.py #", with # being the frequency at which to flash the LED in hertz (cycles-per-second).

e.g. "python led_blink.py 3" for flashing the LED at 3 Hz.

Help is printed with "python led_blink.py -h" or "python led_blink.py --help"
