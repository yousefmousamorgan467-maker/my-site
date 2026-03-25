from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window

class MyCalc(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        main_layout = BoxLayout(orientation="vertical", padding=10)
        self.result = Label(text="0", font_size=50, size_hint_y=0.4)
        main_layout.add_widget(self.result)
        
        buttons_layout = GridLayout(cols=4, spacing=5)
        btns = ["7","8","9","/", "4","5","6","*", "1","2","3","-", ".","0","C","+"]
        for b in btns:
            btn = Button(text=b, font_size=30)
            btn.bind(on_press=self.click)
            buttons_layout.add_widget(btn)
            
        main_layout.add_widget(buttons_layout)
        eq = Button(text="=", size_hint_y=0.2, background_color=(0,1,0,1))
        eq.bind(on_press=self.calc)
        main_layout.add_widget(eq)
        return main_layout

    def click(self, instance):
        if instance.text == "C": self.result.text = "0"
        else: self.result.text = (instance.text if self.result.text=="0" else self.result.text + instance.text)

    def calc(self, instance):
        try: self.result.text = str(eval(self.result.text))
        except: self.result.text = "Error"

if __name__ == "__main__":
    MyCalc().run()
