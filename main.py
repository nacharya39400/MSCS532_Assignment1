from insertion_sort import insertion_sort

def convertInputNumbers(rawString):
    values = []
    for s in rawString:
        try:
            values.append(int(s))
        except ValueError:
            try:
                values.append(float(s))
            except ValueError:
                raise ValueError(f"Not a number: {s!r}")
    return values

def main():
    raw = input("Enter spaceseparated numbers: ").strip().split()
    arr = convertInputNumbers(raw) if raw else []
    print(insertion_sort(arr))

if __name__ == "__main__":
    main()
