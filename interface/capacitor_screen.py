
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

from calculations.capacitor import (
    calculate_charge,
    calculate_capacitance
)


class CapacitorScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=12
        )

        heading = Label(
            text="Capacitor Calculator",
            font_size=30,
            bold=True,
            color=(0.2, 0.85, 1, 1)
        )

        self.operation = Spinner(
            text="Calculate Charge",
            values=("Calculate Charge", "Calculate Capacitance")
        )

        self.operation.bind(text=self.update_fields)

        self.first_label = Label(text="Capacitance (F)")
        self.first_input = TextInput(
            hint_text="Enter capacitance in Farads",
            input_filter="float",
            multiline=False
        )

        self.second_label = Label(text="Voltage (V)")
        self.second_input = TextInput(
            hint_text="Enter voltage",
            input_filter="float",
            multiline=False
        )

        calculate_button = Button(text="Calculate")
        calculate_button.bind(on_release=self.calculate)

        self.result_label = Label(
            text="Result will appear here",
            font_size=20,
            color=(0.2, 0.85, 1, 1)
        )

        back_button = Button(text="Back to Dashboard")
        back_button.bind(on_release=self.go_back)

        for widget in (
            heading,
            self.operation,
            self.first_label,
            self.first_input,
            self.second_label,
            self.second_input,
            calculate_button,
            self.result_label,
            back_button
        ):
            layout.add_widget(widget)

        self.add_widget(layout)

    def update_fields(self, spinner, selection):

        if selection == "Calculate Charge":
            self.first_label.text = "Capacitance (F)"
            self.second_label.text = "Voltage (V)"
            self.first_input.hint_text = "Enter capacitance in Farads"
            self.second_input.hint_text = "Enter voltage"

        else:
            self.first_label.text = "Charge (C)"
            self.second_label.text = "Voltage (V)"
            self.first_input.hint_text = "Enter charge in Coulombs"
            self.second_input.hint_text = "Enter voltage"

    def calculate(self, instance):

        try:
            first = float(self.first_input.text)
            second = float(self.second_input.text)

            if self.operation.text == "Calculate Charge":
                result = calculate_charge(first, second)
                unit = "C"

            else:
                result = calculate_capacitance(first, second)
                unit = "F"

            self.result_label.text = f"Result: {result:.6g} {unit}"

        except ValueError as error:
            self.result_label.text = f"Invalid input: {error}"

    def go_back(self, instance):
        self.manager.current = "dashboard"


