from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from story import STORY

Window.clearcolor = get_color_from_hex("#1a1a2e")


class Oyun(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dugum = "baslangic"

        # Diyalog metni
        self.metin = Label(
            text="", font_size="20sp", size_hint=(0.9, 0.35),
            pos_hint={"center_x": 0.5, "y": 0.02},
            halign="left", valign="top", color=(1, 1, 1, 1),
        )
        self.metin.bind(size=self._metni_sar)
        self.add_widget(self.metin)

        # Secenek butonlari
        self.secenek_kutu = BoxLayout(
            orientation="vertical", spacing=8, size_hint=(0.9, 0.4),
            pos_hint={"center_x": 0.5, "y": 0.42},
        )
        self.add_widget(self.secenek_kutu)

        self.goster(self.dugum)

    def _metni_sar(self, *a):
        self.metin.text_size = (self.metin.width, None)

    def goster(self, dugum_adi):
        self.secenek_kutu.clear_widgets()
        dugum = STORY[dugum_adi]
        self.metin.text = dugum["metin"]

        for etiket, hedef in dugum["secenekler"]:
            b = Button(
                text=etiket, font_size="18sp", size_hint_y=None, height="60dp",
                background_color=get_color_from_hex("#e94560"),
            )
            b.bind(on_release=lambda _, h=hedef: self.goster(h))
            self.secenek_kutu.add_widget(b)


class GorselRomanApp(App):
    def build(self):
        return Oyun()


if __name__ == "__main__":
    GorselRomanApp().run()
