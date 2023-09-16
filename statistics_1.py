import numpy as np
import pandas as pd
raw_df = pd.read_csv('complaints-2023-09-13_17_56.csv')
raw_df["Date received"] = pd.to_datetime(raw_df["Date received"])
raw_df = raw_df.reset_index()

def get_recent_complaints_df(start, end, company, df):
  filtered_df = df[df["Company"] == company]
  time_mask = (filtered_df["Date received"] > start) & (filtered_df["Date received"] <= end)
  recent_df = filtered_df[time_mask == True]
  return (filtered_df, recent_df)

def get_ordered_series(df):
  issues_df = df[["index","Issue", "Sub-issue"]]
  issues_df['count'] =1
  grouped_series = issues_df.groupby(["Issue","Sub-issue"])['count'].sum()
  ordered_series = grouped_series.sort_values(ascending=False)
  ordered_df = ordered_series.reset_index()
  return ordered_df

def get_top_issue(ordered_df):
  return ordered_df.iloc[0]["Issue"]

def get_top_subissue(ordered_df):
  return ordered_df.iloc[0]["Sub-issue"]