from Pattern import Pattern
entries = []
duplicate_entries = []
pattern = Pattern()
todaypath = pattern.getfilepath("bse", 0)
with open(todaypath, 'r') as my_file:
    for line in my_file:
        columns = line.strip().split(',')
        if columns[1] not in entries:
            entries.append(columns[1])
        else:
            duplicate_entries.append(columns[1])
print(duplicate_entries)