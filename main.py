import sys
import pandas as pd


def val_to_min(val):
    mil = int(val) - val
    seconds = int(val)%60
    minutes = int(int(val)/60)
    "12m 1s 321ms"
    return f"{minutes}m {seconds}s {mil}ms"


def add_column(df):
    cname = "Display Time"
    df[cname] = ""
    for idx, row in df.iterrows():
        row[cname] = val_to_min(row["time"])
        df.at[idx, cname] = val_to_min(row["time"])
    df.to_csv("new_data.txt", sep="|", index=False)


def workflow(data_path):
    df = pd.read_csv(data_path, sep="|")
    add_column(df)
    print(f"The new generated file is new_data.csv")


if len(sys.argv) == 2:
    workflow(sys.argv[1])
else:
    print(f"Error: Expects the path to your data file")

