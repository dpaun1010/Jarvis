import subprocess

from execution.result import ExecutionResult


class ShellExecutor:

    def execute(self, command: str) -> ExecutionResult:

        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        return ExecutionResult(
            success=result.returncode == 0,
            stdout=result.stdout,
            stderr=result.stderr,
            return_code=result.returncode
        )


executor = ShellExecutor()