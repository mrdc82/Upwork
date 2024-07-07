from flask import Flask, request, render_template, redirect, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def save_website_text_to_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
        return f"Website text has been saved to {filename}"
    else:
        return f"Failed to retrieve the website. Status code: {response.status_code}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        filename = request.form['filename']
        message = save_website_text_to_file(url, filename)
        return redirect(url_for('index', message=message))
    message = request.args.get('message')
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
