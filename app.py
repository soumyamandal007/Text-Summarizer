from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_text():
    data = request.get_json()
    article = data.get('article')
    max_value = data.get('maxValue')
    min_value = data.get('minValue')
    print(article,max_value,min_value)

    if not article:
        return jsonify({'error': 'Article text is required'}), 400

    summary = summarizer(article, max_length=max_value, min_length=min_value, do_sample=False)[0]['summary_text']
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)