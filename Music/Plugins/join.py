from pyrogram import filters, Client
from pyrogram.types import Message
from Music.MusicUtilities.tgcallsrun import ASS_ACC as USER

@Client.on_message(filters.private & filters.incoming & filters.command("join"))
async def userbotjoin(_, message: Message):
    lol = await message.reply_text("**Processing...**")
    print("join request")
    if len(message.command) == 1:
        try:
           await lol.edit("**Give a invite link too !**")
        except:
          return
    elif len(message.command) == 2:      
        try:
           await lol.edit("Checking invite link...")
           await asyncio.sleep(2)
           query = message.text.split(None, 1)[1]
           query = str(query)
           
           if query.startswith("http://t.me/+"):
              query = query.replace("http://t.me/+","https://t.me/joinchat/")
              pass
           elif query.startswith("https://t.me/+"):
              query = query.replace("https://t.me/+","https://t.me/joinchat/")
              pass
           elif query.startswith("t.me/+"):
              query = query.replace("t.me/+","https://t.me/joinchat/")
              pass
           elif query.startswith("telegram.me/+"):
              query = query.replace("telegram.me/+","https://t.me/joinchat/")
              pass
           elif query.startswith("-1"):
              return await lol.edit(f"Use /play command in chat to invite userbot to public chats")
           elif query.startswith("http://t.me/"):
              query = query.replace("http://t.me/","https://t.me/joinchat/")
              return await lol.edit(f"Use /play command in chat to invite userbot to public chats")
           elif query.startswith("https://"):
              query = query.replace("https://t.me/","https://t.me/joinchat/")
              return await lol.edit(f"Use /play command in chat to invite userbot to public chats")
           elif query.startswith("t.me/"):
              query = query.replace("t.me/","https://t.me/joinchat/")
              return await lol.edit(f"Use /play command in chat to invite userbot to public chats")
           elif query.startswith("telegram.me/"):
              query = query.replace("telegram.me/","https://t.me/joinchat/")
              return await lol.edit(f"Use /play command in chat to invite userbot to public chats")            
           elif query.startswith("@"): 
              return await lol.edit(f"Use /play command in chat to invite userbot to public chats")
           else:
              return await lol.edit(f"The link `{query}` is invalid..! Check again.")
           try:
              await lol.edit("Assiatant joining to your chat...")
           except:
              pass
           try:
              await USER.join_chat(query)
              await USER.send_message(query, "I joined here as your request")
              await lol.edit("Assistant successfully joined your chat")
           except UserAlreadyParticipant:
              await lol.edit("Assistant already in your chat")
              pass   
           except Exception as e:
              return await lol.edit(f"An error occured while joining your chat.\n\nReasons: {e}")
           except:
              return await lol.edit(f"An error occured while joining your chat")   
                    
           return await lol.edit("Unknown error occured")
        except:
          return
    else:
       return
