from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


presentation = Builder.load_file("Kivy.kv")

class MainApp(App):
    def build(self):
        return presentation()

if __name__ == "__main__":
    MainApp().run()
