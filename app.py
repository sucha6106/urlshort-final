from flask import Flask, render_template, request, redirect
import random, string

app = Flask(__name__)
short_to_url = {}

def generate_short_id(num_of_chars: int) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=num_of_chars))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        original_url = request.form['url']
        short_id = generate_short_id(6)
        short_to_url[short_id] = original_url
        return render_template('home.html', short_url=request.host_url + short_id)
    return render_template('home.html', short_url=None)

@app.route('/<short_id>')
def redirect_to_url(short_id):
    url = short_to_url.get(short_id, 'https://www.google.com')
    return render_template('ad_page.html', final_url=url)

if __name__ == '__main__':
    app.run(debug=True)
