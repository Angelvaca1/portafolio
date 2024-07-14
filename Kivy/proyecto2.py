from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
import random

class CoinFlipApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        self.result_label = Label(text="Presiona 'Lanzar Moneda' para empezar", font_size=24, halign='center')
        layout.add_widget(self.result_label)

        self.coin_image = Image(source='rugal.png', size_hint=(None, None), size=(200, 200))
        layout.add_widget(self.coin_image)

        flip_button = Button(text='Lanzar Moneda', font_size=20, size_hint=(None, None), size=(200, 50))
        flip_button.bind(on_press=self.flip_coin)
        layout.add_widget(flip_button)

        self.flip_sound = SoundLoader.load('kof.wav')

        return layout

    def flip_coin(self, instance):
        result = random.choice(['Aguila', 'Sol'])
        self.result_label.text = f"¡{result}!"

        if result == 'Aguila':
            self.coin_image.source = 'k9999.png'
        else:
            self.coin_image.source = 'angel.png'

        if self.flip_sound:
            self.flip_sound.play()

if __name__ == '__main__':
    CoinFlipApp().run()