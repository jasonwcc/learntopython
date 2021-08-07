import argparse
parser = argparse.ArgumentParser(description='Calculation')

parser.add_argument('num1', type=int, help='First number to my calculation')
parser.add_argument('num2', type=int, help='Second number to my calculation')

args = parser.parse_args()

num1 = args.num1
num2 = args.num2

