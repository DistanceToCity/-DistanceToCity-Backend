class FontColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class FontStyle:
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    ENDING = "\033[0m"

class Styling:
    def style_string(string, font_style, font_color ):
        return f"{font_color}{font_style}{string}{FontStyle.ENDING}{FontColor.ENDC}"
    def style_string_hyperlinks(url, string):
        return f"\033]8;;{url}\033\\{string}\033]8;;\033\\"

class Localizations:
    GREETING = "Вітаємо тебе в програмі 'DistanceToCity'! \n З нами ти зможеш легко визначити відстань до будь-якого міста у нашій базі даних. \n Ти можеш допомогти нам розширити базу даних, додаючи нові міста та їх координати."
    OPTIONS_HEADING = "  \n Оберіть один з наступних пунктів меню: "
    OPTIONS = ["1) Розрахувати Відстань", "2) Додати Нове Місто", "3) Отримати Список Міст", "4) Видалити Місто", "5) Вийти з програми" ]
    SELECT_INPUT_TEXT = " Ведіть дані (Назва міста в латиниці та ваші координати через запиту): "
    SELECT_INPUT_TEXT_ADDED_POINT = " Ведіть дані (Назва міста в латиниці та його координати через запиту): "
    SELECT_INPUT_TEXT_DELETE_POINT = " Ведіть дані (Назва міста в латиниці): "
    LIST_PLACES = " Всі міста які ми маємо у базі:"
    def RETURN_DISTANCE(title_geo, distance):
        return f" Дистанція від {title_geo} до вашої точки {int(distance)}км"