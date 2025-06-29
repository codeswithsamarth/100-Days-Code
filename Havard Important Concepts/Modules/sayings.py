import sys

from say import hello

if len(sys.argv)==2:
    print(hello(sys.argv[1]))

