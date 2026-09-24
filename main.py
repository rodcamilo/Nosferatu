from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class Nosferatu(App):
    def build(self):
        self.ladrao = 0
        self.policia = 0
        self.isentao = 0
        self.nulos = 0
        self.nosf = 0
        self.total = 0

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Divisória ajustada para 45 caracteres para caber em telas mobile sem vazar
        sep_init = "============================================="

        self.output = Label(
            text=f"\n[color=#FFFFFF]{sep_init}[/color]\n"
            "[color=#FFFFFF]ELEIÇÃO 100% CONFIÁVEL DO NOSFERATU[/color]\n"
            f"[color=#FFFFFF]{sep_init}[/color]\n"
            "[color=#FFFFFF]DIGITE:[/color]\n"
            "[color=#FFFFFF]13 - LADRÃO[/color]\n"
            "[color=#FFFFFF]22 - POLÍCIA[/color]\n"
            "[color=#FFFFFF]24 - ISENTÃO[/color]\n"
            "[color=#FFFFFF]99 - APURAR[/color]"
            f"\n[color=#FFFFFF]{sep_init}[/color]\n",
            size_hint_y=None, 
            markup=True,
            halign='center'
        )
        
        # Mantém a altura dinâmica conforme o texto cresce (sem quebrar linha)
        self.output.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        
        scroll = ScrollView(size_hint=(1, 0.7))
        scroll.add_widget(self.output)
        layout.add_widget(scroll)

        # Entrada de texto (ativa Enter e mantém foco)
        self.input_voto = TextInput(
            hint_text="Digite seu voto", 
            multiline=False, 
            input_filter='int', 
            size_hint_y=None, 
            height=100
        )
        self.input_voto.bind(on_text_validate=self.processar_voto)
        layout.add_widget(self.input_voto)

        btn = Button(text="VOTAR", size_hint_y=None, height=100)
        btn.bind(on_press=self.processar_voto)
        layout.add_widget(btn)

        return layout

    def processar_voto(self, instance):
        voto = self.input_voto.text.strip()
        self.input_voto.text = ""
        
        # Mantém o teclado aberto e pronto para o próximo voto
        self.input_voto.focus = True
        
        log = ""
        sep = "[color=#FFFFFF]=============================================[/color]"

        if voto == "13":
            self.ladrao += 1
            self.total += 1
            log = f"{sep}\n[color=#FF0000]VOCÊ VOTOU 13 LADRÃO![/color]\n{sep}"
        elif voto == "24":
            self.isentao += 1
            self.total += 1
            log = f"{sep}\n[color=#FF00FF]VOCÊ VOTOU 24 ISENTÃO![/color]\n{sep}"
        elif voto == "22":
            self.nosf += 1
            self.total += 1
            log = f"{sep}\n[color=#FFFF00]VOCÊ VOTOU 22 POLÍCIA![/color]\n{sep}"
            if self.nosf < 2:
                self.policia += 1
            else:
                self.nosf = 0
                self.ladrao += 1
        elif voto == "99":
            log = (
                f"\n{sep}\n"
                "[color=#FFFFFF]APURAÇÃO DOS VOTOS[/color]\n"
                f"{sep}\n"
                f"[color=#FFFFFF]LADRÃO: {self.ladrao}[color=#FFFFFF] VOTO(S)[/color]\n"
                f"[color=#FFFFFF]POLÍCIA: {self.policia}[color=#FFFFFF] VOTO(S)[/color]\n"
                f"[color=#FFFFFF]ISENTÃO: {self.isentao}[color=#FFFFFF] VOTO(S)[/color]\n"
                f"[color=#FFFFFF]NULOS: {self.nulos}[color=#FFFFFF] VOTO(S)[/color]\n"
                f"{sep}\n"
                f"[color=#FFFFFF]TOTALIZAÇÃO: {self.total}  VOTO(S)[/color]\n"
                f"{sep}\n"
                "[color=#FFFFFF]Este app é apenas uma sátira.[/color]\n"
                "[color=#FFFFFF]Qualquer semelhança com a realidade[/color]\n"
                "[color=#FFFFFF]é mera coincidência.[/color]\n"
                f"{sep}\n"
            )
        else:
            self.nulos += 1
            self.total += 1
            log = f"{sep}\n[color=#FFFFFF]VOCÊ ANULOU SEU VOTO![/color]\n{sep}"

        self.output.text += f"\n\n{log}"

if __name__ == "__main__":
    Nosferatu().run()
