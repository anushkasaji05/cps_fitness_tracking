import pandas as pd
import os

FILE_PATH = "../input/user.csv"

def sign_up_user(username, password):
    """
    Sign up a new user by adding their credentials to the CSV file.
    
    :param username: The username of the new user.
    :param password: The password of the new user.
    :return: True if the signup is successful, False if the username already exists or invalid input.
    """
    if not username or not password:
        return False  # Invalid input

    # Load the CSV file into a DataFrame
    df = pd.read_csv(FILE_PATH)

    # Check if the username already exists
    if username in df["username"].values:
        return False  # Username already exists

    # Append the new user to the DataFrame and save to CSV
    new_user = pd.DataFrame({"username": [username], "password": [password]})
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)

    return True  # Signup successful

def authenticate_user(username, password):
    """
    Authenticate a user by checking their credentials against the CSV file.
    
    :param username: The username to authenticate.
    :param password: The password to authenticate.
    :return: True if authentication is successful, False otherwise.
    """
    if not username or not password:
        return False  # Invalid input

    # Load the CSV file into a DataFrame
    df = pd.read_csv(FILE_PATH)

    # Check if any row matches the username and password
    return ((df["username"] == username) & (df["password"] == password)).any()
