from flask import Flask, render_template, request, jsonify
from gradio_client import Client

client = Client("solo69/AlexanderHolmes0-fake-news-detector")

app = Flask(__name__)

def check_article(article_text):

    result = client.predict(
        param_0=article_text,
        api_name="/predict"
    )
    print(result)

    if result['label'] == 'true':
        return 'Real News'
    else:
        return 'Fake News'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    article_text = request.form['article']
    authenticity = check_article(article_text)
    return jsonify(result=authenticity)

if __name__ == '__main__':
    app.run(debug=True)