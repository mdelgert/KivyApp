# import kivy module
import kivy
   
# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software
#kivy.require("1.9.1")

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App
 
# BoxLayout arranges children
# in a vertical or horizontal box.
from kivy.uix.boxlayout import BoxLayout
 
# class in which we are defining action on click
class RootWidget(BoxLayout):
 
    def btn_clk(self):
        msg = "Button pressed"
        self.lbl.text = msg
        print(msg)
 
# creating action class and calling
# Rootwidget by returning it
class Example1App(App):
 
    def build(self):
        return RootWidget()
 
# creating the myApp root for ActionApp() class 
myApp = Example1App()

# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
myApp.run()

#https://www.geeksforgeeks.org/python-button-action-in-kivy/
#https://kivy.org/doc/stable/guide/events.html
#https://kivy.org/doc/stable/api-kivy.app.html
#https://kivy.org/doc/stable/gettingstarted/installation.html