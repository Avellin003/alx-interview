#!/usr/bin/python3

""" Prime number algorithm """


def isWinner(x, nums):
    def sieve(n):
        """ Returns a list of primes up to n"""
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False
        for start in range(2, int(n**0.5) + 1):
            if is_prime[start]:
                for i in range(start * start, n + 1, start):
                    is_prime[i] = False
        return [num for num, prime in enumerate(is_prime) if prime]

    def play_game(n):
        """ Simulates the game for a given n"""
        primes = sieve(n)
        moves = 0  # Count of moves made

        while primes:
            # Maria's move
            if moves % 2 == 0:
                prime = primes.pop(0)
                primes = [p for p in primes if p % prime != 0]
            else:  # Ben's move
                prime = primes.pop(0)
                primes = [p for p in primes if p % prime != 0]
            moves += 1

        return 'Maria' if moves % 2 != 0 else 'Ben'

    # Initialize the win count
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
