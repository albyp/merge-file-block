# Write list to file at insertion point
def write_list(fileOut, listIn):
    with open(fileOut, "w") as f:
        for x in listIn:
            f.write(x)

# Append lines to a file until a defined line
def write_file_to_line(fileIn, fileOut, endLine):
    stop = endLine - 1

    with open(fileIn, "r") as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            while i <= stop:
                output = open(fileOut, "a")
                output.write(line)
                output.close()
                # print(i)
                i += 1
                break

# Append to a file from a defined line
def write_file_from_line(fileIn, fileOut, startLine):
    with open(fileIn, "r") as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            if i < startLine:
                i += 1
            else:
                output = open(fileOut, "a")
                output.write(line)
                output.close()
                i += 1

# Write to a defined file between start and end lines
def write_file_between_lines(fileIn, fileOut, startLine, endLine):
    with open(fileIn, "r") as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            if i < startLine:
                i += 1
            else:
                while i >= startLine and i <= endLine:
                    output = open(fileOut, "a")
                    output.write(line)
                    output.close()
                    i += 1
                    break
        return i
