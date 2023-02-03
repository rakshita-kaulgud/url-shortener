from flask import Flask, request, render_template
import hashlib

app = Flask(__name__)

map = {}
    

@app.route('/shortenUrl', methods=['GET', 'POST'])
def shortenUrl():
    if request.method == 'POST':
        url = request.form['url']
        # generate hash of the URL
        hashed_url = hashlib.sha224(url.encode('utf-8')).hexdigest()[:8]
        map[hashed_url] = url
        print(map)
        return f"Shortened URL: http://url-shortener.com/{hashed_url}"

    return render_template('index.html')

@app.route('/getUrl', methods=['GET', 'POST'])
def getUrl():
    if request.method == 'POST':
        code = request.form['code']
        # fetch long url
        if code not in map:
            return f"Incorrect code, no mapping found. Try again"
        url = map[code]
        return f"URL: {url}"
    return render_template('longUrlForm.html')

if __name__ == '__main__':
    app.run(debug=True)
