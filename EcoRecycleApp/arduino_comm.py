import serial
import time

def send_open_signal():
    try:
        arduino = serial.Serial('/dev/tty.usbserial-1120', 9600, timeout=1)
        time.sleep(2)  # Give time to Arduino to reset
        arduino.write(b'O')  # 'O' is signal to open panel
        print("✅ Signal sent to Arduino.")
        arduino.close()
    except Exception as e:
        print(f"❌ Error: {e}")
