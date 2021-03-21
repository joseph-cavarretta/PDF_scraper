import pandas as pd
import numpy as np
import tabula
pd.set_option("display.max_rows", None, "display.max_columns", None)

## Set Working Directory
import os
cwd = os.getcwd()

## Set Working Directory
wd = os.chdir(r'') ### Copy in the directory you saved the file to

## Input PDF file name
file = "demo_costar_report.pdf"

## Read tables and convert PDF into csv file
dfs = tabula.convert_into(file, f"{file[:-4]}.csv", output_format="csv", pages='all')

## To convert all files in a folder, use this line
#tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all')

print("File Export Done!")
