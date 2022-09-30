from distutils.command import upload
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
    

    vid = await client.upload_file("C:\\Users\\Spider\\Downloads\\demo.mp4")
    print("Upload sucessful")

   
    i=1
    while True:
        
    
    
        sleep(60)
        
        chat = await event.get_chat()
        try:
            await client.send_file(chat, vid, caption= 
            "Hola\n\n" 

            "¿Te gustaría potenciar tu perfil de Instagram?\n\n"

            "Puedo ayudarte a aumentar los Me gusta de los seguidores, etc.\n\n"

            r"Nuestros servicios son 100% seguros y genuinos."

            "\n\nLos seguidores de Instagram comienzan desde solo 2 dólares por 1000 seguidores\n\n "

            "Si está interesado, envíeme un mensaje.\n\n"

            "Nota: Se aceptan pagos a través de PayPal, tarjeta de crédito/débito y criptomonedas.")
            
            
        except:
            sleep(12)
            await client.send_message(chat,
                                      "Hola\n\n" 

            "¿Te gustaría potenciar tu perfil de Instagram?\n\n"

            "Puedo ayudarte a aumentar los Me gusta de los seguidores, etc.\n\n"

            r"Nuestros servicios son 100% seguros y genuinos."

            "\n\nLos seguidores de Instagram comienzan desde solo 2 dólares por 1000 seguidores\n\n "

            "Si está interesado, envíeme un mensaje.\n\n"

            "Nota: Se aceptan pagos a través de PayPal, tarjeta de crédito/débito y criptomonedas."
                                      
                                      )
        
        try:
        
            print("No. of message sent in ",  str(chat.title()) , i)
            
        except:
            print("No. of message sent in group: ", i)
        
        i+=1
   
        print(chat)
   
   
   
# @client.on(events.NewMessage(incoming=True, ))

# async def greeting2(event):
#     chat = await event.get_chat()
#     if event.is_group==True:
#         pass
#     else:
#         print(event.message)
        
#         if event.message_id()== 1 or 2:

        
#           await client.send_message(chat, "Hola")
#           await client.send_message(chat, "¿Te gustaría potenciar tu perfil de Instagram?" )
#           await client.send_message(chat, "Puedo ayudarte a aumentar los me gusta de tus seguidores, etc.")    
#         else:
#             pass
        
        
    
    

client.start()
client.run_until_disconnected()