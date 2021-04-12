import setup
@setup.client.event

# sample event
@setup.client.event
async def on_ready():
    print('bot is ready')

# sample command
@setup.client.command()
async def sampleCommand(ctx):
    await ctx.send("Sample message")