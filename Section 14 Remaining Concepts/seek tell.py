# with open('file.txt','a') as f:
#     f.seek(10)
#     data = "Samarth is very good boy"
#     f.write(data)
# print(data)

with open('file.txt','r') as f:
    # f.write("Hello World")
    # f.truncate(6)
    data = f.read()
    print(data)