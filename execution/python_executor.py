import subprocess
import tempfile
import os

from execution.result import ExecutionResult


class PythonExecutor:

    def execute(self, code: str) -> ExecutionResult:

        with tempfile.NamedTemporaryFile(
            suffix=".py",
            delete=False,
            mode="w",
            encoding="utf-8"
        ) as file:

            file.write(code)

            path = file.name

        result = subprocess.run(
            ["python", path],
            capture_output=True,
            text=True
        )

        os.remove(path)

        return ExecutionResult(
            success=result.returncode == 0,
            stdout=result.stdout,
            stderr=result.stderr,
            return_code=result.returncode
        )


executor = PythonExecutor()