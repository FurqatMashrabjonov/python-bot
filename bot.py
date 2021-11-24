
from functions import (fromHextoDec, fromBintoDec, fromHextoBin, fromDectoBin, fromDectoHex, fromBintoHex, fromRimtoDec, fromDectoRim)

import logging
from aiogram import Bot, Dispatcher, executor, types
import datetime
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

API_TOKEN = '2084331966:AAFi4UzSvFk9jfErr4jDVe31UucPPAsYqaY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


buttons1 = KeyboardButton("Sizning nomeringiz ?", request_contact=True)
buttons2 = KeyboardButton("Joylashgan joyingiz?", request_location=True)
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(buttons1, buttons2)

@dp.message_handler(commands='info')
async def you_info(message:types.Message):
    await message.reply("Siz haqingizdagi ma'lumotlar. ", reply_markup=keyboard1)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):

   print('iwlayaptiiiiiiiiiiiiiiiiiii')
    """

    This handler will be called when user sends `/start` or  command
    """
    id = {
        'id': message['from']['id']
    }

    with open('user_id.txt','a') as user_id:
        user_id.write(str(id['id'])+ " \n")

    user ={
        'id': message['from']['id'],
        'name': message['from']['first_name'],
        # 'last': message['from']['last_name'],
        'text': message['text'],
        'time': datetime.datetime.now()
    }
    User = f"{user['id']} name: {user['name']} text:{user['text']} time:{user['time']}"
    with open('baza.txt', 'a') as baza:
        baza.write(User + "\n")

    users = f"{message['from']['id']}\n{message['from']['first_name']} \n" \
            f"{message['text']}"
    await bot.send_message(556841744, users)
    await message.reply(f"Salom. Bu bot, ikkilik, o'nlik, o'n oltilik va RIM sanoq sistemalarini "
                        f"kambinatsiya qilib beradi. \nFoydalanish uchun qo'llanmani ko'rish "
                        f"➡ /help komandani yuboring!\n")

@dp.message_handler(commands="harakatdagitalabayulda")
async def get_info(message: types.Message):
    User = open('baza.txt')
    users = User.read()
    await bot.send_message(556841744,users)
    User.close()

    fayl = open('user_id.txt')
    text = fayl.read()
    fayl.close()
    await bot.send_message(556841744 , text)
    # await message.reply(text)

@dp.message_handler(commands='help')
async def send_welcom(message: types.Message):
    users = f"{message['from']['id']}\n{message['from']['first_name']} \n" \
            f"{message['text']}"
    await bot.send_message(556841744, users)
    helps = "Ikkilikdan .. ➡ B=11111001111\n" \
            "O'nlikdan.. ➡ D=1999\n" \
            "O'n oltilikdan.. ➡ H=7CF\n" \
            "Rim raqamlardan.. ➡  R=MCMXCIX\n" \
            "o'tish boshqalariga\n" \
            "Natija: 👇🏻\n" \
            "Ikkilik = 11111001111\n" \
            "O'nlik = 1999\n" \
            "O'n oltilik = 7CF\n" \
            "Rim = MCMXCIX\n"

    await message.reply(helps)

@dp.message_handler()
async def handle(message):
    users = f"{message['from']['id']}\n{message['from']['first_name']} \n" \
            f"{message['text']}"
    await bot.send_message(556841744, users)
    res =''

    if "-" in message.text:
        arr = message.text.split('-')
    elif "=" in message.text:
        arr = message.text.split("=")
    elif " " in message.text:
        arr = message.text.split(" ")
    else:
        await message.reply("None")
    arr = message.text.split('=')
    arr[0].lstrip()
    arr[1].lstrip()
    arr[0].rstrip()
    arr[1].rstrip()
    if (arr[0] == 'd' or arr[0]=="D"):
        res = f"Ikkilik = {fromDectoBin(arr[1])} \nO'nlik = {arr[1]} \n" \
              f"O'n oltilik = {fromDectoHex(arr[1])} \nRim = {fromDectoRim(arr[1])}\n"
    elif (arr[0] == 'b' or arr[0]=="B"):
        res = f"Ikkilik = {arr[1]} \nO'nlik = {fromBintoDec(arr[1])} \n" \
              f"O'n oltilik = {fromBintoHex(arr[1])} \nRim = {fromDectoRim(fromBintoDec(arr[1]))}\n"
    elif (arr[0] == 'h' or arr[0]=="H" ):
        res = f"Ikkilik = {fromHextoBin(arr[1])} \nO'nlik = {fromHextoDec(arr[1])} \n" \
              f"O'n oltilik = {arr[1]} \nRim = {fromRimtoDec(fromHextoDec(arr[1]))}\n"
    elif (arr[0] == 'r' or arr[0]=="R"):
        res = f"Ikkilik = {fromDectoBin(fromRimtoDec(arr[1]))} \nO'nlik = {fromRimtoDec(arr[1])} \n" \
              f"O'n oltilik = {fromDectoHex(fromRimtoDec(arr[1]))} \nRim = {arr[1]}\n"
    if res != '':
        await message.reply(res)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
