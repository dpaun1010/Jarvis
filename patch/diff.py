import difflib


class DiffGenerator:

    def generate(
        self,
        old,
        new,
        filename,
    ):

        return "".join(

            difflib.unified_diff(

                old.splitlines(True),

                new.splitlines(True),

                fromfile=filename,

                tofile=filename,

            )

        )


diff_generator = DiffGenerator()