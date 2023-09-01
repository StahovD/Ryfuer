from kivy.properties import NumericPropery, BooleanProperty
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout

class Runer(BoxLayout):
    value = NumericPropery(0)
    finished = BooleanProperty(False)
    
    def __init__(self, total = 10, steptime = 1, **kwargs):
        super().__init__(**kwargs)
        self.total = total
        self.btn_text_inprogress = "Присідяння"
        self.animation = (Animation(pos_hint={
                        'top':0.1}, duration = steptime/2) + 
                        Animation(pos_hint= {'top':0.1}, 
                        

        