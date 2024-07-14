import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class MyApp(App):

    def build(self):
        # Crear un layout de cuadrícula
        layout = GridLayout(cols=1)

        # Agregar un widget Label al layout
        label = Label(text="¡Hola desde Kivy!")
        layout.add_widget(label)

        # Definir la función que se ejecutará al presionar el botón
        def on_button_click(instance):
            label.text = "¡Has presionado el botón!"

        # Agregar un widget Button al layout
        button = Button(text="Presiona aquí")
        button.bind(on_press=on_button_click)
        layout.add_widget(button)

        return layout

if __name__ == "__main__":
    MyApp().run()
