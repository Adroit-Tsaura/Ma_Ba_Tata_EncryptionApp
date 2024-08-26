from cipher import CeaserCipher
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty


# Load User Interface
Builder.load_string("""
<MainScreen>:
    app_bar: app_bar
    input: input
    my_slider: my_slider
    my_switch: my_switch
    output: output
    MDFloatLayout:
        size: root.width, root.height

        MDTopAppBar:
            id: app_bar
            title: root.title_bar_text
            pos_hint: {"top":1}
            elevation: 0
            left_action_items: [["menu","Menu"]]
            right_action_items:
                [["swap-vertical", lambda x: root.swap_mode(), "Swap modes    "]]

        MDTextField:
            id: input
            hint_text: "Type or paste copied message"
            mode: "rectangle"
            size_hint: .8, .25
            multiline: True
            pos_hint: {"center_x":0.5, "center_y":.75}
        MDLabel:
            text: "" + button.text + " key: [b]" + str(int(my_slider.value)) + "[/b]"
            size_hint: None, None
            height: self.texture_size[1]
            width: "150dp"
            pos_hint: {"center_y":0.58, "center_x":0.355}
            font_size: "16dp"
            markup: True
            theme_text_color: "Custom"
            text_color: "#FF9500"
        MDSlider:
            id: my_slider
            max: 13
            value: 7
            pos_hint: {"center_x":0.69, "center_y":0.58}
            size_hint: .5, None
        MDFillRoundFlatButton:
            id: button
            text: "Encrypt" if app_bar.title == "Encryption" else "Decrypt"
            size_hint: .8, None
            pos_hint: {"center_x":0.5, "center_y":0.5}
            font_size: "18dp"
            on_release: root.on_button_release(self)
        MDTextField:
            id: output
            hint_text: "Your encrypted message" if button.text == "Encrypt" else "Your decrypted message"
            mode: "rectangle"
            size_hint: .8, .25
            multiline: True
            disabled: False
            readonly: True
            pos_hint: {"center_x":0.5, "y":.2}
        MDFloatingActionButton:
            icon: "content-copy"
            pos_hint: {"right":.9, "y":0.06}
            on_release: root.copy_text(self)
        MDLabel:
            id: text_mode
            text: "Dark" if my_switch.active == True else "Light"
            size_hint: None, None
            height: self.texture_size[1]
            width: "150dp"
            theme_text_color: "Hint"
            pos_hint: {"center_y":0.15, "center_x":0.31}
        MDSwitch:
            id: my_switch
            active: True
            on_active: app.on_switch_active(self)
            pos_hint: {"x":0.06, "y":0.06}
""")
# Set the window size to mobile device
#Window.size = (320, 580)


# Define the MainScreen
class MainScreen(MDScreen):
    title_bar_text = StringProperty("Encryption")
    encrypt = BooleanProperty(True)

    def copy_text(self, icon):
        import pyperclip
        copied_text = self.ids.output.text
        
        try:
            from kivymd.uix.snackbar import Snackbar
            
            if copied_text != "":
                Snackbar(text="Message copied!").open()
                pyperclip.copy(copied_text)

        except Exception:
            from kivymd.uix.dialog import MDDialog
            dialog = MDDialog(text="Text copied!")
            
            if copied_text != "":
                pyperclip.copy(copied_text)
                dialog.open()
            

    def swap_mode(self):
        if self.title_bar_text == "Encryption":
            self.encrypt = False
            self.title_bar_text = "Decryption"

        elif self.title_bar_text == "Decryption":
            self.encrypt = True
            self.title_bar_text = "Encryption"

    def on_button_release(self, button):
        if button.text == "Encrypt":
            message = self.ids.input.text
            key = int(self.ids.my_slider.value)
            output = CeaserCipher.encrypt(key=key, message=message)

            #print(f"Key:{key} \nMessage: {message}")
            self.ids.output.text = output

            # clear input
            #self.ids.input.text = ""

        elif button.text == "Decrypt":
            message = self.ids.input.text
            key = int(self.ids.my_slider.value)
            message = CeaserCipher.decrypt(key=key, message=message)

            #print(f"Key:{key} \nMessage: {message}")
            self.ids.output.text = message

            # clear input
            #self.ids.input.text = ""


# Define the App Class
class EncryptionApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_screen = None

    def on_switch_active(self, switch):
        if switch.active:
            self.theme_cls.theme_style = "Dark"
            self.main_screen.ids.output.hint_text_color_normal = (.6, .6, .6, 1)
            self.main_screen.ids.output.text_color_normal = (.6, .6, .6, 1)
            self.main_screen.ids.output.line_color_normal = (.6, .6, .6, 1)

            self.main_screen.ids.input.hint_text_color_normal = (.6, .6, .6, 1)
            self.main_screen.ids.input.text_color_normal = (.6, .6, .6, 1)
            self.main_screen.ids.input.line_color_normal = (.6, .6, .6, 1)

            self.main_screen.ids.text_mode.theme_text_color = "Hint"

        elif not switch.active:
            self.theme_cls.theme_style = "Light"
            self.main_screen.ids.output.hint_text_color_normal = (.2, .2, .2, 1)
            self.main_screen.ids.output.text_color_normal = (.2, .2, .2, 1)
            self.main_screen.ids.output.line_color_normal = (.2, .2, .2, 1)

            self.main_screen.ids.input.hint_text_color_normal = (.2, .2, .2, 1)
            self.main_screen.ids.input.text_color_normal = (.2, .2, .2, 1)
            self.main_screen.ids.input.line_color_normal = (.2, .2, .2, 1)

            self.main_screen.ids.text_mode.theme_text_color = "Primary"

    def build(self):
        self.icon = "icon.png"
        self.title = "BaTata & MaiTata Encryption App"

        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        self.main_screen = MainScreen()
        return self.main_screen


if __name__ == "__main__":
    app = EncryptionApp()
    app.run()
