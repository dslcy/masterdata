# Import the packages
import pandas as pd
from datetime import datetime

# Upload the user_activity_data CSV file
df = pd.read_csv('user_activity_data.csv')

# Remove rows where:
new_df = (df
          .dropna(axis=0, how='all')  # rows are entirely empty  
          .dropna(subset=['user_id'])  # user_id column is NaN          
          .dropna(subset=['timestamp'])  # timestamp column is NaN                 
          .dropna(subset=['activity_type']))  # activity_type column is NaN                 

# Drop duplicates
new_df = new_df.drop_duplicates()    

# Parse the timestamp column into a proper datetime format
new_df['timestamp'] = pd.to_datetime(new_df['timestamp'])

# Change other data types for better performance
new_df['user_id'] = new_df['user_id'].astype(int)
new_df['activity_type'] = new_df['activity_type'].astype('category')

# Create a new column that shows how many activities a user has performed
new_df['count_of_activities'] = new_df.groupby('user_id')['user_id'].transform('size')

# Make sure the index is in order
# print(new_df.index)

# Make sure each event follows the correct logic:
# sorted_df = new_df.sort_values(by=['user_id', 'timestamp'])
# print(sorted_df)

# Save the cleaned and transformed data
new_df.to_csv('cleaned_user_activity_data.csv', index=False)
