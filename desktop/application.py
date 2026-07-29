import os
import subprocess


class ApplicationManager:

    def open(self, application: str):

        os.startfile(application)

    def run(self, command: str):

        subprocess.Popen(command, shell=True)

    def close(self, process: str):

        subprocess.run(
            f"taskkill /IM {process} /F",
            shell=True
        )


manager = ApplicationManager()