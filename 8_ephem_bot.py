"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime
import settings


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("planet", planet_position))
    mybot.start_polling()
    mybot.idle()

PLANETS = {
    "Mercury": ephem.Mercury(),
    "Venus": ephem.Venus(),
    "Mars": ephem.Mars(),
    "Earth": ephem.Earth(),
    "Jupiter": ephem.Jupiter(),
    "Saturn": ephem.Saturn(),
    "Uranus": ephem.Uranus(),
    "Neptune": ephem.Neptune(),
    "Pluto": ephem.Pluto(),
}

def planet_position(update, context):
    planet_name = update.message.text.split()[1].capitalize()
    if planet_name not in PLANETS:
        update.message.reply_text(f"Планета {planet_name} не найдена.")
        return
    
    planet = PLANETS[planet_name]
    planet.compute(datetime.now())
    constellation = ephem.constellation(planet)

    update.message.reply_text(f"Планета {planet_name} сегодня находится в созвездии {constellation[1]}.")
    

if __name__ == "__main__":
    main()