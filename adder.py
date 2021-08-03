#!/bin/env python3
# (c) @kenkanasw
# Please give me credits if you use any codes from here.


print ("\033[1;92m")
print ("░█▀█░█▀▄░█▀▄░█▀▀░█▀▄")
print ("░█▀█░█░█░█░█░█▀▀░█▀▄")
print ("░▀░▀░▀▀░░▀▀░░▀▀▀░▀░▀")
print ("")
print ("      by \033[1;95m@kenkanasw")
print ("\033[1;92m")
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time
import random

api_id =   3913940 #Enter Your 7 Digit Telegram API ID.
api_hash = '9367a1c841e8bafb8cde158f809be37d'   #Enter Yor 32 Character API Hash
phone = '+919719241709'   #Enter Your Mobilr Number With Country Code.
client = TelegramClient(phone, api_id, api_hash)
async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Percobaan hallo !!!!!')


SLEEP_TIME_1 = 100
SLEEP_TIME_2 = 100
with client:
    client.loop.run_until_complete(main())
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('40779'))

users = []
with open(r"members.csv", encoding='UTF-8') as f:  #Enter your file name
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

print('Silahkan pilih group yang mau di tambahkan membernya: ')
i = 0
for group in groups:
    print(str(i) + '- ' + group.title)
    i += 1

g_index = input("Masukkan nomor: ")
target_group = groups[int(g_index)]

target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

mode = int(input("Pilih 1 untuk menambahkan lewat username atau 2 untuk menambahkan lewat ID: "))

n = 0

for user in users:
    n += 1
    if n % 80 == 0:
        time.sleep(60)
    try:
        print("Menambahkan {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("Mode yang di pilih tidak valid, Silahkan coba lagi.")
        client(InviteToChannelRequest(target_group_entity, [user_to_add]))
        print("Menunggu 60-180 Seconds ...")
        time.sleep(random.randrange(0, 5))
    except PeerFloodError:
        print(" Mendapatkan Kesalahan Banjir dari telegram. Skrip berhenti sekarang. Silakan coba lagi setelah beberapa saat.")
        print("Waiting {} seconds".format(SLEEP_TIME_2))
        time.sleep(SLEEP_TIME_2)
    except UserPrivacyRestrictedError:
        print("Pengaturan privasi pengguna tidak mengizinkan Anda melakukan ini. Melewatkan ...")
        print("Menunggu 5 Seconds ...")
        time.sleep(random.randrange(0, 5))
    except:
        traceback.print_exc()
        print("Kesalahan yang tidak terduga! ")
        continue
