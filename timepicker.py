from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.screen import MDScreen

theme_style = "Dark"

class Test(MDApp):
    def build(self):
        return (
            MDScreen(
                MDRaisedButton(
                    text="Open time picker",
                    pos_hint={'center_x': .5, 'center_y': .5},
                    on_release=self.show_time_picker,
                )
            )
        )

    def show_time_picker(self, time):
        from datetime import datetime

        # Must be a datetime object
        previous_time = datetime.strptime("03:20:00", '%H:%M:%S').time()
        time_dialog = MDTimePicker()
        time_dialog.AMPM_or_24h="24h"
        time_dialog.set_time(previous_time)
        time_dialog.open()


Test().run()
