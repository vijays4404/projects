from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.expression = ''
        self.display = TextInput(text='', readonly=True, font_size=40)
        layout.add_widget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', '%']
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                btn = Button(text=label, font_size=40)
                btn.bind(on_press=self.on_button_press)
                h_layout.add_widget(btn)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        symbol = instance.text
        if symbol == 'C':
            self.expression = ''
        elif symbol == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = 'Error'
        else:
            self.expression += symbol
        self.display.text = self.expression

if __name__ == '__main__':
    CalculatorApp().run()
