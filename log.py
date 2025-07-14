s = "this is hello world  -bad code"
print(s)
parts = s.split('-', 1)  # split into 2 parts at first '-'

if len(parts) == 2:
    print(parts[0].strip())  # print before '-', trimmed
    print(parts[1].strip())  # print after '-', trimmed
else:
    print(s)  # no '-' found, print whole string
