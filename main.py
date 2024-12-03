from flask import Flask, request, render_template
from googletrans import LANGCODES
from translate import translate

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        txt_input = request.form["txt_input"]
        translate_to = request.form.get("dest_lang")
        if not translate_to:
            return render_template("index.html", langs=LANGCODES.items(), error="Select a language to translate")
        elif not txt_input:
            return render_template("index.html", langs=LANGCODES.items())

        txt_output = translate(txt_input, translate_to)
        return render_template("index.html", langs=LANGCODES.items(), txt_input=txt_input, txt_output=txt_output)
    else:
        return render_template("index.html", langs=LANGCODES.items())


if __name__ == "__main__":
    app.run(debug=True)
