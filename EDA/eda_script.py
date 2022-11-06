import pandas as pd
from pandas_profiling import ProfileReport


if __name__ == "__main__":
    data = pd.read_csv("../data/raw/heart_cleveland_upload.csv")
    report = ProfileReport(data, explorative=True)

    report.to_file("eda_report.html")
