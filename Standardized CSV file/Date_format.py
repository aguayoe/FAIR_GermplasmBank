"""
Master's thesis: Libraries and support tooling for FAIRification of Germplasm databases
Author: Elena Aguayo Jara (elena.aguayo@protonmail.com, elena.aguayo@estudiante.uam.es)
Universidad Autónoma de Madrid - Facultad de Medicina
Center for Plant Biotechnology and Genomics (CBGP-UPM-INIA/CSIC)
Date: 20-03-2024
"""

import pandas as pd

# Download the CSV file
try:
    df = pd.read_csv('base datos aplanada.csv', delimiter=';', skip_blank_lines=False) # The parameter
    """ 'skip_blank_lines=False' is used to specify whether blank lines should
    be treated as missing values or not. When 'skip_blank_lines' is set to 'False',
    it means that blank lines will not be skipped and will be considered as valid data
    during the parsing of the CSV file. 
    """
except pd.errors.ParserError as error:
    print("Error loading CSV file:", error)
   
"""This code is using a 'try-except' block in Python to handle potential errors that may
occur when reading a CSV file using the 'pd.read_csv' function from the pandas library.
"""

def format_date(date_str):
    """The 'format_date' function takes a date string as input and returns a formatted date string in the
    format 'YYYY-MM-DD' or 'XX-XX-XX' based on certain conditions.
    """  

    if pd.isnull(date_str) or date_str == "":  # Check if it is an empty string
        return "XX-XX-XX"
    elif isinstance(date_str, str) and date_str.endswith("----"):  # Check if it is a string and ends with ‘----’.
        return date_str[:4] + "-XX-XX"
        """The code block 'elif "/"' in date_str: is checking if the input date string contains a forward slash
        ("/"). If the condition is true, it implies that the date format is in a specific format that can be
        converted to a standard date format.
        """
    elif "/" in date_str:
        try:
            return pd.to_datetime(date_str, errors='coerce').strftime('%Y-%m-%d')
        except:
            return "XX-XX-XX"
    elif "verano" in date_str:
        return date_str.split("-")[0] + "-XX-XX"
    elif "invierno" in date_str:
        return date_str.split("-")[0] + "-XX-XX"
    elif "otoño" in date_str:
        return date_str.split("-")[0] + "-XX-XX"
    elif "primavera" in date_str:
        return date_str.split("-")[0] + "-XX-XX"
    elif len(date_str) == 4 and date_str.isdigit():
        return date_str + "-XX-XX"

    else:
        parts = date_str.split("-")
        if len(parts) == 3:
            year = parts[0] if parts[0].isdigit() else 'XXXX'
            month = parts[1] if parts[1].isdigit() else 'XX'
            day = 'XX' if parts[2] == '00' else parts[2]
            return f'{year}-{month.zfill(2)}-{day.zfill(2)}'
        else:
            return "XX-XX-XX"

# Apply function to COLLDATE column
df['COLLDATE'] = df['COLLDATE'].apply(format_date)

# Save the updated DataFrame to a new CSV file
df.to_csv('base_datos_formateada.csv', index=False)




















