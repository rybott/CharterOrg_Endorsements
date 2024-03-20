import pandas as pd
import os
import duckdb as ddb
import time
from datetime import datetime


School_EIN = input(r"Enter the School EIN in [list, format], or enter the word Excel: ")
if School_EIN == ("Excel").lower():
    folder_path = input("Type in the Path to your Excel: ")
else: 
    School_EIN = [School_EIN]  
    folder_path = pd.DataFrame(School_EIN, columns=["EIN"])
    print(folder_path.info())

