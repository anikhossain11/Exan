import csv
import os  # File existence চেক করার জন্য

class FileHandler:
    @staticmethod
    def save_to_file(filename, contacts):
        try:
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Email", "Phone", "Address"])
                for phone, details in contacts.items():
                    writer.writerow([details["Name"], details["Email"], phone, details["Address"]])
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving to file: {e}")

    @staticmethod
    def load_from_file(filename):
        # Check if the file exists; if not, create an empty file
        if not os.path.exists(filename):
            print(f"{filename} not found. Creating a new file...")
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Email", "Phone", "Address"])  # Write headers

        # Load data from file
        try:
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                return {row["Phone"]: {"Name": row["Name"], "Email": row["Email"], "Address": row["Address"]}
                        for row in reader}
        except Exception as e:
            print(f"Error loading file: {e}")
            return {}
