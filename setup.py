# -*- coding: utf-8 -*-
#!/bin/env python3
# Modified by @kenkanasw
# Please give me credits if you use any codes from here.


import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴   v1.2
	""")
banner()
print(gr+"[+] Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] Masukkan API ID : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] Masukkan Hash : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] Masukkan nomor telephon format internasional: "+re)
cpass.set('cred', 'phone', xphone)
setup = open('config.data', 'w')
cpass.write(setup)
setup.close()
print(gr+"[+] Setup complete!")
print(gr+"[+] Now you can run any tool!")
print(gr+"[+] Make sure to read README.md before using this tool.")
print(gr+"[+] https://github.com/Gagan2021/teleScraper/blob/master/README.md")
