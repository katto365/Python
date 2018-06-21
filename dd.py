import discord
import urllib.parse

#import boto3

#NOTIFICATION_CHANNEL = os.environ['NOTIFICATION_CHANNEL']

#code_deploy = boto3.client('codedeploy', region_name='ap-northeast-1')

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # テスト
    if message.content.startswith("!test"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:

            #channel = client.get_channel(423472886955638784)

            print(dir(client))
            print(client.channel.id)
            #await client.send_message("423472886955638784", "channel：" + str(message.channel))

            await client.send_message(client.get_channel(423472886955638784), "通知てすと")

    if message.content.startswith("!MinecraftServerStart"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:

            # awscliでサーバ起動

            # 起動完了メッセージ
            await client.send_message(message.channel, "Minecraft Server 起動中（大嘘） ...")

    if message.content.startswith("!MinecraftServerStop"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:

            # awscliでサーバ停止

            # 起動完了メッセージ
            await client.send_message(message.channel, "Minecraft Server 停止中（大嘘） ...")

    if message.content.startswith("!PixArkServerStart"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:

            # awscliでサーバ起動

            # 起動完了メッセージ
            await client.send_message(message.channel, "PixArk Server 起動中（大嘘） ...")

    if message.content.startswith("!PixArkServerStop"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:

            # awscliでサーバ停止

            # 起動完了メッセージ
            await client.send_message(message.channel, "PixArk Server 停止中（大嘘） ...")

client.run("")