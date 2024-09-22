import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ["+", "-", "*", "/"]
        self.last_was_operator = False
        self.last_button = None

        # GridLayout avec 5 colonnes
        main_layout = GridLayout(cols=4)

        # TextInput pour afficher les résultats
        self.solution = TextInput(
            readonly=True,
            halign="right",
            font_size=40
        )
        main_layout.add_widget(self.solution)

        # Les boutons de la calculatrice
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', 'C', '+'
        ]

        # Ajout des boutons dans le layout
        for button in buttons:
            main_layout.add_widget(Button(
                text=button,
                on_press=self.on_button_press,
                font_size=32
            ))

        # Bouton "="
        equals_button = Button(
            text="=",
            on_press=self.on_solution,
            font_size=32
        )
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Si le bouton C est pressé, on efface l'écran
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                # Ne pas permettre deux opérateurs consécutifs
                return
            elif current == "" and button_text in self.operators:
                # Ne pas commencer par un opérateur
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                # On évalue l'expression mathématique et on l'affiche
                solution = str(eval(self.solution.text))
                self.solution.text = solution
            except Exception as e:
                # En cas d'erreur dans le calcul
                self.solution.text = "Error"

# Exécution de l'application
if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
