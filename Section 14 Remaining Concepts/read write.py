# with open("samarth.txt",'r') as f:
#     contents = f.read()
#     print(contents)
#

with open("samarth.txt",'a') as f:
    lines = ["lines1\n","lines2\n","lines3\n"]
    f.writelines(lines)
