import pyautogui


class Mouse:

    def move(self, x: int, y: int):

        pyautogui.moveTo(x, y)

    def click(self):

        pyautogui.click()

    def double_click(self):

        pyautogui.doubleClick()

    def right_click(self):

        pyautogui.rightClick()

    def drag(self, x: int, y: int):

        pyautogui.dragTo(x, y)


mouse = Mouse()