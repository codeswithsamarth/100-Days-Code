# import cowsay
# import sys
#
# if len(sys.argv) == 2:
#     cowsay.cow("hello"+sys.argv[1])
#

def main():
    hello('samarth')
    good_bye('world')

def hello(name):
    print("Hello "+f"{name}")

def good_bye(name):
    print("GoodBye "+f"{name}")

if __name__  == "__main__":
    main()