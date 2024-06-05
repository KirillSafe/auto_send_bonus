""" Хочу вам напомнить что использование self-bot'ов (коим этот скрипт и является) может привести к бану за нарушение ToS Discord, используйте на свой страх и риск"""
""" Хочу вам напомнить что использование self-bot'ов (коим этот скрипт и является) может привести к бану за нарушение ToS Discord, используйте на свой страх и риск"""
""" Хочу вам напомнить что использование self-bot'ов (коим этот скрипт и является) может привести к бану за нарушение ToS Discord, используйте на свой страх и риск"""
import requests, yaml, time
bonus_id = 715169589931278426
number = 0
class Discord:
    def __init__(self, t):
        self.base = "https://discord.com/api/v9"
        self.auth = { 'authorization': t }
        
    def getMe(self):
        u = requests.get(self.base + "/users/@me", headers=self.auth).json()
        return u
        
    def sendMessage(self, cid, txt):    
        u = requests.post(self.base + "/channels/" + str(cid) + "/messages", headers=self.auth, json={ 'content': txt }).json()
        return u
def start():
    print(""" Хочу вам напомнить что использование self-bot'ов (коим этот скрипт и является) может привести к бану за нарушение ToS Discord, используйте на свой страх и риск""")
    print('y\\n')
    text = input("Вы уверены что хотите включить данного бота?  ")
    return text
def main():
    global number
    with open('config.yaml') as cfg:
        conf = yaml.load(cfg, Loader=yaml.FullLoader) 
    token = conf['token']
    delay = 5
    if isinstance(token, list): 
        token = token[0]  
    print(token)
    print()
    while True:
            try:        
                        Bot = Discord(token)
                        me = Bot.getMe()['username']
                        if number == 0: print(me + " Начинает работу")
                        send = Bot.sendMessage(bonus_id, "!bonus")
                        number += 1
                        print(me + " Сделал bonus " + str(number) + " раз")
                        print("Следущий бонус через 11 минут.")
                        time.sleep(660)

            except Exception as e:
                print("[Error]  Неправильный токен")
                print("[Error]  Бот выключился во избежание ошибок")
                print(f"[Error] {e}")
                exit()
if __name__ == '__main__':
    text = start()
    if text == "y":
        try:
            main()
        except Exception as err:
            print(f"{type(err).__name__} : {err}")
    elif text == "n":
        print("Бот остановлен")
        exit()
    else:
        print("не понял, повтори?")
        start()
        