from flask import Flask, render_template, request
import pandas as pd
import os

from config import UPLOAD_FOLDER, MAX_CONTENT_LENGTH
from services.log_processor import clean_columns, get_log_stats, create_preview_table
from services.ai_analyze import analyze_logs


app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    table = None
    columns = None
    row_count = None
    filename = None
    error = None
    top_actions = None
    top_source_ips = None
    top_dest_ips = None
    denied_count = None
    ai_analysis = None

    if request.method == "POST":
        file = request.files.get("csv_file")

        if not file or file.filename == "":
            error = "Please choose a CSV file."
        else:
            try:
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(filepath)

                df = pd.read_csv(filepath)
                df = clean_columns(df)

                stats = get_log_stats(df)

                row_count = stats["row_count"]
                columns = stats["columns"]
                top_actions = stats["top_actions"]
                top_source_ips = stats["top_source_ips"]
                top_dest_ips = stats["top_dest_ips"]
                denied_count = stats["denied_count"]

                filename = file.filename
                ai_analysis = analyze_logs(df)
                table = create_preview_table(df)

            except Exception as e:
                error = f"Error reading file: {e}"

    return render_template(
        "index.html",
        table=table,
        columns=columns,
        row_count=row_count,
        filename=filename,
        error=error,
        top_actions=top_actions,
        top_source_ips=top_source_ips,
        top_dest_ips=top_dest_ips,
        denied_count=denied_count,
        ai_analysis=ai_analysis
    )


if __name__ == "__main__":
    app.run(debug=True)