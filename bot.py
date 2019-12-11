import telebot # pyTelegramBotAPI da telebot ni import qilish
from others import * # others faylidan barcha o'zgaruvchilarni import qilish

bot = telebot.TeleBot(token) # bot o'zgaruvchiga bot tekonenini kiritib u orqali ishlaymiz

# Botga /start bosganda javob qaytarish
@bot.message_handler(commands=['start'])
def send_start(s): # s - bu habarr metkasi, biz habarga murojat qilganimizda s deb o'tib ketamiz.
# bot.send_message botga habar jo'natish buyrug'i. U o'z ichiga habar jo'natish chat ID raqami, matn, matnni reply qilib jo'natish uchun habar ID raqami, matn formati va boshqalarni o'z ichiga oladi
    bot.send_message(s.chat.id, text=start_text.format(s.from_user.first_name, s.from_user.username), # matnda foydalanuvchi Ismi va uning profiliga URL adresni joylashtirish uchun textda {}dan foydalanib, .format() funksiya orqali skobkalar o'rniga foydalanuvchi ismi va username ni ko'rsatamiz
                     reply_to_message_id=s.message_id, parse_mode='Markdown', disable_web_page_preview=True) # qaysi habarga reply qilish, matn formati va URL ni oldindan ko'rish funksiyasini sozlaymiz

# /help buyrug'iga javob jo'natish
@bot.message_handler(commands=['help'])
def send_help(sos):
    bot.send_message(sos.chat.id, text=sos_text, reply_to_message_id=sos.message_id, parse_mode='Markdown')

# /about buyrug'iga javob jo'natish
@bot.message_handler(commands=['about'])
def send_about(a):
    bot.send_message(a.chat.id, text=about, reply_to_message_id=a.message_id, parse_mode='Markdown')

# /commands buyrug'iga javob jo'natish
@bot.message_handler(commands=['commands'])
def send_commands(c):
    bot.send_message(c.chat.id, text=commands, reply_to_message_id=c.message_id, parse_mode='Markdown')

# botni ishga tushurish
bot.polling()
