from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    table = None
    columns = None
    row_count = None
    filename = None
    error = None

    if request.method == "POST":
        file = request.files.get("csv_file")

        if not file or file.filename == "":
            error = "Please choose a CSV file."
        else:
            try:
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(filepath)

                df = pd.read_csv(filepath)

                row_count = len(df)
                columns = df.columns.tolist()
                filename = file.filename

                table = df.head(20).to_html(
                    classes="table table-striped table-bordered",
                    index=False
                )
            except Exception as e:
                error = f"Error reading file: {e}"

    return render_template(
        "index.html",
        table=table,
        columns=columns,
        row_count=row_count,
        filename=filename,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)