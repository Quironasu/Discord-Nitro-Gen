import random
import string
import time
import os
import requests

# Función para generar códigos de Discord Nitro
def generate_nitro_code():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{code}"

# Función para guardar el código en el archivo
def save_code_to_file(code):
    with open("nitro.txt", "a") as file:
        file.write(code + "\n")

# Función para verificar si un código es válido
def check_nitro_code(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    return response.status_code == 200 and response.json().get('uses') == 0

# Borrar el contenido de nitro.txt al abrir el archivo nuevamente
if os.path.exists("nitro.txt"):
    os.remove("nitro.txt")

# Mensaje de inicio
print("""
░█████╗░██████╗░░█████╗░██████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝
██║░░╚═╝██████╔╝███████║██████╔╝██║░░██║░╚███╔╝░
██║░░██╗██╔══██╗██╔══██║██╔══██╗██║░░██║░██╔██╗░
╚█████╔╝██║░░██║██║░░██║██║░░██║╚█████╔╝██╔╝╚██╗
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

Generando códigos de Discord Nitro...""")

# Esperar 3 segundos antes de comenzar la generación
time.sleep(3)

# Generar y mostrar los códigos
try:
    while True:
        nitro_code = generate_nitro_code()  # Generar un código
        print(nitro_code)  # Mostrar el código en la consola
        save_code_to_file(nitro_code)      # Guardar el código en el archivo

        # Verificar si el código es válido antes de enviarlo a la webhook
        if check_nitro_code(nitro_code.split('/')[-1]):
            webhook_url = "https://discord.com/api/webhooks/1131380433695817868/DoCUF4cSkxxWABowtFEIbDjdLjDVN0JeW24l7_eBx5iYIDcfiB5CmInNi3qIqt1jrup0"
            data = {
                "content": nitro_code
            }
            requests.post(webhook_url, data=data)

        time.sleep(0.02)  # Esperar un breve tiempo antes de generar el siguiente código

except KeyboardInterrupt:
    print("\nGeneración de códigos detenida.")
