import pandas as pd
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    vi_single_questions = pd.read_csv("C:/Users/elliott.lapinel/Downloads/VISPDAT.csv", parse_dates=True, na_values=['nan'])
    entries = pd.read_csv("C:/Users/elliott.lapinel/Downloads/PDR_Detail.csv", parse_dates=True, na_values=['nan'])








# See PyCharm help at https://www.jetbrains.com/help/pycharm/
