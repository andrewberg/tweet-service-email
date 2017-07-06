from flask import Flask, request
app = Flask(__name__)

from functions import *

@app.route("/tweet-send", methods = ['POST', 'GET'])
def call():
	if request.method == 'POST':
		tid = request.form['tweet-id']
		send_tweet_mail(tid)
		return 'SUCCESS'

	return "ERROR"

if __name__ == '__main__':
    app.run(host= '0.0.0.0')