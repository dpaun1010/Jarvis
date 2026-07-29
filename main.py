from desktop import application
from desktop import keyboard
from desktop import mouse
from desktop import screen


print()

print(screen.size())

application.run("notepad")

keyboard.write("Hello from DeepJarvis!")

mouse.click()

screen.screenshot("desktop.png")

print("\nAutomation Completed.")