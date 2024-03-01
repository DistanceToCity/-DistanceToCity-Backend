import sys
sys.path.append(".")
from Implementations.interface import Interface
from Clients.ui import Styling, FontColor, FontStyle, Localizations
import json








class Console(Interface):
    def greeting(self):
        print("\n "+ Styling.style_string(Localizations.GREETING, FontColor.OKBLUE, FontStyle.BOLD ))
    def select_options(self):
        print(Styling.style_string(Localizations.OPTIONS_HEADING,FontColor.OKBLUE, FontStyle.BOLD))
        print(Styling.style_string("\n   " + "  \n   ".join(Localizations.OPTIONS),FontColor.HEADER, FontStyle.ITALIC ))
        return input(Styling.style_string(Localizations.OPTIONS_HEADING,FontColor.OKBLUE, FontStyle.BOLD))
        return response
    def distance(self):
       input_data = input(Styling.style_string(Localizations.SELECT_INPUT_TEXT,FontColor.OKBLUE, FontStyle.BOLD)).split(",")
       geo = [float(input_data[1]), float(input_data[2])]
       print(Styling.style_string(Localizations.RETURN_DISTANCE(input_data[0], self.get_distance(geo, self.get_geo_by_title(input_data[0]))),FontColor.HEADER, FontStyle.ITALIC))
    def set_place(self):
       input_data = input(Styling.style_string(Localizations.SELECT_INPUT_TEXT,FontColor.OKBLUE, FontStyle.BOLD)).split(",")
       geo = [str(input_data[1]).strip() , str(input_data[2]).strip()]
       print(input_data[0], geo)
       print(self.set_geo(input_data[0], geo))
    def list_places(self):
       print(Styling.style_string(Localizations.LIST_PLACES,FontColor.OKBLUE, FontStyle.BOLD))
       for place in json.loads(self.get_list_geo()):
           links = Styling.style_string_hyperlinks(f'http://www.google.com/maps/place/{",".join(place[1])}', place[0])
           geo = f" широта {place[1][0]} довгота {str(place[1][1]).strip()}"
           print("   " + Styling.style_string(f'{links} - {geo}',FontColor.HEADER, FontStyle.BOLD), )
    def delete_place(self):
       title = input(Styling.style_string(Localizations.SELECT_INPUT_TEXT,FontColor.OKBLUE, FontStyle.BOLD))
       print(self.delete_geo_by_title(title))
        
    



if __name__ == '__main__':
    CLI = Console()
    CLI.greeting()
    isRunning = True
    while isRunning:
        options = CLI.select_options() 
        if(options == "1"):
            CLI.distance()
        if (options == "2"):
            CLI.set_place()
        if (options == "3"):
            CLI.list_places()
        if (options == "4"):
            CLI.delete_place()
        if (options == "5"):
            isRunning = False










#[49.83336983579546, 36.67178842630304], "Kiev"

#print(f"\n{Color.OKBLUE}\033[1m Оберіть один з наступних пунктів меню:{Color.ENDC} \n   1) Розрахувати Відстань \n   2) Додати Нове Місто\n   3) Отримати Список Міст  \n   4) Видалити Місто")

#print(CLI.list_gos()) 