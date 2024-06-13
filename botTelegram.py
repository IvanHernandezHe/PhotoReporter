#PhotoReporter_Copryserr_Bot
import telebot
TOKEN = '7375526041:AAHjABWlwdK00t8C3dc6pgPvUSGYJ4MTaH8'
import telebot
from telebot import types


bot = telebot.TeleBot(TOKEN)

images = []

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    start_button = types.KeyboardButton('Iniciar sesión de envío de imágenes')
    end_button = types.KeyboardButton('Finalizar sesión de envío de imágenes')
    markup.add(start_button, end_button)
    bot.reply_to(message, 'Bienvenido al reporteador. Usa los botones para iniciar y finalizar la sesión de envío de imágenes.', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Iniciar sesión de envío de imágenes')
def start_session(message):
    bot.reply_to(message, 'Sesión de envío de imágenes iniciada. Puedes comenzar a enviar tus imágenes.')

@bot.message_handler(func=lambda message: message.text == 'Finalizar sesión de envío de imágenes')
def end_session(message):
    bot.reply_to(message, 'Sesión de envío de imágenes finalizada. Procesando imágenes...')
    process_images(message.chat.id)
    bot.reply_to(message, 'Procesamiento de imágenes completado.')

@bot.message_handler(content_types=['photo'])
def handle_image(message):
    if message.photo:
        file_info = bot.get_file(message.photo[-1].file_id)
        file = bot.download_file(file_info.file_path)
        images.append(file)
        bot.reply_to(message, 'Imagen recibida.')

def process_images(chat_id):
    # Aquí puedes agregar el código para procesar las imágenes almacenadas en la lista 'images'.
    # Por ejemplo, podrías guardarlas en el disco, analizarlas, etc.
    for idx, image in enumerate(images):
        with open(f'image_{idx}.jpg', 'wb') as img_file:
            img_file.write(image)
    bot.send_message(chat_id, 'Las imágenes han sido procesadas y guardadas.')

if __name__ == "__main__":
    bot.polling(none_stop=True)
