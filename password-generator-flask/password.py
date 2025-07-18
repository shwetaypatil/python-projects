from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('password.html')

@app.route('/', methods=['POST'])
def generate_password():
    length = int(request.form.get('length', 20))
    password_type = request.form.get('password_type', 'random')
    include_numbers = 'numbers' in request.form
    include_symbols = 'symbols' in request.form

    def get_random(length):
        chars = string.ascii_letters
        if include_numbers:
            chars += string.digits
        if include_symbols:
            chars += string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))

    def get_alphanumeric(length):
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def get_strong(length):
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(length))

    def get_pin(length):
        return ''.join(random.choice(string.digits) for _ in range(min(length, 10)))

    def get_passphrase(num_words=4):
        words = ['sun', 'moon', 'light', 'dream', 'wave', 'code', 'love', 'sky']
        return '-'.join(random.choice(words) for _ in range(num_words))

    if password_type == 'alphanumeric':
        password = get_alphanumeric(length)
    elif password_type == 'strong':
        password = get_strong(length)
    elif password_type == 'pin':
        password = get_pin(length)
    elif password_type == 'passphrase':
        password = get_passphrase()
    else:
        password = get_random(length)

    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
