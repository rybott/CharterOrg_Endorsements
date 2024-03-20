import pandas as pd
import os
import duckdb as ddb
import time
from datetime import datetime

data_990 = None
folder_path = None
#data_990 = r"C:\Users\rybot\OneDrive\Desktop\990filings"
#folder_path = r"C:\Design Folder\RBGithub\CharterOrg_Endorsements\Nonprofit Schools\List of Non profit schools.xlsx"


if folder_path == None:
    School_EIN = input(r"Enter the School EIN in [list, format], or enter the word Excel: ")
    if School_EIN.lower() == ("excel"):
        folder_path = input("Type in the Path to your Excel: ")
        School_List = pd.read_excel(folder_path)
    else: 
        try: 
            School_EIN = [School_EIN]  
            School_List = pd.DataFrame(School_EIN, columns=["EIN"])
        except:
            print("ERROR: EIN numbers must be in the format [No.1,No.2,etc.]")
else: 
    School_List = pd.read_excel(folder_path)

if data_990 == None:
    data_990_folder = input("Insert the Path to the folder with the 990 Data in it: ")
else:
    pass

Name_file = input("Name of the Excel File when finished (with .xlsx): ")

qry = '''
SELECT * 
FROM df
INNER JOIN School_List ON df.EIN = School_List.EIN
'''

Master_df_list = []
sheets = []


# Iterate over the files in the folder
for filename in os.listdir(data_990_folder):
    print("File Printing")
    if filename.endswith('.xlsx'):  # Checks for Excel files (can also use '.xls' for older Excel files)
        sheets.append(filename[:14])
        t1 = datetime.now()
        file_path = os.path.join(data_990_folder, filename)
        df = pd.read_excel(file_path)
        t2 = datetime.now()
        qry_df = ddb.sql(qry).df()
        Master_df_list.append(qry_df)
        time = t2-t1
        print(int(time.total_seconds()))

        break

with pd.ExcelWriter(Name_file) as writer:
    for sheetname, Mdf in zip(sheets,Master_df_list):
        Mdf.to_excel(writer, sheet_name=sheetname, index=True)
