import pyperclip


class Clipboard:

    def copy(self, text: str):

        pyperclip.copy(text)

    def paste(self):

        return pyperclip.paste()


clipboard = Clipboard()