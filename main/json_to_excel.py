import os
import json
import pandas as pd
from main.init_session import phone
from main.config import Config


source_group_id = Config.source_group_id
path_file = os.path.join(os.getcwd(),"main/data/user") + phone + "_" + str(source_group_id) + '.json'

# Load the JSON file
with open(path_file, 'r') as f:
    data = json.load(f)

# Convert the JSON to a Pandas DataFrame
df = pd.DataFrame.from_dict(data, orient='columns')

df_filtered = df[df['date_online'] == 'online'][['username', 'date_online']]

# Write the DataFrame to an Excel file
df_filtered.to_excel('actions/data.xlsx', index=False)
