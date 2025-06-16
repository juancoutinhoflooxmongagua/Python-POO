from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-b", "--basic")

args = parser.parse_args()

if args.basic is None:
    print("vc n passou o valor de b")
else:
    print("o valor de b:", args.basic)
