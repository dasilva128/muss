# telegram_handler.py
from telegram.ext import Updater, CommandHandler
from telegram import Bot
from config import BOT_TOKEN, ALLOWED_GROUP_ID
from audio_manager import AudioManager

class TelegramHandler:
    def __init__(self):
        self.bot = Bot(token=BOT_TOKEN)
        self.updater = Updater(token=BOT_TOKEN, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.audio_manager = AudioManager()

    def start_command(self, update, context):
        """دستور /start برای شروع ربات"""
        if update.effective_chat.id != ALLOWED_GROUP_ID:
            update.message.reply_text("این ربات فقط در گروه مجاز کار می‌کند!")
            return
        update.message.reply_text("ربات پخش موسیقی آماده است! از /play <نام_آهنگ> استفاده کنید.")

    def play_command(self, update, context):
        """دستور /play برای پخش موسیقی"""
        if update.effective_chat.id != ALLOWED_GROUP_ID:
            update.message.reply_text("این ربات فقط در گروه مجاز کار می‌کند!")
            return

        try:
            song_name = context.args[0]
            if self.audio_manager.load_song(song_name):
                update.message.reply_text(f"در حال پخش: {song_name}")
                self.audio_manager.play_song()
            else:
                update.message.reply_text("آهنگ یافت نشد! لطفاً نام فایل را بررسی کنید.")
        except IndexError:
            update.message.reply_text("لطفاً نام آهنگ را وارد کنید: /play <نام_آهنگ>")

    def stop_command(self, update, context):
        """دستور /stop برای توقف موسیقی"""
        if update.effective_chat.id != ALLOWED_GROUP_ID:
            update.message.reply_text("این ربات فقط در گروه مجاز کار می‌کند!")
            return
        self.audio_manager.stop_song()
        update.message.reply_text("پخش موسیقی متوقف شد.")

    def setup_handlers(self):
        """تنظیم دستورات ربات"""
        self.dispatcher.add_handler(CommandHandler("start", self.start_command))
        self.dispatcher.add_handler(CommandHandler("play", self.play_command))
        self.dispatcher.add_handler(CommandHandler("stop", self.stop_command))

    def start_bot(self):
        """شروع ربات"""
        self.setup_handlers()
        self.updater.start_polling()
        self.updater.idle()