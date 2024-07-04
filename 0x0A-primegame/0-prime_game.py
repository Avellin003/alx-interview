#!/usr/bin/python3
"""Game module"""


def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def calculate_winner(turns, n):
    """Calculate the winner of the game"""
    if turns % 2 == 0:
        return "Maria"
    return "Ben"


def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None

    n = max(nums)

    primes = [False, False] + [True for i in range(n - 1)]
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    scores = [0, 0]
    for i in range(1, n + 1):
        if primes[i]:
            scores[0] += 1
        else:
            scores[1] += 1

    winner = calculate_winner(scores[0], n)
    return winner
