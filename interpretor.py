# Find insertion point from file
def find_insert_point(file, lastOccurTag):
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            if lastOccurTag in line:
                insertPoint = lines.index(line)
    return insertPoint

# Find block between tags in file
def tag_block(file, openTag, closeTag):
    openLine = 0
    closeLine = 0

    with open(file, "r") as f:
        #lines = fd.readlines()
        for (i, line) in enumerate(f):
            if openTag in line:
                x = i
                openLine = x + 1
                break
        for (i, line) in enumerate(f):
            if closeTag in line:
                closeLine = i + x
                break
    return openLine, closeLine

# Create list from lines within range
def write_list(file, lines):
    writeListOutput = []
    i = 0
    with open(file, "r") as f:
        for line in f:
            if i in range(lines[0], lines[1]):
                writeListOutput.append(line)
            i += 1
    return writeListOutput
