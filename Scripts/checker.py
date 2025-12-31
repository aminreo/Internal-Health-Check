import json


def main():
    with open('Data/Services.JSON','r', encoding='utf-8') as json_obj:
        json_file=json.load(json_obj)
        for i in json_file:
            print(i["url"])
    return

if __name__=="__main__":
    main()