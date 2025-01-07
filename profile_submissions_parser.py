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
                "color": row["What color do you want on your profile? (IN COLOR HEX FORMAT) (green is the default)"],
                "team": row["What team are you on and what is the name of your team?"],
                "role": row["What is your role?"],
                "school": row["What school do you go to?"],
                "location": row["Where are you located?"],
                "member_since": row["When did you first join this class?"],
                "favorite_thing": row["What is the favorite thing in that topic?"],
                "main_tasks": row["What are your main tasks on your team?"],
                "aspired_skill": row["What do you want to be?"],
                "favorite_thing_at_school": row["What is your favorite thing at school?"],
                "topic": row["Topic of your favorite thing"],
                "background_experience": row["Give a brief description of your background experience."].split(', '),
                "outside_of_work": row["What do you do outside of work/school?"].split(', '),
                "website": "",  # Default as empty since it's not in the CSV
                "linkedin": row["Paste your LinkedIn profile url here"],
                "github": row["Paste your GitHub profile here"],
                "image": row["Upload your profile picture (It will not be used if it is not a picture of you)"],
                "banner": row["Upload a banner you would like to use for your profile (Needs to be professional)"],
                "subicon": "",  # Default as empty since it's not in the CSV
                "team_icon": "",  # Default as empty since it's not in the CSV
            }
            new_entries.append(new_entry)

    # Merge existing data with new entries
    existing_data.extend(new_entries)

    # Write updated JSON data back to file
    with open(json_path, 'w') as jf:
        json.dump(existing_data, jf, indent=4)

# File paths
csv_file_path = "profile_submissions.csv"
json_file_path = "JSON/profile.json"

# Execute the function
parse_csv_to_json(csv_file_path, json_file_path)

print(f"New entries from '{csv_file_path}' have been added to '{json_file_path}'!")
