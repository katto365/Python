import discord
import urllib.parse

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("test"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:

            print(dir(client))
            print("")
            print(dir(message))

    if message.content.startswith("!wiki"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:

            if len(message.content) >= 6:
                str = message.content.split(None, 1)
                enc = urllib.parse.quote(str[1])

                # メッセージを書きます
                m = "次の検索結果を表示しています：" + str[1] + "( https://ja.wikipedia.org/wiki/" +  enc + " )"
                # メッセージが送られてきたチャンネルへメッセージを送ります
                await client.send_message(message.channel, m)

    if message.content.startswith("!google"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:

            if len(message.content) >= 8:
                str = message.content.split(None, 1)
                enc = urllib.parse.quote(str[1])

                # メッセージを書きます
                m = "ぐぐったよ★ミ：" + str[1] + "( https://www.google.co.jp/search?q=" +  enc + "&oq=" + enc + " )"
                # メッセージが送られてきたチャンネルへメッセージを送ります
                await client.send_message(message.channel, m)


client.run("確かここにdiscordのキーを入れる")