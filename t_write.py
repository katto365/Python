from requests_oauthlib import OAuth1Session

CK = ''                             # Consumer Key
CS = ''         # Consumer Secret
AT = '' # Access Token
AS = ''         # Accesss Token Secert

url_text = "https://api.twitter.com/1.1/statuses/update.json"

# 本文
tweet = ""
tweet_id = ""

# 実行
if len(tweet_id) == 0:
    # 通常
    req = OAuth1Session(CK, CS, AT, AS).post(url_text, params = {"status": tweet})
else:
    # replyの場合
    req = OAuth1Session(CK, CS, AT, AS).post(url_text, params={"status": tweet, "in_reply_to_status_id": tweet_id})

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
