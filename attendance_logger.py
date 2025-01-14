# import csv
from datetime import datetime
from firebase_admin import credentials, db,firestore
import pytz

# Generate the timestamped CSV filename at the start of the script
start_time = datetime.now().strftime("%Y%m%d_%H%M%S")  # Format: YYYYMMDD_HHMMSS
csv_path = f"attendance_{start_time}.csv"

# Create a set to track logged names
logged_names = set()


def log_name(name, filename=csv_path):
    # If the name has already been logged, skip logging it again
    if name in logged_names:
        print(f"Name {name} has already been logged. Skipping...")
        return

    # Generate a timestamp
    # timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Generate a timestamp with the desired format
    timezone = pytz.timezone('Africa/Tunis')  # Set timezone to UTC+1 (Tunisia time)
    timestamp = datetime.now(timezone).strftime("%B %d, %Y at %I:%M:%S %p UTC+1")
    # Add the data to Firebase Firestore
    db = firestore.client()  # Create Firestore client
    doc_ref = db.collection("attendance").document(name)  # Reference to the "attendance" collection

    # Check if the student document exists
    doc = doc_ref.get()

    if doc.exists:
        # If the document exists, append the new timestamp to the array
        existing_data = doc.to_dict()
        timestamps = existing_data.get("timestamps", [])  # Get the existing timestamps array, or an empty list
        timestamps.append(timestamp)
        doc_ref.update({"timestamps": timestamps})  # Update the document with the new timestamp
        print(f"Logged {name} at {timestamp} in Firestore (Updated Array)")

    else:
        # If the document doesn't exist, create a new document with the first timestamp
        new_entry = {
            "name": name,
            "timestamps": [timestamp]  # Store timestamps as an array
        }
        doc_ref.set(new_entry)  # Set the document (like a row in a table)
        print(f"Logged {name} at {timestamp} in Firestore (New Entry)")

    # Mark this name as logged
    logged_names.add(name)
