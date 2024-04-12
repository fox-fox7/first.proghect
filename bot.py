
import telebot
YsngmanBot= telebot.TeleBot('AAEYifKRZRFS8-AUxRqwlyPsKBAuX7Nhfgs')

from telebot import types

@YsngmanBot.message_handler(commands=['start'])
def startBot(message):
  first_mess = f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, привет!\nХочешь расскажу немного о нашей компании?"
  markup = types.InlineKeyboardMarkup()
  button_yes = types.InlineKeyboardButton(text = 'Да', callback_data='yes')
  markup.add(button_yes)
  YsngmanBot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@YsngmanBot.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        second_mess = "Мы облачная платформа для разработчиков и бизнеса. Более детально можешь ознакомиться с нами на нашем сайте!"
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://timeweb.cloud/"))
        YsngmanBot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        YsngmanBot.answer_callback_query(function_call.id)
          
YsngmanBot.infinity_polling()