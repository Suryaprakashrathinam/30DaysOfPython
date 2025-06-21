from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner


def convert_temp(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return value

    if from_unit == 'fahrenheit':
        value = (value - 32) * 5/9
    elif from_unit == 'kelvin':
        value = value - 273.15
    elif from_unit != 'celsius':
        raise ValueError("Invalid from_unit")

    if to_unit == 'fahrenheit':
        return value * 9/5 + 32
    elif to_unit == 'kelvin':
        return value + 273.15
    elif to_unit == 'celsius':
        return value
    else:
        raise ValueError("Invalid to_unit")


class TempConverter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.input_temp = TextInput(hint_text="Enter temperature", multiline=False)
        self.add_widget(self.input_temp)

        self.from_unit = Spinner(text='Celsius', values=('Celsius', 'Fahrenheit', 'Kelvin'))
        self.add_widget(self.from_unit)

        self.to_unit = Spinner(text='Fahrenheit', values=('Celsius', 'Fahrenheit', 'Kelvin'))
        self.add_widget(self.to_unit)

        self.result_label = Label(text="Result will appear here")
        self.add_widget(self.result_label)

        self.convert_button = Button(text="Convert", on_press=self.convert)
        self.add_widget(self.convert_button)

    def convert(self, instance):
        try:
            value = float(self.input_temp.text)
            result = convert_temp(value, self.from_unit.text, self.to_unit.text)
            self.result_label.text = f"{value} {self.from_unit.text} = {result:.2f} {self.to_unit.text}"
        except ValueError:
            self.result_label.text = "Please enter a valid number!"


class TempApp(App):
    def build(self):
        return TempConverter()


if __name__ == "__main__":
    TempApp().run()
