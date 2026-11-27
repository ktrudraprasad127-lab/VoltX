
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

from calculations.resistance import calculate_resistance


class ResistorScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        heading = Label(
            text="Resistor Colour Code Calculator",
            font_size=26,
            bold=True,
            color=(0.2, 0.85, 1, 1)
        )

        self.band1 = Spinner(
            text="Brown",
            values=("Black", "Brown", "Red", "Orange",
                    "Yellow", "Green", "Blue", "Violet",
                    "Grey", "White")
        )

        self.band2 = Spinner(
            text="Black",
            values=("Black", "Brown", "Red", "Orange",
                    "Yellow", "Green", "Blue", "Violet",
                    "Grey", "White")
        )

        self.band3 = Spinner(
            text="Red",
            values=("Black", "Brown", "Red", "Orange",
                    "Yellow", "Green", "Blue", "Gold", "Silver")
        )

        self.band4 = Spinner(
            text="Gold",
            values=("Brown", "Red", "Green", "Blue",
                    "Violet", "Grey", "Gold", "Silver")
        )

        calculate_button = Button(text="Calculate Resistance")
        calculate_button.bind(on_release=self.calculate)

        self.result_label = Label(
            text="Select colours and calculate",
            font_size=20,
            color=(0.2, 0.85, 1, 1)
        )

        back_button = Button(text="Back to Dashboard")
        back_button.bind(on_release=self.go_back)

        for widget in (
            heading,
            Label(text="Band 1 - First Digit"),
            self.band1,
            Label(text="Band 2 - Second Digit"),
            self.band2,
            Label(text="Band 3 - Multiplier"),
            self.band3,
            Label(text="Band 4 - Tolerance"),
            self.band4,
            calculate_button,
            self.result_label,
            back_button
        ):
            layout.add_widget(widget)

        self.add_widget(layout)

    def calculate(self, instance):

        try:
            resistance, tolerance = calculate_resistance(
                self.band1.text,
                self.band2.text,
                self.band3.text,
                self.band4.text
            )

            self.result_label.text = (
                f"Resistance: {resistance:g} Ω\n"
                f"Tolerance: ±{tolerance:g}%"
            )

        except ValueError as error:
            self.result_label.text = str(error)

    def go_back(self, instance):
        self.manager.current = "dashboard"
