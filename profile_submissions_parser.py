import csv
import json
from pathlib import Path

def parse_csv_to_json(csv_file, json_file):
    # Read existing JSON data
    json_path = Path(json_file)
    if json_path.exists():
        with open(json_path, 'r') as jf:
            existing_data = json.load(jf)
    else:
        existing_data = []

    # Read CSV data
    new_entries = []
    with open(csv_file, 'r') as cf:
        csv_reader = csv.DictReader(cf)
        for row in csv_reader:
            # Extract necessary fields and map them to JSON structure
            new_entry = {
                "name": row["Full Name"],
                "color": row.get("What color do you want on your profile? (IN COLOR HEX FORMAT) (green is the default)", ""),
                "team": row.get("What team are you on and what is the name of your team?", ""),
                "role": row.get("What is your role?", ""),
                "school": row.get("What school do you go to?", ""),
                "location": row.get("Where are you located?", ""),
                "member_since": row.get("When did you first join this class?", ""),
                "favorite_thing": row.get("What is the favorite thing in that topic?", ""),
                "main_tasks": row.get("What are your main tasks on your team?", ""),
                "aspired_skill": row.get("What do you want to be?", ""),
                "favorite_thing_at_school": row.get("What is your favorite thing at school?", ""),
                "topic": row.get("Topic of your favorite thing", ""),
                "background_experience": row.get("Give a brief description of your background experience.", "").split(', '),
                "outside_of_work": row.get("What do you do outside of work/school?", "").split(', '),
                "website": "",  # Default as empty since it's not in the CSV
                "linkedin": row.get("Paste your LinkedIn profile url here", ""),
                "github": row.get("Paste your GitHub profile here", ""),
                "image": row.get("Upload your profile picture (It will not be used if it is not a picture of you)", ""),
                "banner": row.get("Upload a banner you would like to use for your profile (Needs to be professional)", ""),
                "subicon": "",  # Default as empty since it's not in the CSV
                "team_icon": "",  # Default as empty since it's not in the CSV
            }
            new_entries.append(new_entry)

    # Merge existing data with new entries
    existing_data.extend(new_entries)

    # Write updated JSON data back to file
    with open(json_path, 'w') as jf:
        json.dump(existing_data, jf, indent=4)

def parse_members_csv_to_json(csv_file, json_file):
    # Read existing JSON data
    json_path = Path(json_file)
    if json_path.exists():
        with open(json_path, 'r') as jf:
            existing_data = json.load(jf)
    else:
        existing_data = []

    # Read CSV data
    new_entries = []
    with open(csv_file, 'r') as cf:
        csv_reader = csv.DictReader(cf)
        for row in csv_reader:
            # Extract necessary fields and map them to JSON structure
            new_entry = {
                "name": row["Full Name"],
                "image": row.get("Upload your profile picture (It will not be used if it is not a picture of you)", ""),
                "linkedin": row.get("Paste your LinkedIn profile url here", ""),
                "github": row.get("Paste your GitHub profile here", ""),
            }
            new_entries.append(new_entry)

    # Merge existing data with new entries
    existing_data.extend(new_entries)

    # Write updated JSON data back to file
    with open(json_path, 'w') as jf:
        json.dump(existing_data, jf, indent=4)

# File paths
profile_csv_file_path = "profile_submissions.csv"
profile_json_file_path = "JSON/profile.json"
members_json_file_path = "JSON/members.json"

# Execute the functions
parse_csv_to_json(profile_csv_file_path, profile_json_file_path)
parse_members_csv_to_json(profile_csv_file_path, members_json_file_path)

print(f"New entries from '{profile_csv_file_path}' have been added to '{profile_json_file_path}'!")
print(f"New entries from '{profile_csv_file_path}' have been added to '{members_json_file_path}'!")
