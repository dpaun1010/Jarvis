import subprocess
from pathlib import Path


class SandboxExecutor:

    def run(
        self,
        command,
        cwd,
        timeout=300,
    ):

        result = subprocess.run(
            command,
            cwd=Path(cwd),
            capture_output=True,
            text=True,
            timeout=timeout,
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
        }


executor = SandboxExecutor()