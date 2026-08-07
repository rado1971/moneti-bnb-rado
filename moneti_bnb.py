Python
import json
iport datetime
print("Монети БНБ -Радо")
print("проверка на юбилейни монети")
Python
today=datetime.date.today()
print("Днес е:",today)
Python
with open("config.json","r")as file:config=json.load(file)
print("Имейл за известия:",config["email]
Python
moneti=["Няма нови монети"]
print("Следене монети:") for m in moneti:print("-",m)
PPython
last_check=today
print("Последна проверка:",last_check)
Phyton
def proveri_moneti():
print("проверявам нови емисии на БНБ...")
print("Няма открити нови монети.')
proveri_moneti()
history={"last_check:str(today)"status":"Проверката е извършена"}prin(history)
Phyton import requests

def proveri_bnb():url="https://www.bnb.bg"odgovor=requests.get(url)
if odgovor.status_code==200:print("Връзката с БНБ работи.")
se:print("Проблем със захранването .")i_bnb()
Python def tarsi_moneti():
    Puthon if "монети"in otgovor.text.lower():
        print(Намерена е информация за монети в сайтана БНБ.")
Phyton else:
        print("Няма намерени новинини за монети.)

Phyton tarsi_moneti()
Phyton print ("Проверката приключи успешно.")
Phyton print ("Чакаме нови емисии на БНБ.")
Phyton with open("moneti_seen.json,"r") as file:
    Phyton seen=json.load(file)
Phyton print("Запомнени монети",seen)
Phyton if nova_moneta="Няма нова монета"
phyton if nova_moneta not in seen:
    Phyton print("Нова монета ;",nova_moneta)
    Phyton seen.append(nova_moneta)
Phyton with open("moneti_seen.json","w") as file:
        json.dump(seen,file)
Phyton with open("bnb_config.json","r")
    Phyton bnb=json.load(file)
Phyton print("Страница на БНБ:",bnb["url"]    
Phyton stranica=requests.get(bnb["url"])
Phyton tekst=stranica.text.lower()
Phyton print("Получени дснни от БНБ.")
Phyton if "емисия"in tekst:
    Phyton print("Открита е нова емисия!")
Phyton else:
    Phyton print("Няма нова емисия")
      
      
