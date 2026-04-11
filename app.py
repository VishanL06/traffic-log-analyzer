from flask import Flask, render_template, request
import pandas as pd
import os
from openai import OpenAI

app = Flask(__name__)
client = OpenAI()
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

def analyze_logs(df):
    summary = f"""
    Top actions:
    {df['action'].value_counts().head()}

    Top source IPs:
    {df['source address'].value_counts().head()}
    
    Top destination IPs:
    {df['destination address'].value_counts().head()}

    Denied count:
    {(df['action'] == 'deny').sum()}
    """
    
    prompt = f"""
    You are a cybersecurity analyst reviewing firewall traffic logs.

    Here is a traffic summary:

    {summary}

    Write a concise analysis with these sections:
    1. Overall traffic pattern
    2. Potentially suspicious activity
    3. Anything worth investigating further

    Be specific and avoid vague filler.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


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

                df.columns = df.columns.str.strip().str.lower()
                
                row_count = len(df)
                columns = df.columns.tolist()
                filename = file.filename
                top_actions = df["action"].value_counts().head(5)
                top_source_ips = df["source address"].value_counts().head(5)
                top_dest_ips = df["destination address"].value_counts().head(5)
                denied_count = (df["action"] == "deny").sum()
                ai_analysis = analyze_logs(df)

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
        error=error,
        top_actions=top_actions,
        top_source_ips=top_source_ips,
        top_dest_ips=top_dest_ips,
        denied_count=denied_count,
        ai_analysis=ai_analysis
    )


if __name__ == "__main__":
    app.run(debug=True)