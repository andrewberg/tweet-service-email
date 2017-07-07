from flask import Flask, request
app = Flask(__name__)

from functions import *

@app.route("/tweet-send", methods = ['POST', 'GET'])
def call():
	retval = False

	if request.method == 'POST':
		tid = request.form['tweet-id']
		retval = send_tweet_mail(tid, False) # No retweets, "FALSE"

	if retval:
		return "SUCCESS"
	else:
		return "FAILURE - Possible retweet"

if __name__ == '__main__':
    app.run(host= '0.0.0.0')