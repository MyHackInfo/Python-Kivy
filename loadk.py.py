from kivy.app import App
from kivy.lang import Builder

get= Builder.load_file("kivy.kv")

class Mains(App):
    def build(self):
        return get()

if __name__ == "__main__":
    Mains().run()
