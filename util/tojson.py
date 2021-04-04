import json

# Simple utility to read Strings from a file and convert them to json

if __name__ == "__main__":
    import sys
    convert(sys.argv[1])


def convert(input,output):
    with open(input) as f:
        lines = f.readlines()
        res = [line.rstrip() for line in lines]
        names = json.JSONEncoder().encode(res)
    with open(output, "w") as fout:
        fout.write(str(names))