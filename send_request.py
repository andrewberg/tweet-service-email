import requests

# api-endpoint
URL = "http://bergcode.com:5000/tweet-send"

# sending post request and saving the response as response object
r = requests.post(url = URL, data = {'tweet-id':input_data['twit_id']})