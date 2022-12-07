import pandas as pd


def cut_combinations():
    with open('combinations_import.csv', 'r') as f_in, open('combinations_sample.csv', 'w+') as f_out:
        df = pd.read_csv(f_in, sep=';', nrows=100)
        df.to_csv(f_out, sep=';', index=False)
