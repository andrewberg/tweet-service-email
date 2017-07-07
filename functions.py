import smtplib, tweepy, re

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from twitnewsconfig import *

def send_tweet_mail(tweet_id, tweet_retweets):
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

	api = tweepy.API(auth)

	tweet = api.get_status(tweet_id, tweet_mode='extended')

	if (tweet_retweets == False):
		if (hasattr(tweet, 'retweeted_status')):
			return False

	tweet_img_url = ""
	tweet_has_img = False

	if (hasattr(tweet, 'extended_entities')):
		tweet_img_url = tweet.extended_entities['media'][0]['media_url']
		tweet_has_img = True


	#print(api.rate_limit_status())

	tweet_txt = tweet.full_text
	tweet_link = "http://twitter.com/a/status/" + str(tweet_id)

	tweet_author_name = tweet.author.name
	tweet_author_sname = tweet.author.screen_name
	tweet_author_pimg = tweet.author.profile_image_url_https

	me = "dailynews@pobox.com"
	you = "dailynews@pobox.com"


	tweet_txt = tweet_txt.encode('ascii', 'ignore')
	tweet_txt = re.sub('\n', ' ', tweet_txt)

	tweet_subject = re.sub('(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '', tweet_txt)

	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = tweet_subject
	msg['From'] = tweet_author_sname + '@pobox.com'
	msg['To'] = you

	# Create the body of the message (a plain-text and an HTML version).
	text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
	html = """<div><div id="tweet" style="border-radius: 6px;border: 1px solid #8A837B;padding: 20px; " ><img style="float:left; margin-right:10px;" src='""" + tweet_author_pimg + """'></img>""" + """<div class='tweet_sname' style="float:left;"><h5>@""" + tweet_author_sname + """</h5></div><p style="clear:both; padding-top:20px; font-size: 16px;">""" + tweet_txt + """  </p> """ + """<p><a href='""" + tweet_link + """' target="_blank"><img src='""" + tweet_img_url + """' style='width:100%;' border="0"></a></p> <a href='""" + tweet_link + """'>""" + tweet_link + """ </a> </div> <p style="font-size:9px;margin-top:15px;color:#8A837Bpadding-top:15px;">&copy; 2017 SRG, LLC</p></div>"""

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)
	
	# Send the message via local SMTP server.
	mail = smtplib.SMTP(smtp_ip, smtp_port)
	mail.ehlo()

	mail.starttls()

	mail.login(smtp_user, smtp_pass)
	mail.sendmail(me, you, msg.as_string())
	mail.quit()

	return True