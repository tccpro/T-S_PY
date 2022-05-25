import requests

def send_sms(phone,text):
    url="http://notify.eskiz.uz/api/message/sms/send"

    payload={
        'mobile_phone':phone,
        'message':text,
        'from':'4546',
        'callback_url':'http://0000.uz/test.php'
    }
    files=[

    ]
    headers={
        'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9ub3RpZnkuZXNraXoudXpcL2FwaVwvYXV0aFwvbG9naW4iLCJpYXQiOjE2NDY2MzM2OTYsImV4cCI6MTY0OTIyNTY5NiwibmJmIjoxNjQ2NjMzNjk2LCJqdGkiOiJTQUdBNWxUQXhuZVd4UzQ1Iiwic3ViIjo1LCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.Ev2MlkfEK_CekvXf9XBNjZRZ8RpaSjQFl4ltCUiSX4A'
    }

    response = requests.request("POST",url,headers=headers,data=payload,files=files)
    print(response.text)

