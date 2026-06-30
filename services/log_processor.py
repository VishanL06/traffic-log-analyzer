import pandas as pd

def clean_columns(df):
    df.columns = df.columns.str.strip().str.lower()
    return df


def get_log_stats(df):
    return {
        "row_count": len(df),
        "columns": df.columns.tolist(),
        "top_actions": df["action"].value_counts().head(5),
        "top_source_ips": df["source address"].value_counts().head(5),
        "top_dest_ips": df["destination address"].value_counts().head(5),
        "denied_count": (df["action"] == "deny").sum()
    }


def create_preview_table(df):
    return df.head(20).to_html(
        classes="table table-striped table-bordered",
        index=False
    )