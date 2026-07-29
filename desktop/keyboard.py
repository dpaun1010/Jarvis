import pyautogui


class Keyboard:

    def write(self, text: str):

        pyautogui.write(
            text,
            interval=0.02
        )

    def press(self, key: str):

        pyautogui.press(key)

    def hotkey(self, *keys):

        pyautogui.hotkey(*keys)


keyboard = Keyboard()