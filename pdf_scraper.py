import pandas as pd
import tabula
pd.set_option("display.max_rows", None, "display.max_columns", None)

## Input PDF file name
file = "demo_costar_report.pdf"

## Read tables and convert PDF into csv file
tabula.convert_into(file, f"{file[:-4]}.csv", output_format="csv", pages='all')

## To convert all files in a folder, use this line
#tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all')

print("File Export Done!")
