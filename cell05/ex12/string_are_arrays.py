#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return

    text = sys.argv[1]
    result = ""

    for ch in text:
        if ch == "z":
            result += "z"

    if result == "":
        print("none")
    else:
        print(result)

if __name__ == "__main__":
    main()
