from datetime import datetime
from firebase_admin import credentials, db, firestore
import pytz

# Generate the timestamped CSV filename at the start of the script
start_time = datetime.now().strftime("%Y%m%d_%H%M%S")  # Format: YYYYMMDD_HHMMSS
csv_path = f"attendance_{start_time}.csv"

# Create a dictionary to track logged IDs
logged_ids = {}

def log_name(student_id, name, student_unique_id, filename=csv_path):
    if student_id in logged_ids:
        print(f"ID {student_id} has already been logged. Skipping...")
        return

    timezone = pytz.timezone('Africa/Tunis')
    timestamp = datetime.now(timezone).strftime("%B %d, %Y at %I:%M:%S %p UTC+1")

    db = firestore.client()
    doc_ref = db.collection("attendance").document(student_id)

    doc = doc_ref.get()
    if doc.exists:
        existing_data = doc.to_dict()
        timestamps = existing_data.get("timestamps", [])
        timestamps.append(timestamp)
        doc_ref.update({"timestamps": timestamps})
        print(f"Logged ID {student_unique_id}, Name: {name} at {timestamp} (Updated Array)")
    else:
        new_entry = {
            "id": student_unique_id,
            "studentID": student_id,
            "timestamps": [timestamp]
        }
        doc_ref.set(new_entry)
        print(f"Logged ID {student_unique_id}, Name: {name} at {timestamp} (New Entry)")

    logged_ids[student_id] = True
