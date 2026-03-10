import yt_dlp
import telebot

TOKEN = "7953484219:AAEGvUwwb-OH4ixVAvI4NPUzTU27L47EI9E"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def download_video(message):
    url = message.text

    try:
        ydl_opts = {
            'outtmpl': 'video.mp4'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        with open("video.mp4", "rb") as video:
            bot.send_video(message.chat.id, video)

    except:
        bot.reply_to(message, "Không tải được video")

bot.polling()
