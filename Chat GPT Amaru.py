from requests import get
import json, time
from os import system as sys
from random import randint
rd, lgn, gn, yh, lrd, be, pe, off = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;37m', '\033[01;31m', '\033[00;0m', '\033[01;35m','\033[00;0m'
cn = '\033[00;36m'
def clear():
    try:sys("clear")
    except:sys("cls")


w = input(f"""
{lrd}{lgn}{lrd}{lrd} Telegram : {yh}@AimFov  {lrd} Model : {yh}ChatGPT

{yh}Writen by : {lrd}Amaru

{off}[{lrd} 1 {off}]{lgn} asking questions

Enter : """)

def question():
    question = input(f"\n{off}[{lrd}+{off}]{lgn} Ask your question : {cn}")
    url = f"https://api2.haji-api.ir/gpt/gpt.php?text={question}"
    response = get(url)
    print (f"\n{gn}Your question has been answered\n{off}{off}")
    for char in json.loads(response.text)["result"]["answer"]:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print (f"\n\n{lgn}")

while True:
    if w == '1':
        question()
        Cl = input(f"\n{lrd}[{lgn} ? {lrd}]{lgn} Do you want to continue {off}[{gn} Y{off} / {lrd}N {off}] : {cn}")
        if Cl == 'y' or Cl == 'Y':
            clear()
        else:
        	break
    