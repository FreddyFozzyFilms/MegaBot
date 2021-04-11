import setup

keywords = ["pipe down", "fred sucks", "TEST DELETE"]


@setup.client.event
async def on_message(message):
  # makes sure the bot doesnt respond to itself
  #but why that would be fun and create an endless loop of spam
  if message.author.id == setup.client.user.id:
        return
  
  for i in keywords:
    if i in message.content:
      await message.channel.send("This message is offensive to the african jewish community")
      await message.delete()
  await setup.client.process_commands(message)

