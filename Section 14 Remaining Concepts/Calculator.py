# import argparse
#
# Calculator = argparse.ArgumentParser(description="Simple Calculator")
# Calculator.add_argument("num1",type=float,help="First Number")
# Calculator.add_argument("num2",type=float,help="Second Number")
# Calculator.add_argument("Operation",choices=['add','sub','mul','div'],help="Enter Operator")
#
# args = Calculator.parse_args()
#
# if (args.Operation == "add"):
#     print(f"The result is equal to {args.num1+args.num2}")
# elif (args.Operation == "sub"):
#     print(f"The result is equal to {args.num1-args.num2}")
# elif (args.Operation == "mul"):
#     print(f"The result is equal to {args.num1*args.num2}")
# elif (args.Operation == "div"):
#     if args.num2 == 0:
#         print("Cant Divide by zero")
#     else:
#         print(f"The result is equal to {args.num1/args.num2}")

import argparse

Calculator = argparse.ArgumentParser(description="Simple Calculator")
Calculator.add_argument("num1",type=float,help="First Number")
Calculator.add_argument("num2",type=float,help="Second Number")
Calculator.add_argument("Operation",choices=['add','sub','mul','div'],help="Enter Operator")

args = Calculator.parse_args()

if (args.Operation == "add"):
    print(f"The result is equal to {args.num1+args.num2}")
elif (args.Operation == "sub"):
    print(f"The result is equal to {args.num1-args.num2}")
elif (args.Operation == "mul"):
    print(f"The result is equal to {args.num1*args.num2}")
elif (args.Operation == "div"):
    if args.num2 == 0:
        print("Cant Divide by zero")
    else:
        print(f"The result is equal to {args.num1/args.num2}")

