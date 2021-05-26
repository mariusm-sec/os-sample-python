from flask import Flask, request, jsonify
import fib
application = Flask(__name__)

@application.route("/")
def hello():
    return "Please visit /fibseq/NUMBER url to get Fibonacci sequence or /fib/NUMBER to get Fibonacci number.\n"

@application.route('/fibseq/<num>')
def show_fibonacci_sequence(num):
    if num[0] == '-':
        return jsonify({'input': num,
            'error': 'Negative value, service accepts only non-negative numbers', 'sequence': None}
            ), 400

    try:
        sequence = fib.fib_sequence(int(num))
        return jsonify({'input': num, 'error': None, 'sequence': sequence}), 200
    except ValueError as e:
        return jsonify({'input': num, 'error': str(e), 'sequence': None}), 400

@application.route('/fib/<num>')
def show_fibonnaci_number(num):
    try:
        fib_num = fib.fib_number(int(num))
        return jsonify({'input': num, 'error': None, 'number': fib_num}), 200
    except ValueError as e:
        return jsonify({'input': num, 'error': str(e), 'number': None}), 400

@application.route('/cache')
def show_cache():
    return jsonify(fib.cache())

if __name__ == "__main__":
    application.run()
