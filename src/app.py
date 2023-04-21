import kivy
import pandas as pd
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.stacklayout import StackLayout 
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
import container as c
import barbot_client as bbc
import barbot_pb2 
from math import ceil
kivy.require('1.9.0')


FULL_OZ_CONTAINER = 25.3605 # 750 mL

df = pd.read_csv("drinkRecipes3.csv")  # CHANGE
df.set_index('Drink Name', inplace=True)

CONTAINERS = []
FLAVOR_NAMES = ["Mint", "Lime", "None"]
FLAVOR_COLORS = ["#00FF00", "#FFFF00", "#FFFFFF"]
CONTAINER_COLORS= ["#FF0000", "#FFA500", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3", "#FFFFFF"]
FLAVOR_DICT = dict(zip(FLAVOR_NAMES, FLAVOR_COLORS))

# These global variables define the
# information for the current order
DRINK_NAME = ""
FLAVOR_TO_ORDER = "None" # "None" is no flavor
FLAVOR_ID = 0 # 0 is no flavor
ORDER_ARR = []

class AdminMenu(Screen):
    def clean(self):
        bbc.clean_system("admin")
    pass

class LevelMenu(Screen):
    def on_pre_enter(self):
        global CONTAINERS
        l = len(CONTAINERS)
        self.ids.stack.clear_widgets()
        self.ids.stack.add_widget(Button(text="Container Levels",background_color="blue",font_size=48, size_hint=(1, 1/(l+1))))
        for container in CONTAINERS:
            self.ids.stack.add_widget(Button(text=container.ingredient_name + ": " + str(container.container_level) + " oz at " + str(container.container_level / FULL_OZ_CONTAINER * 100) + "%",
                                             font_size=48,
                                                background_color=CONTAINER_COLORS[container.container_num-1],
                                             size_hint=(1, 1/(l+1))))

class FlavorMenu(Screen): 

        def order_function(self, instance):
            global FLAVOR_TO_ORDER, FLAVOR_ID
            flavor_num = FLAVOR_NAMES.index(instance.text) + 1
            if(instance.text != "None"):
                FLAVOR_TO_ORDER = instance.text
                FLAVOR_ID = flavor_num
            self.manager.current = "drinkOrderSynopsis"

        def on_pre_enter(self):
            self.ids.stack.clear_widgets()
            self.ids.stack.add_widget(Button(text="Select Flavor",background_color="blue",font_size=40, size_hint=(1, 0.1)))
            for flavor in FLAVOR_NAMES:
                self.ids.stack.add_widget(Button(on_press=self.order_function,background_color=FLAVOR_DICT[flavor] ,text=flavor,font_size=48, size_hint=(1, 1/len(FLAVOR_NAMES))))


class HomeScreen(Screen):

    def admin(self, instance):
        self.manager.current = "admin"

    def on_pre_enter(self):
        global DRINK_NAME, FLAVOR_TO_ORDER, FLAVOR_ID, ORDER_ARR
        DRINK_NAME = ""
        FLAVOR_TO_ORDER = "None"
        FLAVOR_ID = 0
        ORDER_ARR = []
        self.ids.fl.add_widget(Button(background_normal=f'pics/wrench-icon.png', 
                                                on_press=self.admin, 
                                                pos_hint={"x":0.0, "y":0.0},
                                                size_hint=(0.1,0.15)))

class DrinkOrderSynopsis(Screen):
    def order_function(self, instance):
        global DRINK_NAME, FLAVOR_TO_ORDER, FLAVOR_ID, ORDER_ARR
        bbc.place_order(user_id="admin",
                        drink_name=DRINK_NAME,
                        order_tuple=ORDER_ARR,
                        flavor_name=FLAVOR_TO_ORDER,
                        flavor_id=FLAVOR_ID)
        DRINK_NAME = ""
        FLAVOR_TO_ORDER = "None"
        FLAVOR_ID = 0
        ORDER_ARR = []
        self.manager.current = "home"

    def on_pre_enter(self):
        global DRINK_NAME, FLAVOR_TO_ORDER, FLAVOR_ID
        self.ids.stack.clear_widgets()
        '''
        Add text to this screen that sums up the order
        '''
        self.ids.stack.add_widget(Button(text="Order Summary", font_size=48, size_hint=(1, 0.3), background_color="blue"))
        self.ids.stack.add_widget(Button(text="Drink Name: " + DRINK_NAME, font_size=48,size_hint=(1, 0.2), background_color="tan"))
        self.ids.stack.add_widget(Button(text="Flavor: " + FLAVOR_TO_ORDER, font_size=48, size_hint=(1, 0.2), background_color="tan"))
        self.ids.stack.add_widget(Button(text="Order!", font_size=48, on_press=self.order_function, size_hint=(1, 0.3), background_color="green"))


class DrinkMenu(Screen):
    def back(self, instance):
        self.manager.current = "home"

    def order_function(self, instance):
        global ORDER_ARR, DRINK_NAME
        DRINK_NAME = instance.text
        drink_row = df.loc[[instance.text]]
        names_of_drinks = list(drink_row.columns)
        [values_from_drink] = drink_row.values.tolist()
        ingredient_tuples = []
        for idx, amount in enumerate(values_from_drink):
            if amount != 0:
                ingredient_tuples.append((names_of_drinks[idx], amount))
        for ingredient, amount in ingredient_tuples:
            for container in CONTAINERS:
                if container.get_ingredient_name() == ingredient:
                    container.decrease_level(amount)
                    ORDER_ARR.append(barbot_pb2.OrderTuple(container_id=container.container_num, amount_oz=amount))
        self.manager.current = "flavor"
        


    def on_pre_enter(self):

        self.ids.stack.clear_widgets()
        self.ids.stack.add_widget(Button(text="Click a drink to order it!",
                                         background_color=[0.82, 0.7, 0.54, 1],
                                         font_size=40, 
                                         size_hint=(1, 0.25),
                                         font_name="art/Harlow"))

        for drink in BarBot.drinks:
            self.ids.stack.add_widget(Button(background_normal=f'pics/{drink}.png', 
                                                on_press=self.order_function, 
                                                text=f'{drink}', 
                                                font_size=32,
                                                size_hint = (0.2,0.25)
                                                ))
                                                #,size_hint=(1/num_cols, 0.25)))
        


class ConfigMenu(Screen):

    def submit(self):

        BarBot.drinks = []
        global CONTAINERS
        ## search for drinks that can be made
        containers = [self.ids.c1.text, self.ids.c2.text, self.ids.c3.text, self.ids.c4.text, self.ids.c5.text, self.ids.c6.text]
        CONTAINERS = []
        for container_name in containers:
            if(container_name == ""):
                continue
            CONTAINERS.append(c.Container(ingredient_name= container_name, 
                                        container_level=FULL_OZ_CONTAINER,
                                        container_num= containers.index(container_name) + 1))

        i = 0
        i_containers = []
        for col in df.columns:
            if col in containers:
                i_containers.append(i)
            i += 1

        for drink, vals in df.iterrows():
            
            i = 0
            i_drink = []
            for val in vals:
                if val > 0:
                    i_drink.append(i)
                i += 1
           
            if i_drink and set(i_drink).issubset(set(i_containers)) and drink not in BarBot.drinks:
                BarBot.drinks.append(drink)
        


class UI(ScreenManager):

    def back_home(self):
        self.current = "home"

    def __init__(self): 
        super(UI, self).__init__()
        self.add_widget(HomeScreen(name="home"))
        self.add_widget(DrinkMenu(name="menu"))
        self.add_widget(ConfigMenu(name="config"))
        self.add_widget(FlavorMenu(name="flavor"))
        self.add_widget(LevelMenu(name="levels"))
        self.add_widget(AdminMenu(name="admin"))
        self.add_widget(DrinkOrderSynopsis(name="drinkOrderSynopsis"))

class BarBot(MDApp):
    
    def build(self):
        BarBot.drinks = ['Margarita', 'Gin and Tonic', 'Vodka Cranberry', 'Old Fashioned', 'Tequila Sunrise']
        #BarBot.drinks = []
        return UI()

if __name__ == "__main__":
    bb = BarBot()
    bb.run()

