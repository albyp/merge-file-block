import os

# Find filetypes within directory and store to list
def find_files(dir, filetype):
    projects = []

    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                projects.append(os.path.join(root, file))
    projects.sort()
    return projects
