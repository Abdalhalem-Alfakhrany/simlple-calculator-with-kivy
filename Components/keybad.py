from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from .key import Key


class Keybad(StackLayout):
    def __init__(self, updater, getresult, removelast, clearall, **kwargs):
        super().__init__(**kwargs)

        # self.padding = 5
        # self.spacing = 5
        self.size_hint = (1, .8)

        keys = ["+", "-", "*"]
        for i in range(1, 10):
            k = None
            k = Key(text=i, keyAction=updater)
            k.size_hint = (.25, .2)
            self.add_widget(k)

            if(i % 3 == 0):
                k = Key(text=keys.pop(), keyAction=updater)
                k.size_hint = (.25, .2)
                self.add_widget(k)

        keys = ['.', '0']
        for key in keys:
            k = Key(text=key, keyAction=updater)
            k.size_hint = (.25, .2)
            self.add_widget(k)

        clear = Button(text='C')
        clear.on_press = clearall
        clear.font_size = 35
        clear.size_hint = (.25, .2)

        poplast = Button(text='D')
        poplast.on_press = removelast
        poplast.font_size = 35
        poplast.size_hint = (.25, .2)

        self.add_widget(clear)

        devidor = Key(text='/', keyAction=updater)
        devidor.size_hint = (.25, .2)

        self.add_widget(devidor)

        Equal = Button(text='=')
        Equal.on_press = getresult
        Equal.font_size = 35
        Equal.size_hint = (.75, .2)

        self.add_widget(Equal)
        self.add_widget(poplast)
