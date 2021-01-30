from kivy.uix.button import Button


class Key(Button):

    def __init__(self, text, keyAction, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 35
        self.text = str(text)
        self.on_press = lambda: keyAction(text)
