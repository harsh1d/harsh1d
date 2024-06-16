import pickle

# Function to serialize data and save to a .pkl file
def save_data_to_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

# Function to deserialize data from a .pkl file
def load_data_from_pickle(filename):
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    return data

# Example usage:
# Suppose we have a text file 'data.txt' containing some text data
text_data_filename = 'data.txt'
pickle_filename = 'data.pkl'
import pickle

# Function to serialize data and save to a .pkl file
def save_data_to_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

# Function to deserialize data from a .pkl file
def load_data_from_pickle(filename):
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    return data

# Example usage:
# Suppose we have a text file 'data.txt' containing some text data
text_data_filename = 'data.txt'
pickle_filename = 'data.pkl'

# Read from the text file
# Read from the text file using 'with' statement to ensure proper file handling
try:
    with open(text_data_filename, 'r', encoding='utf-8') as file:
        text_data = file.read()
        # Save text data to pickle file
        save_data_to_pickle(text_data, pickle_filename)
except FileNotFoundError:
    print(f"The file {text_data_filename} does not exist.")
except IOError:
    print(f"An error occurred while reading the file {text_data_filename}.")

# Load data from pickle file (to demonstrate deserialization)
import pickle

# Function to serialize data and save to a .pkl file
def save_data_to_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

# Function to deserialize data from a .pkl file
def load_data_from_pickle(filename):
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    return data

# Example usage:
# Suppose we have a text file 'data.txt' containing some text data
text_data_filename = 'data.txt'
pickle_filename = 'data.pkl'

# Read from the text file
# Read from the text file using 'with' statement to ensure proper file handling
try:
    with open(text_data_filename, 'r', encoding='utf-8') as file:
        text_data = file.read()
        # Save text data to pickle file
        save_data_to_pickle(text_data, pickle_filename)
except FileNotFoundError:
    print(f"The file {text_data_filename} does not exist.")
except IOError:
    print(f"An error occurred while reading the file {text_data_filename}.")

# Load data from pickle file (to demonstrate deserialization)
loaded_data = load_data_from_pickle(pickle_filename)
print(loaded_data)  # Should print the content of the original text file
loaded_data = load_data_from_pickle(pickle_filename)
print(loaded_data)  # Should print the content of the original text file

# Read from the text file
# Read from the text file using 'with' statement to ensure proper file handling
try:
    with open(text_data_filename, 'r', encoding='utf-8') as file:
        text_data = file.read()
except FileNotFoundError:
    print(f"The file {text_data_filename} does not exist.")
except IOError:
    print(f"An error occurred while reading the file {text_data_filename}.")
# The rest of the code remains unchanged.
    text_data = file.read()

# Save text data to pickle file
save_data_to_pickle(text_data, pickle_filename)

# Load data from pickle file (to demonstrate deserialization)
loaded_data = load_data_from_pickle(pickle_filename)
print(loaded_data)  # Should print the content of the original text file