from telethon import TelegramClient, events 
from time import sleep
import os

try:
    os.remove("C:\\Users\\Spider\\Downloads\\TelegramPythonBot\\session.session")
    os.remove("C:\\Users\\Spider\Downloads\\TelegramPythonBot\\session.session-journal")
    
except:
    pass


print("Enter your API ID")
api_id = int(input())
print("Enter your API Hash")
api_hash = input()


client = TelegramClient("session", api_id, api_hash)
try:
    client.start()
except:
    print("Delete the session.session file and restart the application")
x= input("Enter the message to trigger the bot\n")
@client.on(events.NewMessage(outgoing=True, pattern= (x)))

async def greeting(event):
    i=1
    print("Enter the message")
    msg= open("C:\\Users\\Spider\\Downloads\\TelegramPythonBot\\msg.txt")
    print("Enter the delay you want (in seconds)")
    sec= int(input())
    
    while True:
        
    
    
        sleep(sec)
        
        chat = await event.get_chat()
        try:
            await client.send_message(chat, msg)
            
            print("Message sent", i)
            i+=1
        except:
            return print("Unable to send Message, Please Try Restarting The Program")
        
    
    


client.run_until_disconnected()
