#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
import json

# 認証情報
CK = '' # Consumer Key
CS = '' # Consumer Secret
AT = '' # Access Token
AS = '' # Accesss Token Secert

# 実行
timeline = OAuth1Session(CK, CS, AT, AS).get("https://api.twitter.com/1.1/statuses/home_timeline.json", params = {})

# 結果を成形
for tweet in json.loads(timeline.text):

    print("-----------------------")
    print("n1: " + tweet["user"]["name"])
    print("n2: " + tweet["user"]["screen_name"])

    tweet_text = tweet["text"]
    reply = tweet["in_reply_to_screen_name"]
    if reply is not None:
        print("r : " + reply)
        if len(tweet_text) > 50:
            print("t : " + tweet_text.replace("@" + reply + " ", "")[0:50] + "[...]")
        else:
            print("t : " + tweet_text.replace("@" + reply + " ", ""))
    else:
        if len(tweet_text) > 50:
            print("t : " + tweet_text[0:50] + "[...]")
        else:
            print("t : " + tweet_text)
    print("-----------------------")
