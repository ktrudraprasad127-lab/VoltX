
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

from interface.ohms_law_screen import OhmsLawScreen
from interface.resistor_screen import ResistorScreen
from interface.capacitor_screen import CapacitorScreen


class DashboardScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        title = Label(
            text="VoltX",
            font_size=52,
            bold=True,
            color=(0.2, 0.85, 1, 1),
            size_hint_y=0.20
        )

        subtitle = Label(
            text="Precision Circuit Analysis, Component Intelligence & Signal Simulation",
            font_size=17,
            halign="center",
            size_hint_y=0.12
        )

        tagline = Label(
            text="Engineer Your Skills. Master Every Circuit.",
            font_size=16,
            italic=True,
            color=(0.65, 0.75, 0.85, 1),
            size_hint_y=0.10
        )

        dashboard = GridLayout(
            cols=2,
            spacing=15,
            padding=20,
            size_hint_y=0.50
        )

        modules = [
            "Electrical Calculations",
            "Component Analysis",
            "Circuit Solver",
            "Signal Analysis",
            "Capacitor Analysis"
        ]

        for module in modules:

            button = Button(
                text=module,
                font_size=20,
                bold=True,
                background_normal="",
                background_color=(0.08, 0.25, 0.36, 1),
                color=(0.2, 0.85, 1, 1)
            )

            button.bind(
                on_release=lambda instance, name=module:
                self.open_module(name)
            )

            dashboard.add_widget(button)

        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(tagline)
        layout.add_widget(dashboard)

        self.add_widget(layout)

    def open_module(self, module_name):

        if module_name == "Electrical Calculations":
            self.manager.current = "ohms_law"

        elif module_name == "Component Analysis":
            self.manager.current = "resistor"

        elif module_name == "Capacitor Analysis":
            self.manager.current = "capacitor"

        else:
            print(f"{module_name} is coming soon!")


class VoltXApp(App):

    def build(self):

        Window.size = (1000, 650)
        Window.clearcolor = (0.05, 0.07, 0.12, 1)

        screen_manager = ScreenManager()

        dashboard = DashboardScreen(name="dashboard")
        calculator = OhmsLawScreen(name="ohms_law")
        resistor = ResistorScreen(name="resistor")
        capacitor = CapacitorScreen(name="capacitor")

        screen_manager.add_widget(dashboard)
        screen_manager.add_widget(calculator)
        screen_manager.add_widget(resistor)
        screen_manager.add_widget(capacitor)

        return screen_manager


if __name__ == "__main__":
    VoltXApp().run()
