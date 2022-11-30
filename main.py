import signal
import time
import pyautogui as pag
import ctypes
import subprocess
from PIL import Image
import win32gui
import win32api
import psutil
import os

ctypes.windll.kernel32.SetConsoleTitleA(b"ExRelog                                      by tg/vk - @sensationnels_dev")
print('''
███████╗██╗  ██╗██████╗ ███████╗██╗      ██████╗  ██████╗ 
██╔════╝╚██╗██╔╝██╔══██╗██╔════╝██║     ██╔═══██╗██╔════╝ 
█████╗   ╚███╔╝ ██████╔╝█████╗  ██║     ██║   ██║██║  ███╗
██╔══╝   ██╔██╗ ██╔══██╗██╔══╝  ██║     ██║   ██║██║   ██║
███████╗██╔╝ ██╗██║  ██║███████╗███████╗╚██████╔╝╚██████╔╝
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝  ╚═════╝ 
Created by @sensationnels_dev

----------------------------------------------
Как пользоваться афк-ботом для ExcaliburCraft?
----------------------------------------------
1) Соблюдайте регистр букв при написании своего ника, если Ваш ник EmBeRaaaq, то вводить надо именно
EmBeRaaaq, а не emberaaaq. Нужно соблюдать чтобы написание ника было как на сервере;
2) Переименуйте лаунчер Excalibur-Craft в ExLauncher;
3) Разрешение экрана Windows должно быть 1366x768, выставить можно через ПКМ по рабочему столу;
4) Запускать лаунчер в окне, растянув на весь экран, режим игры через F11 не подойдёт;
При несоблюдении вышеперечисленных пунктов бот не запустится, либо будет рабоать некорректно.
----------------------------------------------
''')
nick = input("Ваш ник на сервере: ")
time.sleep(1)
subprocess.Popen(("start", "ExLauncher.exe"), shell=True) # открывает лаунчер excaliburcraft
time.sleep(5)
pag.leftClick(1000, 350)
time.sleep(110)
windowPID = win32gui.FindWindow(None, "Excalibur-Craft " + nick)
log_first = str(os.getenv("AppData"))
log_two = "\.exlauncher\clients\skyfactory\logs\latest.log"
exLogs = (log_first + log_two)
pag.moveTo(670,160)
time.sleep(0.4)
pag.leftClick(670, 160)
time.sleep(1)
pag.leftClick(670, 160)
pag.leftClick(670, 160)
time.sleep(2)
pag.moveTo(460, 315)
time.sleep(0.25)
pag.leftClick(460, 315)
time.sleep(2)
pag.moveTo(423, 126)
time.sleep(0.25)
pag.leftClick(423, 126)
time.sleep(5)
file = open(exLogs, "w", encoding="1251")
file.close()
print('''Лаунчер успешно запущен!
         Начинаем АФКшить :)
      ''')

while True:
    time.sleep(5)
    file = open(exLogs, "r", encoding="1251")
    text = file.read()
    file.close()
    if "**СЕРВЕР БУДЕТ ПЕРЕЗАГРУЖЕН ЧЕРЕЗ 1 МИНУТУ**" in text:
        print("На сервере произошел рестарт, ожидаем.")
        time.sleep(150)
        file = open(exLogs, "r", encoding="1251")
        text = file.read()
        file.close()
        if "Stopping all currently running radio streams." in text:
            print("Заходим на сервер после рестарта")
            pag.screenshot("restart.png")
            img = Image.open("restart.png")
            allo = str(img.getpixel((643, 336)))
            print(allo)
            time.sleep(2)
            pag.moveTo(675, 420)
            pag.leftClick(675, 420)
            time.sleep(0.5)
            pag.moveTo(423, 126)
            pag.leftClick(423, 126)
            time.sleep(10)
            pag.screenshot("result.png")
            img_2 = Image.open("result.png")
            hallo = str(img_2.getpixel((643, 336)))
            print(hallo)
            time.sleep(2)
            pag.moveTo(675, 420)
            pag.leftClick(675, 420)
            time.sleep(0.5)
            pag.moveTo(423, 126)
            pag.leftClick(423, 126)
            time.sleep(3)
            file = open(exLogs, "r", encoding="1251")
            text = file.read()
            file.close()
            hallo = str(img_2.getpixel((643, 336)))
            print(hallo)
            if "Нет новых писем." in text:
                file = open(exLogs, "w", encoding="1251")
                file.close()
                print("зашли на сервер")
    elif "Stopping all currently running radio streams." in text:
        file = open(exLogs, "w", encoding="1251")
        file.close()
        print("Вы были в AFK 15 минут.")
        pag.screenshot("restart.png")
        img = Image.open("restart.png")
        allo = str(img.getpixel((643, 336)))
        print(allo)
        time.sleep(5)
        pag.moveTo(675, 420)
        pag.leftClick(675, 420)
        time.sleep(0.5)
        pag.moveTo(423, 126)
        pag.leftClick(423, 126)
        time.sleep(5)
        pag.screenshot("result.png")
        img_2 = Image.open("result.png")
        hallo = str(img_2.getpixel((643, 336)))
        print(hallo)
        file = open(exLogs, "r",encoding="1251")
        text_3 = file.read()
        time.sleep(1)
        if "Нет новых писем." in text_3:
            file = open(exLogs, "w", encoding="1251")
            file.close()
            print("Вход выполнен успешно!")
        elif allo == "(235, 78, 78)" or hallo == "(235, 78, 78)":
            print("~~Пожалуйста, перезапустите лаунчер~~")
            subprocess.call("TASKKILL /F /IM java.exe") # закрывает лаунчер excaliburcraft
            print("Лаунчер закрыт")
            time.sleep(1)
            file = open(exLogs, "w", encoding="1251")
            file.close()
            print("Логи очищены")
            time.sleep(1)
            print("Открываем лаунчер")
            subprocess.Popen(("start", "ExLauncher.exe"), shell=True) # открывает лаунчер excaliburcraft
            time.sleep(5)
            pag.leftClick(1000, 350)
            time.sleep(110)
            pag.moveTo(670, 160)
            time.sleep(0.4)
            pag.leftClick(670, 160)
            time.sleep(1)
            pag.leftClick(670, 160)
            pag.leftClick(670, 160)
            time.sleep(2)
            pag.moveTo(460, 315)
            time.sleep(0.25)
            pag.leftClick(460, 315)
            time.sleep(2)
            pag.moveTo(423, 126)
            time.sleep(0.25)
            pag.leftClick(423, 126)
            time.sleep(5)
            file = open(exLogs, "r", encoding="1251")
            text_2 = file.read()
            if "CoFH World: Load Complete." in text_2:
                file = open(exLogs, "w", encoding="1251")
                file.close()
                print("Лаунчер успешно перезапущен!")

