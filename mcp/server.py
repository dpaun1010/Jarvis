from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


TOOLS = {
    "list_directory": lambda args: {
        "files": []
    },
    "health": lambda args: {
        "status": "ok"
    }
}


@app.get("/tools")
def tools():

    return jsonify(
        list(TOOLS.keys())
    )


@app.post("/execute")
def execute():

    data = request.json

    tool = data["tool"]

    arguments = data.get(
        "arguments",
        {}
    )

    if tool not in TOOLS:

        return jsonify(
            {
                "error": "Unknown tool"
            }
        ), 404

    return jsonify(

        TOOLS[tool](arguments)

    )


@app.get("/health")
def health():

    return jsonify(
        {
            "status": "running"
        }
    )


if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=8000,
        debug=False
    )