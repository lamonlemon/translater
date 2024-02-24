from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_translate(text, source, target):
    client_id = "###"
    client_secret = "###"

    data = {'text': text,
            'source': source,
            'target': target}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id": client_id,
              "X-Naver-Client-Secret": client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if rescode == 200:
        send_data = response.json()
        trans_data = send_data['message']['result']['translatedText']
        return trans_data
    else:
        print("Error Code:", rescode)

@app.route('/', methods=['GET', 'POST'])
def index():
    languages = {
        'ko': 'Korean',
        'en': 'English',
        'ja': 'Japanese',
        'zh-CN': 'Simplified Chinese',
        'zh-TW': 'Traditional Chinese',
        'es': 'Spanish',
        'fr': 'French',
        'ru': 'Russian',
        'vi': 'Vietnamese',
        'th': 'Thai',
        'id': 'Indonesian',
        'de': 'German',
        'it': 'Italian'
    }

    if request.method == 'POST':
        source = request.form.get('source')
        target = request.form.get('target')
        text = request.form.get('text')

        if source and target and text:
            translated_text = get_translate(text, source, target)
            return render_template('index.html', languages=languages, translated_text=translated_text, text=text)
    
    return render_template('index.html', languages=languages)

if __name__ == '__main__':
    app.run(debug=True)
