# audio_manager.py
from pydub import AudioSegment
from pydub.playback import play
import os
from config import MUSIC_DIRECTORY

class AudioManager:
    def __init__(self):
        self.current_song = None
        self.is_playing = False

    def load_song(self, song_name):
        """بارگذاری فایل موسیقی از مسیر مشخص"""
        song_path = os.path.join(MUSIC_DIRECTORY, song_name)
        if os.path.exists(song_path):
            self.current_song = AudioSegment.from_file(song_path)
            return True
        return False

    def play_song(self):
        """پخش موسیقی"""
        if self.current_song and not self.is_playing:
            self.is_playing = True
            play(self.current_song)
            self.is_playing = False
            return True
        return False

    def stop_song(self):
        """توقف پخش موسیقی (در صورت نیاز)"""
        self.is_playing = False
        self.current_song = None
        # توجه: pydub امکان توقف مستقیم را ندارد، این تابع برای گسترش‌پذیری آینده است