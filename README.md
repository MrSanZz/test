## Counter Booking System with IP Restriction

This example allows a visitor to book a counter increment only once, using IP detection. The count persists even after page refresh.

### Frontend Code (HTML & JavaScript)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Counter Booking</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        #counter { font-size: 2em; margin: 20px; }
        button { font-size: 1.2em; padding: 10px 20px; }
    </style>
</head>
<body>
    <div>
        <span id="counter">Loading...</span>
        <br>
        <button id="bookButton">Book!</button>
    </div>

    <script>
        const counterElement = document.getElementById('counter');
        const bookButton = document.getElementById('bookButton');

        async function fetchCounter() {
            const response = await fetch('/get_counter');
            const data = await response.json();
            counterElement.textContent = data.count;
            if (data.alreadyBooked) {
                bookButton.textContent = "You already book this!";
                bookButton.disabled = true;
            }
        }

        async function bookCounter() {
            const response = await fetch('/book', { method: 'POST' });
            const data = await response.json();
            if (data.success) {
                counterElement.textContent = data.newCount;
                bookButton.textContent = "You already book this!";
                bookButton.disabled = true;
            } else {
                alert(data.message);
            }
        }

        bookButton.addEventListener('click', bookCounter);
        fetchCounter();
    </script>
</body>
</html>
```

### Backend Code (Python with Flask)

```python
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Initialize the counter and IP log
DATA_FILE = 'data.json'

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"count": 0, "ip_log": []}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/get_counter', methods=['GET'])
def get_counter():
    data = load_data()
    client_ip = request.remote_addr
    already_booked = client_ip in data['ip_log']
    return jsonify({"count": data['count'], "alreadyBooked": already_booked})

@app.route('/book', methods=['POST'])
def book():
    data = load_data()
    client_ip = request.remote_addr

    if client_ip in data['ip_log']:
        return jsonify({"success": False, "message": "You have already booked this!"})

    data['count'] += 1
    data['ip_log'].append(client_ip)
    save_data(data)
    return jsonify({"success": True, "newCount": data['count']})

if __name__ == '__main__':
    app.run(debug=True)
```

### Setup Instructions

1. Save the HTML & JavaScript code into a file named `index.html`.
2. Save the Python code into a file named `app.py`.
3. Create an empty file named `data.json` in the same directory.
4. Run the Flask server:
   ```bash
   python app.py
   ```
5. Open `index.html` in a browser to test the application.

### Notes
- The counter value is stored persistently in `data.json`.
- The IP address log ensures each visitor can only book once.
