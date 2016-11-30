
result = ""

for y in range(1, 11):

    for x in range(1, 11):

        if x == y:
            result += "*"
        else:
            result += " "
    result += "\n"

print (result)