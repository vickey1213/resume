import json
import nextpy as xt

# Assuming your JSON file is named 'resume.json' and is in the same directory as the script
json_file_path = "/workspace/nextpy-app-data/app_test/app_test/resume.json"


# Function to load JSON data from a file
def load_json_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


# Load the resume data from JSON file
RESUME_DATA = load_json_data(json_file_path)


# You can define more specific constants if needed, for example:
BASICS = RESUME_DATA["basics"]
WORK_EXPERIENCE = RESUME_DATA["work"]
EDUCATION_HISTORY = RESUME_DATA["education"]
SKILLS = RESUME_DATA["skills"]
PROJECTS = RESUME_DATA["projects"]


def index():
    layout = xt.vstack(
        xt.text(EDUCATION_HISTORY, font_size="2em"),
    )
    return layout


app = xt.App()
app.add_page(index)
