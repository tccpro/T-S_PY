from telegram import  InlineKeyboardButton,InlineKeyboardMarkup

from bot.api import get_products,get_cat_id

def products_keyboard(category,page=1):
    datas = get_products(get_cat_id(category),page)
    keys = [str(data['id']) for data in datas]
    return InlineKeyboardMarkup([
                [InlineKeyboardButton(text="Oldingi",callback_data='previous'),InlineKeyboardButton(text=f"{page}",callback_data=f'{page}'),InlineKeyboardButton(text="Keyingi",callback_data='next')]

    ]),keys

