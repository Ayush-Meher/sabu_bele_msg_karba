from distutils.command import upload
from telethon import TelegramClient, events 
from time import sleep
import os
import json
from typing import List

api_id = 13679745
api_hash = "bbd314bbf977ec060d6b555670717daa"
phone_number = "+19292071901"
chat_id = 1184118791,1626608761,1565177729,1567046516,1754258877,1001412857329,1001685280773,1001534443266,1001595374063,1001457477857,1001335928674,1001157619504,1001572281677,1001543894063

filename = 'replied_users.txt'



replied_users = set()
try:
    with open(filename) as file:
        for line in file:
            replied_users.add(int(line.strip()))
except:
    pass

client = TelegramClient("session", api_id, api_hash)
@client.on(events.NewMessage(chats=chat_id))
async def handle_new_message(event):
    
    
    user_id = event.message.sender.id
    if user_id not in replied_users:
        vid = await client.upload_file("C:\\Extra\\Programs\\Telegram Bot\\Media Message Bot\\Vid.mp4")
        print("Upload Successful")

        try:
            await event.respond(vid, caption= 
            "Hola\n\n" 

            "¿Te gustaría potenciar tu perfil de Instagram?\n\n"

            "Puedo ayudarte a aumentar los Me gusta de los seguidores, etc.\n\n"

            r"Nuestros servicios son 100% seguros y genuinos."

            "\n\nLos seguidores de Instagram comienzan desde solo 2 dólares por 1000 seguidores\n\n "

            "Si está interesado, envíeme un mensaje.\n\n"

            "Nota: Se aceptan pagos a través de PayPal, tarjeta de crédito/débito y criptomonedas.")
                
                
        except:
            await event.message.reply(
                                    "Hola\n\n" 

            "¿Te gustaría potenciar tu perfil de Instagram?\n\n"

            "Puedo ayudarte a aumentar los Me gusta de los seguidores, etc.\n\n"

            r"Nuestros servicios son 100% seguros y genuinos."

            "\n\nLos seguidores de Instagram comienzan desde solo 2 dólares por 1000 seguidores\n\n "

            "Si está interesado, envíeme un mensaje.\n\n"

            "Nota: Se aceptan pagos a través de PayPal, tarjeta de crédito/débito y criptomonedas."
                                        
                                        )
                
        
        print(f"{user_id}")
        
            
        
    
        print(event.chat)
        
            
        
        
    
    

client.start(phone_number)
client.run_until_disconnected()