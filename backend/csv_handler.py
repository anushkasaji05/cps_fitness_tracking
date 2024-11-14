import pandas as pd
import os
# File path for the CSV file
FILE_PATH = 'input/data.csv'

def insert_record(record):
    """
    Inserts a record into the CSV file if all fields are present.
    
    :param record: Dictionary with keys: username, date, weight, sleep, water, activity, workout_duration
    :return: True if the record is inserted successfully, False otherwise
    """
    required_fields = ['username', 'date', 'weight', 'sleep', 'water', 'activity', 'workout_duration']
    
    # Check if all fields are present in the record
    if not all(field in record and record[field] for field in required_fields):
        return False

    # Load the CSV file
    if os.stat(FILE_PATH).st_size == 0:
        # Initialize an empty DataFrame with the required columns
        df = pd.DataFrame(columns=required_fields)
    else :
        df = pd.read_csv(FILE_PATH)

    # Append the new record
    df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)
    
    # Save the updated DataFrame to the CSV file
    df.to_csv(FILE_PATH, index=False)
    return True

def update_record(record):
    """
    Updates a record in the CSV file based on username and date.
    
    :param record: Dictionary with keys: username, date, weight, sleep, water, activity, workout_duration
    :return: True if the record is updated successfully, False otherwise
    """
    required_fields = ['username', 'date', 'weight', 'sleep', 'water', 'activity', 'workout_duration']
    
    if not all(field in record for field in required_fields):
        return False

    try:
        df = pd.read_csv(FILE_PATH)
    except FileNotFoundError:
        return False

    # Check if the record exists
    mask = (df['username'] == record['username']) & (df['date'] == record['date'])
    if not mask.any():
        return False

    # Update the record
    df.loc[mask, :] = list(record.values())
    
    # Save the updated DataFrame to the CSV file
    df.to_csv(FILE_PATH, index=False)
    return True

def delete_record(username, date):
    """
    Deletes a record from the CSV file based on username and date.
    
    :param username: Username of the record to delete
    :param date: Date of the record to delete
    :return: True if the record is deleted successfully, False otherwise
    """
    
    try:
        df = pd.read_csv(FILE_PATH)
    except FileNotFoundError:
        return False
    

    # Filter out the record to delete
    initial_length = len(df)
    df = df[~((df['username'] == username) & (df['date'] == date))]

    # Check if any record was deleted
    if len(df) == initial_length:
        return False

    # Save the updated DataFrame to the CSV file
    df.to_csv(FILE_PATH, index=False)
    return True

def read_activity(username, activity):
    try:
        # Read the CSV file
        df = pd.read_csv(FILE_PATH)
        
        # Check if the required columns exist
        required_columns = {'username', 'activity', 'weight', 'workout_duration'}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"The CSV file must contain the columns: {required_columns}")
        
        # Filter rows matching the specified username and activity
        filtered_df = df[(df['username'] == username) & (df['activity'] == activity)]
        
        # Extract weight and workout_duration values into lists
        weight_values = filtered_df['weight'].tolist()
        workout_duration_values = filtered_df['workout_duration'].tolist()
        
        # Return the nested list
        return [weight_values, workout_duration_values]
    
    except FileNotFoundError:
        print(f"Error: The file {FILE_PATH} does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []



