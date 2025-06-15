from flask import Flask, render_template, request, session, redirect, url_for
import pyttsx3
import threading
import serial
import time

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session storage

# 🔉 Speak asynchronously
def speak_async(message):
    def run():
        engine = pyttsx3.init()
        engine.setProperty('rate', 165)
        engine.say(message)
        engine.runAndWait()
    threading.Thread(target=run).start()

# 🧠 Function to send signal to Arduino to open panel (Servo 1)
def send_open_signal():
    try:
        arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # ⚠️ Update port as per your system
        time.sleep(2)  # Give time to reset
        arduino.write(b'O')  # 'O' = Open panel
        print("✅ Panel open signal sent to Arduino.")
        arduino.close()
    except Exception as e:
        print(f"❌ Error sending open signal: {e}")

# ------------------ ROUTES ------------------

@app.route('/')
def welcome():
    speak_async("Welcome to Incentivised Plastic or Metallic Can Recycling Machine. Let's start recycling.")
    return render_template('welcome.html')

@app.route('/enter-items', methods=['GET'])
def enter_items():
    speak_async("Please enter how many number of plastic bottles or metal cans you want to recycle?")
    return render_template('enter_items.html')

@app.route('/start-recycling', methods=['POST'])
def start_recycling():
    num_items = request.form.get('item_count')

    if num_items:
        # 🔐 Save item count in session for later use
        session['item_count'] = int(num_items)

        # 🗣️ Speak and open panel via Arduino
        speak_async("Opening the panel. Please insert your first bottle or metallic can.")
        send_open_signal()

        # 🔁 Show scanning animation page
        return render_template('scanning.html')

    return "Invalid input", 400

# --------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)