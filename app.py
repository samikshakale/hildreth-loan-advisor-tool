from flask import Flask, request, render_template
from statistics_1 import get_recent_complaints_df, get_ordered_series, get_top_issue, get_top_subissue
import numpy as np
import pandas as pd
raw_df = pd.read_csv('complaints-2023-09-13_17_56.csv')
raw_df["Date received"] = pd.to_datetime(raw_df["Date received"])
raw_df = raw_df.reset_index()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    company = request.form['company']
    start_date = request.form['start']
    end_date = request.form['end']
    print(raw_df.head())
    (_, recent_df) = get_recent_complaints_df(start_date, end_date, company, raw_df)
    ordered_df = get_ordered_series(recent_df)
    print(ordered_df.head())
    top_issue = get_top_issue(ordered_df)
    top_subissue = get_top_subissue(ordered_df)
    return render_template('result.html', company=company, start_date=start_date, end_date=end_date, tables=[ordered_df.to_html(classes='data')], titles=ordered_df.columns.values)