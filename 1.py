# connect library
from gtts import gTTS
from pygame import *
import os
import time
import random
from colorama import init, Fore, Back, Style
from rich.console import Console
from rich.table import Table



init(autoreset=True)
#colored text

console = Console()
#table (text №2)
table = Table(title="Таблиця оцінок")
#part1
table.add_column("Ім’я", justify="left", style="cyan", no_wrap=True)
table.add_column("Математика", justify="center", style="magenta")
table.add_column("Фізика", justify="center", style="green")
#part2
table.add_row("Аня", "12", "14")
table.add_row("Богдан", "15", "16")
table.add_row("Катя", "14", "15")
#print all of this out
console.print(table)

##############################################

def colored_text(text: str, color: str = "RED") -> str:
    
     # Dictionary for color mapping
    color_dict = {
        "RED": Fore.RED,
        "GREEN": Fore.GREEN,
        "YELLOW": Fore.YELLOW,
        "BLUE": Fore.BLUE,
        "MAGENTA": Fore.MAGENTA,
        "CYAN": Fore.CYAN,
        "WHITE": Fore.WHITE
    }
    
    return color_dict.get(color.upper(), Fore.WHITE) + text

def print_colored_background(text: str, background: str = "RED") -> str:
    
     # Dictionary for color mapping
    background_dict = {
        "RED": Back.RED,
        "GREEN": Back.GREEN,
        "YELLOW": Back.YELLOW,
        "BLUE": Back.BLUE,
        "MAGENTA": Back.MAGENTA,
        "CYAN": Back.CYAN,
        "WHITE": Back.WHITE
    }
    
    return background_dict.get(background.upper(), Back.WHITE) + text


print(colored_text ("Тъгата отлита на крилете на времето.", "RED"))
print(print_colored_background ("людмила", "CYAN"))
print(colored_text ("wish you the best", "GREEN"))
print(print_colored_background ("nektaryinki", "YELLOW"))

#############################################




def text_to_speech(phrase: str, lang: str = "uk") -> str:
    """
    Функція озвучує переданий текст і зберігає його у mp3 файл з унікальною назвою.
    
    Параметри:
    phrase (str) : Текст, який потрібно озвучити
    lang (str)   : Мова озвучення (за замовчуванням українська "uk")
    
    Повертає:
    str : назва збереженого mp3 файлу
    """
    # Додаємо випадкове число до назви файлу для унікальності
    filename = f"voice_{random.randint(1000, 9999)}.mp3"
   
    # Створюємо об'єкт з текстом у gTTS
    tts = gTTS(phrase, lang=lang)
    # Зберігає пустий файл
    tts.save(filename)
    # Запуск мікшера, загружаємо файл і програємо
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    # Кожні пів секунди перевірка чи зайнятий процес запису у файлі
    while mixer.music.get_busy():
        time.sleep(0.5)
    # Прибирає музику з загрузки і виходить
    mixer.music.unload()
    mixer.quit()
    
    return filename





def delete_file(filename: str) -> bool: 
    """
    Функція видаляє файл з диску.
    
    Параметри:
    filename (str) : Назва файлу для видалення
    
    Повертає:
    bool : True, якщо файл видалено успішно, False, якщо сталася помилка
    """
    try:
        # Видаляє файл
        os.remove(filename)
        return True
    except Exception as e:
        print(f"Помилка при видаленні файлу: {e}")
        return False


###############################
f=input("Введіть фразу для озвучки:")
l=int(input("Введіть мову: 1-укр 2 англ:"))
my_lang="uk"
if l==1:
    my_lang="uk"
elif l==2:
    my_lang="en"
else:
    print("Не вірна мова")

file: str = text_to_speech(f,my_lang)
success: bool =delete_file(file)
print(f"Файл видалено:{success}")


