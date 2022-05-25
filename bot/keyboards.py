from telegram import ReplyKeyboardMarkup
from .api import get_categories,get_cat_id,get_products
main_markup = ReplyKeyboardMarkup(
    [['Kategoriyalar'],
    ['🛒Savatcha','⏱Buyurtmalar tarixi']],
    resize_keyboard=True
)

categories_markup = ReplyKeyboardMarkup(
    [
        [c['name']] for c in get_categories()
    ],
    resize_keyboard=True
)

def product_markup(category,page=1):
    return ReplyKeyboardMarkup(
                [
                    [p['id'] for p in get_products(get_cat_id(category),page)],
                    ['Kategoriyalar']

                ],
        resize_keyboard=True
    )

