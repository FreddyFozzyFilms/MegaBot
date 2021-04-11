import setup


@setup.client.command() # all strings in aliases invoke cammond
async def randlink(ctx):
    responses = ['https://stackoverflow.com/',
                'https://discord.com/',
                'https://www.boredbutton.com/',
                'https://htwins.net/scale2/',
                'https://www.youtube.com/ ',
                "https://en.wikipedia.org/wiki/Troglodyte",
                'https://www.twitch.tv/',
                'https://theuselessweb.com/',
                "Error/6"]
    await ctx.send(f'random link: {setup.random.choice(responses)}')



#async def addlink(ctx, *, message):
  #if message.content.lower().count('https://'):



    #await ctx.send(f'added link: {setup.message.content}')
    #await ctx.send(f'Question: {question}\nAnswer: {setup.random.choice(responses)}')
    #elif message.channel.send('no link')
    #message = ["addlink"]

