from request_get import get_html, parse_html
import telebot

Url = "https://www.gismeteo.ru/weather-omsk-4578/now/"
bot = telebot.TeleBot('8030976704:AAHm8Uc-SfaGS38M5HagYrGSvwmw0_-744Y')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text)
    if (message.text).lower() == "погода":
        print(message)
        html = get_html(Url)
        soup = parse_html(html)
        soup = soup.find("temperature-value")
        bot.send_message(message.from_user.id, text=f"Погода сегодня в омске {soup['value']}")
        print(soup['value'])

bot.polling(none_stop=True, interval=0)