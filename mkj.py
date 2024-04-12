import requests
import telebot

def openAI(prompt):
    response =requests.post(
        'https://api.openai.com/v1/comp;etions',
        headers={'Authorizathion':f'Bearer{"API ключ open.ai"}'},
        json={'model':'НУЖНАЯ МОДЕЛЬ chat gpt',
              'prompt':prompt,'temperature':0.4,'max_token':300}
    )

    result=response.json()
    final_result=''.join(choice['text'] for choice in result['choices'])
    return final_result

bot=telebot.TeleBot('AAEYifKRZRFS8-AUxRqwlyPsKBAuX7Nhfgs')

@bot.message_handler()
def req(message):
    res = openAI(message.text)
    bot.send_message(message.chat.id, res)

bot.polling()