import csv
import os

def read_pet_data(pet_type):
    directory = "data"  # Directory containing the CSV files
    file_name = f"{pet_type}.csv"  # Dynamic file name
    file_path = os.path.join(directory, file_name)  # Combine directory and file name
    
    try:
        with open(file_path, "r") as file:
            print(f"Opened file: {file_path}")  # Debugging line
            reader = csv.DictReader(file)  # Reads CSV file into a dictionary format
            pets = [
                f"{row['name'].strip()} is a {row['age'].strip()} year old {row['breed'].strip()}." 
                for row in reader if row['name'].strip() and row['age'].strip() and row['breed'].strip()
            ]
            
            if pets:
                print("Found pets:")
                for pet in pets:
                    print(pet)
            else:
                print(f"Sorry, we don't have any {pet_type} here.")
    
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
    except KeyError as e:
        print(f"Error: Missing expected column {e} in the CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Get user input
pet_type = input("Enter the type of pet (cats or dogs): ").strip().lower()
read_pet_data(pet_type)
