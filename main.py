import telebot
import requests

API_KEY = 'ebce4eda08c32192d4c1dda97eb7b327'
bot = telebot.TeleBot('7418962566:AAGwke5Uj7CgZ6WPSSPsu4LmbC2a83MX1B8')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Напиши название города, чтобы получить погоду.")

@bot.message_handler(func=lambda message: True)
def get_weather(message):
    city = message.text
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temperature = main['temp']
        
        weather_info = f"Погода в {city}:\n" \
                       f"Температура: {temperature}°C" \
                       f"Описание: {weather_desc.capitalize()}"
        
        bot.reply_to(message, weather_info)
    else:
        bot.reply_to(message, "Город не найден. Пожалуйста, проверьте название.")

if __name__ == '__main__':
    bot.polling()
