
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import Screen

from calculations.ohms_law import (
    calculate_voltage,
    calculate_current,
    calculate_resistance
)


class OhmsLawScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        heading = Label(
            text="Ohm's Law Calculator",
            font_size=30,
            bold=True,
            color=(0.2, 0.85, 1, 1)
        )

        self.calculation_type = Spinner(
            text="Calculate Voltage (V)",
            values=(
                "Calculate Voltage (V)",
                "Calculate Current (I)",
                "Calculate Resistance (R)"
            )
        )

        self.calculation_type.bind(text=self.update_fields)

        self.first_label = Label(text="Current (A)")
        self.first_input = TextInput(
            hint_text="Enter current",
            input_filter="float",
            multiline=False
        )

        self.second_label = Label(text="Resistance (Ω)")
        self.second_input = TextInput(
            hint_text="Enter resistance",
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
            self.calculation_type,
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

        if selection == "Calculate Voltage (V)":
            self.first_label.text = "Current (A)"
            self.second_label.text = "Resistance (Ω)"
            self.first_input.hint_text = "Enter current"
            self.second_input.hint_text = "Enter resistance"

        elif selection == "Calculate Current (I)":
            self.first_label.text = "Voltage (V)"
            self.second_label.text = "Resistance (Ω)"
            self.first_input.hint_text = "Enter voltage"
            self.second_input.hint_text = "Enter resistance"

        else:
            self.first_label.text = "Voltage (V)"
            self.second_label.text = "Current (A)"
            self.first_input.hint_text = "Enter voltage"
            self.second_input.hint_text = "Enter current"

    def calculate(self, instance):

        try:
            first = float(self.first_input.text)
            second = float(self.second_input.text)

            selection = self.calculation_type.text

            if selection == "Calculate Voltage (V)":
                result = calculate_voltage(first, second)
                unit = "V"

            elif selection == "Calculate Current (I)":
                result = calculate_current(first, second)
                unit = "A"

            else:
                result = calculate_resistance(first, second)
                unit = "Ω"

            self.result_label.text = f"Result: {result:.4f} {unit}"

        except ValueError as error:
            self.result_label.text = f"Invalid input: {error}"

    def go_back(self, instance):
        self.manager.current = "dashboard"
