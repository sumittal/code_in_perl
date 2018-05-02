man = []
other = []

try:
    data = open('oops.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError as err:
    print("file error: ", str(err))

print(man)
print(other)

try:
    md = open("man_data.txt", "w")
    od = open("other_data.txt", "w")

    print(man, file=md)
    print(other, file=od)

except IOError:
    print("File error")

finally:
    if md in locals():
        md.close()

    if od in locals():
    od.close()
