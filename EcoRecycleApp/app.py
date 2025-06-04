from flask import Flask, render_template, request
from arduino_comm import send_open_signal

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/enter-items')
def enter_items():
    return render_template('enter_items.html')

@app.route('/start-recycling', methods=['POST'])
def start_recycling():
    item_count = int(request.form['item_count'])
    print(f"User entered {item_count} items to recycle.")
    
    try:
        send_open_signal(item_count)
        return "✅ Panel opened successfully! You may now insert items."
    except Exception as e:
        print("❌ Error:", e)
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
