from flask import Flask, render_template, request
import pyttsx3
import threading

app = Flask(__name__)

# 🔉 Speak async (non-blocking)
def speak_async(message):
    def run():
        engine = pyttsx3.init()
        engine.setProperty('rate', 165)
        engine.say(message)
        engine.runAndWait()
    threading.Thread(target=run).start()

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
    num_items = request.form.get('item_count')  # Fixed field name
    if num_items:
        return f"You entered {num_items} items to recycle!"
    return "Invalid input", 400

if __name__ == '__main__':
    app.run(debug=True)
