import random
import string
import time
import os
import requests

def generate_nitro_code():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f"https://discord.gift/{code}"

def save_code_to_file(code):
    with open("nitro.txt", "a") as file:
        file.write(code + "\n")

def check_nitro_code(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    return response.status_code == 200 and response.json().get('uses') == 0

if os.path.exists("nitro.txt"):
    os.remove("nitro.txt")

print("""
░█████╗░██████╗░░█████╗░██████╗░░█████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝
██║░░╚═╝██████╔╝███████║██████╔╝██║░░██║░╚███╔╝░
██║░░██╗██╔══██╗██╔══██║██╔══██╗██║░░██║░██╔██╗░
╚█████╔╝██║░░██║██║░░██║██║░░██║╚█████╔╝██╔╝╚██╗
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

Generating Discord Nitro codes...""")

time.sleep(3)

try:
    while True:
        nitro_code = generate_nitro_code() 
        print(nitro_code)  
        save_code_to_file(nitro_code)

        if check_nitro_code(nitro_code.split('/')[-1]):
            webhook_url = "Your Webhook URL here"
            data = {
                "content": nitro_code
            }
            requests.post(webhook_url, data=data)

        time.sleep(0.02) 

except KeyboardInterrupt:
    print("\nCode generation stopped.")
