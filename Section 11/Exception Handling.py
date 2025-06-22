
try:
    f = open("Samarth.txt",'w')
    content = "Samarth is very nice guy"
    f.write(content)
    print(content)
    f.close()
except FileNotFoundError:
    print("The File Does Not exists")