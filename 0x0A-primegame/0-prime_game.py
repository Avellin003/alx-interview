#!/usr/bin/python3

""" Prime number algorithm """


def isWinner(x, nums):
    """function that perfroms the algorithm"""
    if x < 1 or not nums:
        return None

    def sieve(n):
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
        return prime_numbers

    max_n = max(nums)
    prime_numbers = sieve(max_n)

    def play_game(n):
        remaining = set(range(1, n + 1))
        turn = 0  # Maria starts, 0 for Maria, 1 for Ben
        while True:
            move_made = False
            for prime in prime_numbers:
                if prime in remaining:
                    multiples = set(range(prime, n + 1, prime))
                    remaining -= multiples
                    move_made = True
                    break
            if not move_made:
                return "Ben" if turn == 0 else "Maria"
            turn = 1 - turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
