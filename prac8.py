from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

lcd = LCD()

def safe_exit(signum, frame):
    lcd.clear()
    exit(1)

try:
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    lcd.text("hello", 1)
    lcd.text("raspberry pi!", 2)
    pause()
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
