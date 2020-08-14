# api key: q4JqeHIFDIUxr3xX3cIHLZHT5
# api secret key: tkY56KZV5EMwiHXj0gBjG739YobEQfGeGCYJ4hQhqgVL0ZXJWk
# bearer token: AAAAAAAAAAAAAAAAAAAAAKotGgEAAAAAlh%2FSzj76NMHthOhuDUQodTJ828c%3D4qFcUTV5PHnk32X5KY4LFLzH2ZHaYXV8MFIowQJHfedoJfxLhf

# access token: 8976762-X0FwsXbtA9vzPNc4p2skhmwH0Dyx455fhedeR42nP2
# access token secret: 39gCKiHjM2ArHC6iYYEv3rqk3TP5gftOHJMiWFvIj3rNS


import tweepy

consumer_key = "q4JqeHIFDIUxr3xX3cIHLZHT5"
consumer_secret = "tkY56KZV5EMwiHXj0gBjG739YobEQfGeGCYJ4hQhqgVL0ZXJWk"
access_token = "8976762-X0FwsXbtA9vzPNc4p2skhmwH0Dyx455fhedeR42nP2"
access_secret = "39gCKiHjM2ArHC6iYYEv3rqk3TP5gftOHJMiWFvIj3rNS"

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

tweets = api.search(q='#python')

# display results to screen
for t in tweets:
    print(t.created_at, t.text, "\n")