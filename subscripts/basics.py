import setup
@setup.client.event
async def on_ready():
    print('bot is ready')

@setup.client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(setup.client.latency * 1000)} ms')

@setup.client.command(aliases=['8ball']) # all strings in aliases invoke cammond
async def _8ball(ctx, *, question):
    responses = ['As I see it, yes.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                "Don't count on it.",
                'It is certain.',
                'It is decidedly so.',
                "I don't see why not"]
    await ctx.send(f'Question: {question}\nAnswer: {setup.random.choice(responses)}')
