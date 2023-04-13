from distutils.command import upload
from telethon import TelegramClient, events 
from time import sleep
from typing import List
import json

api_id = 13679745
api_hash = "bbd314bbf977ec060d6b555670717daa"
phone_number = "+19292071901"
filename = "C:\\Extra\\Programs\\Telegram Bot\\Media Message Bot\\replied_users.json"
replied_users_id =[]
with open(filename, "r") as file:
    replied_users_id.extend(json.load(file))

message = ("Hola\n\n" 
"¿Te gustaría potenciar tu perfil de Instagram?\n\n"
"Puedo ayudarte a aumentar los Me gusta de los seguidores, etc.\n\n"
r"Nuestros servicios son 100% seguros y genuinos."
"\n\nLos seguidores de Instagram comienzan desde solo 3 dólares por 1000 seguidores\n\n "
"Si está interesado, envíeme un mensaje.\n\n"
"Nota: Se aceptan pagos a través de PayPal, tarjeta de crédito/débito y criptomonedas.\n\n"
"Que tenga un buen día")

client = TelegramClient("session5", api_id, api_hash)

group_id=(1184118791,1626608761,1565177729,1567046516,1754258877,1001412857329,1001685280773,1001534443266,1001595374063,872448107,981083241,607109685,1001778235717,920576207,1001869291778,1001847616329,1001562516291,1001441473075,743431833,1001770092513,1001457477857,1001335928674,1001157619504,1001572281677,1001543894063)

@client.on(events.NewMessage(chats=group_id))
async def handle_new_message(event):
    user_id = event.message.sender.id
    user_name = event.message.sender.first_name
    if user_id not in replied_users_id:
        await event.message.reply(message)
        with open(filename, "w") as file:
            json.dump(replied_users_id, file) 
        print(f"{user_id} {user_name}\n")
        print(f"{event.chat}\n")
        replied_users_id.append(user_id)
        print(f"{replied_users_id}")
        
        
        
while True:
    client.start(phone_number)
    client.run_until_disconnected()
    sleep(300)


        
 

        