def test(N):
    # write your code in Python 3.6
    num_str = str(N)

    negative = False
    if num_str[0] == "-":
        negative = True
        num_str = num_str[1:]

    print(num_str)
    for reverse_idx, digit in enumerate(reversed(num_str)):
        print(digit)
        if digit == "5":
            print(f"result string before: {num_str}")
            idx = (N - 1) - reverse_idx
            result_str = num_str[:idx] + num_str[idx - 1 :]
            print(f"idx: {idx}")
            print(f"result string after: {result_str}")
            if negative:
                return -int(result_str)
            return int(result_str)


if __name__ == "__main__":
    res = test(-5859)
    print(res)
