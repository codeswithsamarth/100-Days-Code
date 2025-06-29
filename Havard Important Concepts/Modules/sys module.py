import sys
# try:
#     print("hello,my name is",sys.argv[1])
# except IndexError:
#     print("Index Is Out of Range")

if len(sys.argv)<2:
    sys.exit("To Few Argument")

print("hello,my name is",*sys.argv[1:])

