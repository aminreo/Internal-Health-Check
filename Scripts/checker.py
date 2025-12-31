import json
import requests


def main():
    with open('Data/Services.JSON','r', encoding='utf-8') as json_obj:
        json_file=json.load(json_obj)
        for i in json_file:
            # print(i["url"])
            r= requests.head(i["url"])
            print(r.status_code)
    return

if __name__=="__main__":
    main()