import re
import os
import pandas as pd

excel_path = os.path.join(os.getcwd(),"current_data.xlsx")
excel_data = pd.read_excel(excel_path, sheet_name='Sheet1')

# Convert DataFrame to list
excel_data_list = excel_data.values.tolist()

# Convert list to string
excel_data_str = str(excel_data_list)

# Pattern to match usernames beginning with @
pattern = r'@\w+'

# Find all matches in the string
matches = re.findall(pattern, excel_data_str)
print(matches)
# Create a new DataFrame from the list of matches
df = pd.DataFrame({'Usernames': matches})

# Write the DataFrame to an Excel file
df.to_excel('usernames.xlsx', index=False)