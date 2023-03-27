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

kivy.require('1.9.0')


# CHANGE
df = pd.read_csv("drinkRecipes3.csv")
df.set_index('Drink Name', inplace=True)


class HomeScreen(Screen):
    pass

class DrinkMenu(Screen):

    def order_function(self, instance):
        ### insert GRPC call!
        data = df.loc[[instance.text]].iloc[i_containers]
        print(data)

    def on_pre_enter(self):

        self.stack = StackLayout()
        self.add_widget(self.stack)
        if not BarBot.drinks:
            print("No Drinks!")

        else:
            for drink in BarBot.drinks:
                #self.add_widget(Button(background_normal=f'{drink}.png', size_hint=(0.3, 0.3), keep_ratio=False, allow_stretch=True))
                self.stack.add_widget(Button(background_normal=f'pics/{drink}.png', on_press=self.order_function, text=f'{drink}', font_size=32, size_hint=(0.3, 0.3)))
                #self.stack.add_widget()



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
    def __init__(self): 
        super(UI, self).__init__()
        self.add_widget(HomeScreen(name="home"))
        self.add_widget(DrinkMenu(name="menu"))
        self.add_widget(AdminMenu(name="admin"))
        




class BarBot(MDApp):
    
    def build(self):
        BarBot.drinks = ['Margarita', 'Gin and Tonic', 'Vodka Cranberry', 'Old Fashioned', 'Tequila Sunrise']
        return UI()


         


if __name__ == "__main__":
    bb = BarBot()
    bb.run()

