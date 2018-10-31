from kivy.app import App
from kivy.uix.button import Button

class Kivy(App):
    def build(self):
        return Button()

if __name__ == "__main__":
    Kivy().run()
