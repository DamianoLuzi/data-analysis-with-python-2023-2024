#!/Users/Damiano-Luzi/AppData/Roaming/Code/User/globalStorage/moocfi.test-my-code/workspaces/.tmc/.venv/Scripts/python.exe
import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv('src/UK-top40-1964-1-2.tsv', sep='\t')
    print(df)
    existing = df[~df['LW'].isin(['New', 'Re'])]
    print(existing)
    dropped = existing[existing['Pos'] > existing['LW'].astype(int)]
    return dropped

def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
