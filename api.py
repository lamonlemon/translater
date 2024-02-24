import requests

def get_translate(text,source,target):
    client_id = "###"
    client_secret = "###"

    data = {'text' : text,
            'source' : source,
            'target': target}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:" , rescode)


print("Languages: Korean (ko), English (en), Japanese (ja), Simplified Chinese (zh-CN), Traditional Chinese (zh-TW), Spanish (es), French (fr), Russian (ru), Vietnamese ( vi), Thai (th), Indonesian (id), German (de), Italian (it)")
source = input('Enter original language-->  ')
target = input('Enter the language you want to translate-->  ')
get = input("Enter sentence to translate-->  ")
trans = get_translate(get,source,target)
print(trans)