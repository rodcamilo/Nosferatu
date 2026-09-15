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
            "[color=#FFFFFF]Bem-vindo à Eleição 100% confiável do Nosferatu![/color]\n"
            f"[color=#FFFFFF]{sep_init}[/color]\n"
            "[color=#FFFFFF]Digite:[/color]\n"
            "[color=#FF0000]13 - LADRÃO[/color]\n"
            "[color=#00FF00]22 - POLÍCIA[/color]\n"
            "[color=#FF69B4]24 - ISENTÃO[/color]\n"
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

        btn = Button(text="Votar / Confirmar", size_hint_y=None, height=100)
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
                f"\n{sep}\n"
                "[color=#FFFFFF]Resultado da Eleição[/color]\n"
                f"{sep}\n"
                f"[color=#FFFFFF]LADRÃO: {self.ladrao}[color=#FFFFFF] voto(s)![/color]\n"
                f"[color=#FFFFFF]POLÍCIA: {self.policia}[color=#FFFFFF] voto(s)![/color]\n"
                f"[color=#FFFFFF]ISENTÃO: {self.isentao}[color=#FFFFFF] voto(s)![/color]\n"
                f"[color=#FFFFFF]NULOS: {self.nulos}[color=#FFFFFF] voto(s)![/color]\n"
                f"{sep}\n"
                f"[color=#FFFFFF]TOTALIZAÇÃO: {self.total} voto(s)![/color]\n"
                f"{sep}\n"
                "[color=#FFFFFF]Obrigado por acreditar em nossa Ju$tiça Eleitoral![/color]\n"
                f"{sep}\n"
                "[color=#FFFFFF]Este app é apenas uma brincadeira.[/color]\n"
                "[color=#FFFFFF]Qquer semelhança à realidade é só coincidência.[/color]\n"
                "[color=#FFFFFF]Autor: RCDM[/color]\n"
                f"{sep}\n"
            )
        else:
            self.nulos += 1
            self.total += 1
            log = f"{sep}\n[color=#FFFFFF]Você ANULOU seu voto![/color]\n{sep}"

        self.output.text += f"\n\n{log}"

if __name__ == "__main__":
    Nosferatu().run()