# callback methoods------------------------------------------------------
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from redis_connection import redis_connection as redconn
import json
from bot.inline_keyboards import products_keyboard
from bot.keyboards import main_markup, categories_markup,product_markup
from bot.make_image import get_gr_photo
from bot.api import bot_login, get_my_cart, get_my_orders


def start(update:Update, context: CallbackContext):
    redconn.delete(f'{update.message.from_user.id}')
    user_json = redconn.get(f'{update.message.from_user.id}')
    if user_json:
        user_data = json.loads(user_json)
        token = user_data.get('token',None)
        if token:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Salom bu eshopning boti!!!",
                reply_markup=main_markup
            )
        # else:

    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Salom bu eshopning boti!\nOnline do'konimizning imkoniyatlaridan to'liq foydalanish uchun tizimga kiring!\nTelefon raqamingizni kiriting:",
            reply_markup=ReplyKeyboardRemove()
        )

def text_message(update:Update, context: CallbackContext):
    message = update.message.text
    try:
        user_json = redconn.get(f'{update.message.from_user.id}')
        if user_json:
            user_data = json.loads(user_json)
            token = user_data.get('token',None)
            phone_number = user_data.get('phone_number',None)
            if token:
                if message == 'Kategoriyalar':
                    context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        text=f"Marhamat kerakli kategoriyani tanlang",
                        reply_markup=categories_markup
                    )
                elif message == "Ortga":
                    context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        text="Bosh sahifa",
                        reply_markup=main_markup
                    )
                elif message == "🛒Savatcha":
                    for item in get_my_cart(token):
                        context.bot.send_message(
                            chat_id=update.effective_chat.id,
                            text=f"Buyurtmaning tartib raqami:   {item['order_id']}\nBuyurtma tarkibining raqami:    {item['item_id']}\nBuyurtma qilingan mahsulot:    {item['product']}\nBuyurtma qilingan mahsulot soni:   {item['quantity']}\nBuyurtma qilingan mahsulot umumiy narxi:    ${item['price']}",
                            reply_markup=ReplyKeyboardRemove()
                        )
                elif message == "⏱Buyurtmalar tarixi":
                    for item in get_my_orders(token):
                        context.bot.send_message(
                            chat_id=update.effective_chat.id,
                            text=f"Buyurtmaning tartib raqami:   {item['order_id']}\nBuyurtma yaratilgan sana:    {item['order_date']}\nBuyurtma yetkazilgan sana:    {item['expired_date']}\nBuyurtma qilingan mahsulotlar soni:   {item['item_count']}\nBuyurtma qilingan mahsulot umumiy narxi:    ${item['price']}\nBuyurtma statusi:   {item['status']}",
                            reply_markup=ReplyKeyboardRemove()
                        )

                else:
                    p_keyboard, keys = products_keyboard(message, page=1)
                    context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        text=message,
                        reply_markup=product_markup(message, page=1)

                    )
                    context.bot.send_photo(
                        chat_id=update.effective_chat.id,
                        photo=open(get_gr_photo(keys), 'rb'),
                        caption="Kerakli mahsulotni raqami bo'yicha tanlang:",
                        reply_markup=p_keyboard
                    )
            elif phone_number:

                status_code,response_json = bot_login(phone_number=phone_number,password=message)
                if status_code==200:
                    redconn.mset({f'{update.message.from_user.id}': json.dumps({
                        'token': response_json['token']
                    })})
                    context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        text="Tizimga muvoffaqiyatli kirdingiz:",
                        reply_markup=main_markup
                    )
                else:
                    context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        text="password:"
                    )
            else:
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=f"Online do'konimizning imkoniyatlaridan to'liq foydalanish uchun tizimga kiring!\nTelefon raqamingizni kiriting:",
                )
        else:
            redconn.mset({f'{update.message.from_user.id}': json.dumps({
                'phone_number': message
            })})
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"password:"
            )

    except Exception as error:
        print('error:',error)



def photo_message(update:Update,context:CallbackContext):
    context.bot.send_photo(chat_id=update.effective_chat.id,photo=open('img.png','rb'))
# end callback methoods------------------------------------------------------
