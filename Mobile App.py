import kivy
from kivy.app import app
from kivy.uix.gridlayout import Gridlayout
from  kivy.uix.label import Label
from kivy.uix.textinput import Textinput
from kivy.uix.button import Button

class childApp(Gridlayout):
    def __init__(self,**kwargs):
        super(childApp,self).__init__()
        self.cols = 2
        #this is pending.....
        
