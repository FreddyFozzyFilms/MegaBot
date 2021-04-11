import setup

from PIL import Image, ImageOps
from io import BytesIO
from keep_alive import keep_alive
import filecmp


@setup.client.command()
async def ascii(ctx, channel='Grey'):
    if not ctx.message.attachments:
        await ctx.send('must attach image')

    attachment = ctx.message.attachments[0]
    response = setup.requests.get(attachment.url)

    if 'image' in response.headers['content-type']:
        img = Image.open(BytesIO(response.content))

        # Create Black and white Image
        if channel == 'R':
            img = img.getchannel('R')
        elif channel == 'G':
            img = img.getchannel('G')
        elif channel == 'B':
            img = img.getchannel('B')
        elif channel == 'A':
            img = img.getchannel('A')
        else:
            img = ImageOps.grayscale(img)
        width, height = img.size

        factor = int ( setup.math.floor(width/29) )
        width = int (round(width / factor))
        height = int (round(height / factor))

        if width > 29:
            width = 29

        img = img.resize((width, height),resample=Image.BILINEAR)
        img.save("test2.png")

        width, height = img.size
        for i in range(height):
            line = []
            for j in range(width):
                pixel = img.getpixel((j, i))
                if pixel > 150:
                    pixel = " "*2 + "$" + " "*2
                elif pixel > 75:
                    pixel = " "*1 + "%" + " "*1
                else:
                    pixel = " "*2 + " , " + " "*2
                line.append(pixel)
            line = ''.join(line)
            await ctx.send(line)
    else:
        await ctx.send('must attach image')