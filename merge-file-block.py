import os
from helper import find_files
from interpretor import *
from writer import *

cwd = os.getcwd()
dir = cwd
filetype = ".p4d"

# Print and check working directory
print("Your directory is: \'" + dir + "\'")
print("Would you like to change?")
changedir = input("Type \'y' for yes: ")

# Change working directory
if changedir == "y":
    result = "n"
    while result != "y":
        dir = input("Enter the directory: ")
        print("New directory: \'" + dir + "\'")
        print("Is this correct?")
        result = input("Type \'y' for yes: ")
        cwd = dir

# Set name of file output
output = cwd + "\\" + input("Name of output file to create: ") + filetype

# Search dir for *.p4d
projects = find_files(dir, filetype)

# Set first and thereafter projects
p0 = projects[0]
blockProjects = projects[1:]

# Set tags for finding block
openTag = "<images>"
closeTag = "</images>"

# Run function to find tag locations in first project
# insertPoint = find_insert_point(p0, closeTag)
p0_open, p0_close = tag_block(p0, openTag, closeTag)
# Fix p0 to include last line
p0_close += 1

# Empty dicts
project_dictionary = {}

# Create loop to iterate through blockProjects and find blocks
i = 0

for x in blockProjects:
    i += 1
    # Run function to find open and closing tag lines
    openLine, closeLine = tag_block(x, openTag, closeTag)

    project = {}

    addProject = {'Project': i}
    addPath = {'Path': x}
    addOpen = {'Open': openLine}
    addClose = {'Close': closeLine}

    project.update(addProject)
    project.update(addPath)
    project.update(addOpen)
    project.update(addClose)

    dictUpdate = {i: project}
    project_dictionary.update(dictUpdate)

# Write out the start of first project "p0"
write_file_to_line(p0, output, p0_close)

# Iterate through remaining projects
for i in project_dictionary:
    file = project_dictionary[i]['Path']
    open = project_dictionary[i]['Open']
    close = project_dictionary[i]['Close']

    # Append blocks from project in remaining projects to output
    print("Starting project: " + str(i))
    x = write_file_between_lines(file, output, open, close)
    print("Ending project: " + str(i) + " at line: " + str(x))

write_file_from_line(p0, output, p0_close)
