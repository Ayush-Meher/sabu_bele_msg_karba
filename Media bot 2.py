from telethon import TelegramClient, events 
from time import sleep
import os


try:
    os.remove("C:\\Users\\Spider\\Downloads\\TelegramPythonBot\\session.session")
    os.remove("C:\\Users\\Spider\Downloads\\TelegramPythonBot\\session.session-journal")
    
except:
    pass


api_id = 12517519
api_hash = "995de932443c9fb27364ea6790bc22af"

client = TelegramClient("session", api_id, api_hash)
@client.on(events.NewMessage(outgoing=True, pattern= "Holaa!"))

async def greeting(event):
   
    i=1
    while True:
        
    
    
        sleep(10)
        
        chat = await event.get_chat()
        await client.send_file(chat, "C:\\Users\\Spider\\Downloads\\demo.mp4", caption= 
        "Hola\n\n" 

        "¿Te gustaría potenciar tu perfil de Instagram?\n\n"

        "Puedo ayudarte a aumentar los Me gusta de los seguidores, etc.\n\n"

        r"Nuestros servicios son 100% seguros y genuinos."

        "\n\nLos seguidores de Instagram comienzan desde solo 2 dólares por 1000 seguidores\n\n "

        "Si está interesado, envíeme un mensaje.\n\n"

        "Nota: Se aceptan pagos a través de PayPal, tarjeta de crédito/débito y criptomonedas.")
        
        print("Message sent in group 1", i)
        i+=1
   
   
   
   
   
@client.on(events.NewMessage(outgoing=True, pattern= "Holaaa!!"))

async def greeting2(event):
    i=1
    while True:
        
    
    
        sleep(10)
        
        chat = await event.get_chat()
        await client.send_file(chat, "C:\\Users\\Spider\\Downloads\\demo.mp4", caption= 
        "Hola\n\n" 

        "¿Te gustaría potenciar tu perfil de Instagram?\n\n"

        "Puedo ayudarte a aumentar los Me gusta de los seguidores, etc.\n\n"

        r"Nuestros servicios son 100% seguros y genuinos."

        "\n\nLos seguidores de Instagram comienzan desde solo 2 dólares por 1000 seguidores\n\n "

        "Si está interesado, envíeme un mensaje.\n\n"

        "Nota: Se aceptan pagos a través de PayPal, tarjeta de crédito/débito y criptomonedas.")
        
        print("Message sent in group 2", i)
        i+=1     
        
        
        
        
@client.on(events.NewMessage(outgoing=True, pattern= "Holaaaa!!!"))

async def greeting2(event):
    i=1
    while True:
        
    
    
        sleep(20)
        
        chat = await event.get_chat()
        await client.send_file(chat, "C:\\Users\\Spider\\Downloads\\demo.mp4", caption= 
        "Hola\n\n" 

        "¿Te gustaría potenciar tu perfil de Instagram?\n\n"

        "Puedo ayudarte a aumentar los Me gusta de los seguidores, etc.\n\n"

        r"Nuestros servicios son 100% seguros y genuinos."

        "\n\nLos seguidores de Instagram comienzan desde solo 2 dólares por 1000 seguidores\n\n "

        "Si está interesado, envíeme un mensaje.\n\n"

        "Nota: Se aceptan pagos a través de PayPal, tarjeta de crédito/débito y criptomonedas.")
        
        print("Message sent in group 3", i)
        i+=1     
        
        
    
    

client.start()
client.run_until_disconnected()