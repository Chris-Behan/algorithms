def coin_change_recursive(coins: list[int], amount: int):
    if amount == 0:
        return 0

    if amount < 0:
        return float("inf")

    min_coins = float("inf")
    for denomination in coins:
        sub_problem = coin_change_recursive(coins=coins, amount=amount - denomination)
        min_coins = min(min_coins, sub_problem + 1)
    return min_coins


def coin_change_dynamic(coins: list[int], amount: int):
    # Initialize list where index is the amount and the int at that index is the minimum number
    # of coins that can be used to sum to that amount. Infinite will be used to represent amounts
    # that cannot be made up with the denominations of coins we have.
    coin_counts = [float("inf") for _ in range(amount + 1)]
    # zero coins of any positive denomination makes 0
    coin_counts[0] = 0

    for num in range(1, amount + 1):
        for denomination in coins:
            if num >= denomination:
                coin_counts[num] = min(
                    coin_counts[num], coin_counts[num - denomination] + 1
                )

    if coin_counts[-1] == float("inf"):
        return -1
    return coin_counts[-1]


# coins = [1,2,5]
# amount = 11

# r_ans = coin_change_recursive(coins, amount)
# dp_ans = coin_change_dynamic(coins, amount)
# print(f"Recursive answer: {r_ans}")
# print(f"Dynamic Programming answer: {dp_ans}")


def longest_palindromic_substring_brute_force(s: str):
    longest_palindrome = ""
    for start in range(len(s)):
        for end in range(
            start, len(s) + 1
        ):  # goes to len(s) + 1 since end is used as the non-inclusive end index
            partial = s[start:end]
            if partial == partial[::-1]:
                longest_palindrome = (
                    s[start:end]
                    if len(s[start:end]) > len(longest_palindrome)
                    else longest_palindrome
                )
    return longest_palindrome


ans = longest_palindromic_substring_brute_force("abccbad")
print(ans)


def longest_palindromic_substring_dp(s: str):
    length = len(s)
    memo = [[False for _ in range(length)] for _ in range(length)]
    # Populate memo with palindromes of length 1
    for i in range(length):
        memo[i][i] = True
        ans = (i, i)

    # Populate memo with palindromes of length 2
    for i in range(length - 1):
        if s[i] == s[i + 1]:
            memo[i][i + 1] = True
            ans = (i, i + 1)
    # Populate memo with palindromes of length 3 to n.
    # A substring that's a palindrome of length 3 is a substring in which the current index is the
    # same as the current index + 2, we will call this j, and the string from i + 1 to j -1 was also
    # a palindrome.
    # If we start by checking all palindromes of length 3, then 4, then 5, and so on,
    # the i + 1 and j -1 will always be populated.
    for diff in range(2, length):
        for i in range(length - diff):
            j = i + diff
            if s[i] == s[j] and memo[i + 1][j - 1]:
                memo[i][j] = True
                ans = (i, j)

    return s[ans[0] : ans[1] + 1]


ans2 = longest_palindromic_substring_dp("aabaa")
print(ans2)
