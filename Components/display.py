from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Display(BoxLayout):
    def __init__(self, text, **kwargs):
        super().__init__(**kwargs)

        self.label = Label(text=text)
        self.label.font_size = 40

        self.padding = 10
        self.size_hint = (1, .1)
        self.add_widget(self.label)

    def updateLabel(self, text):
        self.label.text = str(text)
