#!/usr/bin/env python
# -*- coding: utf-8 -*-

from requests_oauthlib import OAuth1Session
from datetime import datetime
import json

CK = ''                             # Consumer Key
CS = ''         # Consumer Secret
AT = '' # Access Token
AS = ''         # Accesss Token Secert

# パラメータ
tweet_id = ""

# 実行
timeline = OAuth1Session(CK, CS, AT, AS).get("https://api.twitter.com/1.1/statuses/show.json?id=" + tweet_id, params={})

# 結果を成形
tweet = json.loads(timeline.text)
reply_id = tweet["in_reply_to_status_id"]

# replyが付いていない場合
if reply_id is None:
    print("-----------------------")
    print("n1: " + tweet["user"]["name"])
    print("n2: " + tweet["user"]["screen_name"])
    tweet_text = tweet["text"]

    if len(tweet_text) > 50:
        print("t : " + tweet_text[0:50] + "[...]")
    else:
        print("t : " + tweet_text)

    print("-----------------------")

# replyが付いている場合
else:
    # reply元がある場合
    while reply_id is not None:
        print("-----------------------")
        print("n1: " + tweet["user"]["name"])
        print("n2: " + tweet["user"]["screen_name"])
        tweet_text = tweet["text"]

        reply = tweet["in_reply_to_screen_name"]
        print("r : " + reply)

        if len(tweet_text) > 50:
            print("t : " + tweet_text.replace("@" + reply + " ", "")[0:50] + "[...]")
        else:
            print("t : " + tweet_text.replace("@" + reply + " ", ""))

        # reply元のtweetを検索
        timeline = OAuth1Session(CK, CS, AT, AS).get(
            "https://api.twitter.com/1.1/statuses/show.json?id=" + str(reply_id), params={})

        # tweetの内容を書き換え
        tweet = json.loads(timeline.text)

        # 次のreply元を設定
        reply_id = tweet["in_reply_to_status_id"]

        print("-----------------------")

    # ここカッコ悪いからいずれ直す
    print("-----------------------")
    print("n1: " + tweet["user"]["name"])
    print("n2: " + tweet["user"]["screen_name"])
    tweet_text = tweet["text"]

    if len(tweet_text) > 50:
        print("t : " + tweet_text[0:50] + "[...]")
    else:
        print("t : " + tweet_text)

    print("-----------------------")
