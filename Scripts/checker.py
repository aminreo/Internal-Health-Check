import json
import requests
import datetime
from time import sleep


def main():
    with open('Data/Services.JSON','r', encoding='utf-8') as json_obj:
        json_file=json.load(json_obj)
        # print(log_file.read())
        running = True
        while running:
            log_file= open('Logs/checks.log','a', encoding='utf-8')
            for i in json_file:
                # print(i["url"])
                time=datetime.datetime.now()
                try:
                    r= requests.head(i["url"],timeout=3)
                    r_status= "UP" if r.status_code == 200 else "DOWN"
                except:
                    r_status="DOWN"
                if r_status=="DOWN":
                    print("------------Warning------------")
                result = f"[{time}] {i["name"]}: {r_status}"
                print(result)
                log_file.write(result+"\n")
                
            log_file.write(f"\n")
            log_file.close()
            sleep(5)
    return

if __name__=="__main__":
    main()