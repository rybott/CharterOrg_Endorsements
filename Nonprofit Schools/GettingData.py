import pandas as pd
import os
import duckdb as ddb
import time
from datetime import datetime



# The path to the directory containing your Excel files
folder_path = r'C:\Users\rybot\OneDrive\Desktop\990filings'

School_List = pd.read_excel(r"C:\Design Folder\RBGithub\CharterOrg_Endorsements\Nonprofit Schools\List of Non profit schools.xlsx")

qry = '''
SELECT * 
FROM df
INNER JOIN School_List ON df.EIN = School_List.EIN
'''

Master_df_list = []
sheets = []

# Iterate over the files in the folder
for filename in os.listdir(folder_path):
    print("File Printing")
    if filename.endswith('.xlsx'):  # Checks for Excel files (can also use '.xls' for older Excel files)
        sheets.append(filename[:14])
        t1 = datetime.now()
        file_path = os.path.join(folder_path, filename)
        df = pd.read_excel(file_path)
        t2 = datetime.now()
        qry_df = ddb.sql(qry).df()
        Master_df_list.append(qry_df)
        # Master_df = pd.concat([Master_df,qry_df], ignore_index=True)
        time = t2-t1
        print(int(time.total_seconds()))

with pd.ExcelWriter('Qryed_SchoolData2.xlsx') as writer:
    for sheetname, Mdf in zip(sheets,Master_df_list):
        Mdf.to_excel(writer, sheet_name=sheetname, index=True)
