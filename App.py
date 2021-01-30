from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from Components.display import Display
from Components.keybad import Keybad


class Application(App):

    def build(self, **kwargs):

        super().__init__(**kwargs)
        container = BoxLayout(orientation='vertical')

        self.eqn = ''

        self.display = Display(text=self.eqn)
        self.bad = Keybad(updater=self.updateEQN,
                          removelast=self.removelast, clearall=self.clearall, getresult=self.getresult)

        container.add_widget(self.display)
        container.add_widget(self.bad)

        return container

    def updateEQN(self, newValue):
        self.eqn += str(newValue)
        self.display.updateLabel(self.eqn)

    def removelast(self):
        self.eqn = self.eqn[:-1]
        self.display.updateLabel(self.eqn)

    def clearall(self):
        self.eqn = ''
        self.display.updateLabel(self.eqn)

    def getresult(self):
        res = ''
        try:
            res = eval(self.eqn)
        except:
            pass
        self.display.updateLabel(res)


if __name__ == '__main__':
    Application().run()
