import pyautogui


class Screen:

    def screenshot(self, path: str):

        image = pyautogui.screenshot()

        image.save(path)

        return path

    def size(self):

        return pyautogui.size()


screen = Screen()