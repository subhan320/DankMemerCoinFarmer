import discord, time, os
client = discord.Client()

@client.event
async def on_ready():
    print("Logged on as {0}!".format(client.user.name))

@client.event
async def on_connect():
    channel = client.get_channel(752051281950015570)
    while True:
        await channel.send("pls hunt")
        time.sleep(5)
        await channel.send("pls search")
        time.sleep(5)
        await channel.send("pls fish")
        time.sleep(9)
        await channel.send("pls beg")
        time.sleep(20)
        await channel.send("pls pm")
        time.sleep(5)
        await channel.send("pls beg")
        time.sleep(5)
        await channel.send("pls dep all")
        time.sleep(15)
            
token = os.getenv('OTUwNzYwODA2NTU4MTA1NjIw.Yidncw.ZhBsOydzRX4PSjl-cC9Ik3ZgVw0')
client.run(token, bot = False)
