from flask import jsonify, Flask, request

app=Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "<h1>Welcome to My Flask API!</h1>"

@app.route('/about', methods=['GET'])
def about():
    # Pass a Python dict to jsonify, not a string
    return jsonify({
        "name": "Your Name",
        "course": "MCON-504 - Backend Development",
        "semester": "Spring 2025"
    })

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return f'<p>Hello, {name}! Welcome to Flask.</p>'

@app.route('/calculate', methods=['GET'])
def calculate():
    try:
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
    except (ValueError, TypeError):
        return jsonify({'error': 'Please enter valid numbers!'}), 400

    operation = request.args.get('operation', 'add').lower()

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({'error': 'cannot divide by zero!'}), 400
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operation!'}), 400

    return jsonify({'result': result, 'operation': operation})

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    if not(data):
        return jsonify({'error': 'No data provided!'})
    data['echoed'] = True
    return jsonify(data)

@app.route('/status/<int:code>', methods=['GET'])
def status(code):
    return f'This is a {code} error', code

if __name__ == '__main__':
    app.run(debug=True, port=5000)
