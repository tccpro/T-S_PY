from PIL import Image

import requests
import shutil
import os

def get_categories():
    response = requests.get('http://127.0.0.1:8000/api/category/')
    return response.json()

def get_products(cat,page=1,per_page = 6):
    response = requests.get(
        f'http://127.0.0.1:8000/api/product/?category={cat}&page={page}&per_page={per_page}'
    )
    response_data = response.json()
    for data in response_data:
        img_url = data.get('image')
        if img_url:
            file_format = img_url.split('.')[-1]
            path = f"downloads/images/"
            file_name = f"img.{data['id']}.{file_format}"
            r = requests.get(img_url,stream=True)
            if r.status_code == 200 and not(file_name in os.listdir('downloads/images')):
                print(file_name,'download...')
                with open(path+file_name,'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw,f)
        else:
            file_name=f"img.{data['id']}.jpg"
            img = Image.open('downloads/default_shop.jpg')
            img.save('downloads/images/'+file_name)
    return response_data

def get_cat_id(name):
    res:dict = {}
    for c in get_categories():
        res[c['name']]=c['id']
    return res[name]

def bot_login(phone_number,password):
    response = requests.post(
        'http://127.0.0.1:8000/api/login/',
        {
            'phone_number':phone_number,
            'password':password
        }
    )
    return response.status_code,response.json()

def get_my_cart(token):
    response = requests.get(
        'http://127.0.0.1:8000/api/cart/',
        headers={
            'Authorization': f'Token {token}'
        }
    )
    return response.json()['items']


def get_my_orders(token):
    response = requests.get(
        'http://127.0.0.1:8000/api/customer_orders/',
        headers={
            'Authorization': f'Token {token}'
        }
    )
    return response.json()['orders']
# print(get_my_cart('005c50b8ff3fec38c3af97261d089675e4d73b19be3696e60184
#                   e635947deb7e'))