from flask import Flask, request, render_template
import hashlib

app = Flask(__name__)

map = {}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/shortenUrl', methods=['POST'])
def shortenUrl():
    url = request.form['url']
    # generate hash of the URL
    hashed_url = hashlib.sha224(url.encode('utf-8')).hexdigest()[:8]
    map[hashed_url] = url
    print(map)
    return f"Shortened URL: http://url-shortener.com/{hashed_url}"

@app.route('/getUrl', methods=['POST'])
def getUrl():
    code = request.form['code']
    # fetch long url
    url = map[code]
    return f"URL: {url}"

@app.route('/getLongUrl', methods=['GET'])
def getLongUrl():
    return render_template('longUrlForm.html')

if __name__ == '__main__':
    app.run(debug=True)
