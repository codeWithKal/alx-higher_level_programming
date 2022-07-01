#!/usr/bin/python3
def infAdd(argv):
    le = len(argv) - 1
    sum = 0
    if le > 0:
        for i in range(1, le + 1):
            sum += int(argv[i])
    print(f"{sum}")


if __name__ == "__main__":
    import sys
    infAdd(sys.argv)
