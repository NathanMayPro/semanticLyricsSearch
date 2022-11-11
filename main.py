from service.genius import twitter

request_token, request_token_secret = tuple(twitter.get_request_token())
authorize_url = twitter.get_authorize_url(request_token)

print('Visit this URL in your browser: ' + authorize_url)
pin = raw_input('Enter PIN from browser: ')