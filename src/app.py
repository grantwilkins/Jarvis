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
import math
kivy.require('1.9.0')


FULL_OZ_CONTAINER = 100


df = pd.read_csv("drinkRecipes3.csv")  # CHANGE
df.set_index('Drink Name', inplace=True)

CONTAINERS = []



class FlavorScreen(Screen): 
    pass


class HomeScreen(Screen):
    pass

class DrinkMenu(Screen):

    def back(self, instance):
        print("hello")
       # self.current = "home"
    

    def order_function(self, instance):
        ### insert GRPC call!!
        drink_row = df.loc[[instance.text]]
        names_of_drinks = list(drink_row.columns)
        [values_from_drink] = drink_row.values.tolist()
        ingredient_tuples = []
        total_oz = 0;
        for idx, amount in enumerate(values_from_drink):
            if amount != 0:
                ingredient_tuples.append((names_of_drinks[idx], amount))
        print(ingredient_tuples)
        for ingredient, amount in ingredient_tuples:
            for container in BarBot.set_containers:
                if container.get_ingredient_name() == ingredient:
                    container.decrease_level(amount)
                    total_oz += amount
                    bbc.place_order(user_id = "test@hotmail.com", 
                                drink_name = container.get_ingredient_name(), 
                                container_num = container.get_container_num(), 
                                amount_oz=amount, 
                                stirring=1)    
        bbc.place_order(user_id = "test@hotmail.com", 
                    drink_name = "Stirring", 
                    container_num = 7, 
                    amount_oz=3, 
                    stirring=1)  
        bbc.place_order(user_id = "test@hotmail.com", 
                    drink_name = "Pump Out", 
                    container_num = 8, 
                    amount_oz=total_oz, 
                    stirring=0)  
        print(instance.text)

    def on_pre_enter(self):

        if not BarBot.drinks:
            print("No Drinks!")

        else:
            print("length")
            print(len(BarBot.drinks))
            num_cols = ceil(len(BarBot.drinks) / 3)
            print("cols")
            print(num_cols)

            for drink in BarBot.drinks:
                self.ids.stack.add_widget(Button(background_normal=f'pics/{drink}.png', on_press=self.order_function, text=f'{drink}', font_size=32, size_hint=(1/num_cols, 0.25)))
        


class AdminMenu(Screen):

    def submit(self):

        BarBot.drinks = []

        ## search for drinks that can be made
        containers = [self.ids.c1.text, self.ids.c2.text, self.ids.c3.text, self.ids.c4.text, self.ids.c5.text, self.ids.c6.text]
     
        i = 0
        i_containers = []
        for col in df.columns:
            if col in containers:
                i_containers.append(i)
            i += 1



        for drink, vals in df.iterrows():
            #print(drink)
            
            i = 0
            i_drink = []
            for val in vals:
                if val > 0:
                    i_drink.append(i)
                i += 1
           
            if i_drink and set(i_drink).issubset(set(i_containers)):
                print(f'{drink} is in!')
                BarBot.drinks.append(drink)


    



class UI(ScreenManager):

    def back_home(self):
        self.current = "home"

    def __init__(self): 
        super(UI, self).__init__()
        self.add_widget(HomeScreen(name="home"))
        self.add_widget(DrinkMenu(name="menu"))
        self.add_widget(AdminMenu(name="admin"))
        
        




class BarBot(MDApp):
    
    def build(self):
        #   BarBot.drinks = ['Margarita', 'Gin and Tonic', 'Vodka Cranberry', 'Old Fashioned', 'Tequila Sunrise']
        BarBot.drinks = []
        return UI()


         


if __name__ == "__main__":
    bb = BarBot()
    bb.run()

