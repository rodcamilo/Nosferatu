from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class NosferatuApp(App):
    def build(self):
        self.ladrao = 0
        self.policia = 0
        self.isentao = 0
        self.nulos = 0
        self.nosf = 0
        self.total = 0

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.output = Label(
            text="\n============================================================\n"
            "Zerésima da Eleição 100% confiável do NOSFERATU: 0 voto(s)\n"
            "============================================================\n"
            "Digite:\n13 - LADRÃO\n22 - POLÍCIA\n24 - ISENTÃO\n99 - APURAR"
            "\n============================================================\n",
            size_hint_y=None, markup=True
        )
        self.output.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        
        scroll = ScrollView(size_hint=(1, 0.7))
        scroll.add_widget(self.output)
        layout.add_widget(scroll)

        self.input_voto = TextInput(hint_text="Digite seu voto", multiline=False, input_filter='int', size_hint_y=None, height=100)
        layout.add_widget(self.input_voto)

        btn = Button(text="Votar / Confirmar", size_hint_y=None, height=100)
        btn.bind(on_press=self.processar_voto)
        layout.add_widget(btn)

        return layout

    def processar_voto(self, instance):
        voto = self.input_voto.text.strip()
        self.input_voto.text = ""
        log = ""

        sep = "============================================================"

        if voto == "13":
            self.ladrao += 1
            self.total += 1
            log = f"{sep}\n[color=#FF0000]Você votou no 13 LADRÃO![/color]\n{sep}"
        elif voto == "24":
            self.isentao += 1
            self.total += 1
            log = f"{sep}\n[color=#FF69B4]Você votou no 24 ISENTÃO![/color]\n{sep}"
        elif voto == "22":
            self.nosf += 1
            self.total += 1
            log = f"{sep}\n[color=#00FF00]Você votou no 22 POLÍCIA![/color]\n{sep}"
            if self.nosf < 2:
                self.policia += 1
            else:
                self.nosf = 0
                self.ladrao += 1
        elif voto == "99":
            log = (
                "\n============================================================\n"
                "[color=#00FF00]Resultado da Eleição[/color]\n"
                "============================================================\n"
                f"LADRÃO: [color=#FF0000]{self.ladrao}[/color] voto(s)!\n"
                f"POLÍCIA: [color=#00FF00]{self.policia}[/color] voto(s)!\n"
                f"ISENTÃO: [color=#FF69B4]{self.isentao}[/color] voto(s)!\n"
                f"NULOS: [color=#FFFF00]{self.nulos}[/color] voto(s)!\n"
                "============================================================\n"
                f"TOTALIZAÇÃO: {self.total} voto(s)!\n"
                "============================================================\n"
                "[color=#00FF00]Obrigado por acreditar CEGAMENTE em nossa Ju$tiça Eleitoral![/color]\n"
                "============================================================\n"
                "Este app é apenas uma brincadeira.\n"
                "Qualquer semelhança com a realidade é mera coincidência.\n"
                "Autor: RCDM\n"
                "============================================================\n"
            )
        else:
            self.nulos += 1
            self.total += 1
            log = f"{sep}\n[color=#FFFF00]Você ANULOU seu voto![/color]\n{sep}"

        self.output.text += f"\n\n{log}"

if __name__ == "__main__":
    NosferatuApp().run()
