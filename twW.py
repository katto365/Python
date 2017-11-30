from requests_oauthlib import OAuth1Session

CK = '' # Consumer Key
CS = '' # Consumer Secret
AT = '' # Access Token
AS = '' # Accesss Token Secert

# 本文
tw = ""

# 実行
res = OAuth1Session(CK, CS, AT, AS).post("https://api.twitter.com/1.1/statuses/update.json", params = {"status": tw})

# レスポンスを確認
if res.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % res.status_code)
