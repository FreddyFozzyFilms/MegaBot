import setup
from replit import db
import validators

def update_links(new_link):
  if "links" in db.keys():
    links = db["links"] # getting links from db
    if not new_link in links and validators.url(new_link):
      links.append(new_link) # changing links list
      db["links"] = links # updating the encouragmenet in the database
  else:
    links = [new_link]
    db["links"] = links

def delete_link(index):
  links = db["links"]
  if len(links) > index:
    del links[index]
    db["links"] = links

@setup.client.command()
async def randLink(ctx):
    await ctx.send(setup.random.choice(db["links"]))

@setup.client.command()
async def addLink(ctx,  *, link):
  update_links(link)
  await ctx.send(",".join(db["links"]))