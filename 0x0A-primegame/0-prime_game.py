#!/usr/bin/python3
'''Prime Game'''


def isWinner(x, nums):
    '''Finds the winner'''
    winner_count = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        round_winner = isRoundWinner(nums[i], x)
        if round_winner is not None:
            winner_count[round_winner] += 1

    if winner_count['Maria'] > winner_count['Ben']:
        return 'Maria'
    elif winner_count['Ben'] > winner_count['Maria']:
        return 'Ben'
    else:
        return None


def isRoundWinner(n, x):
    '''Find round winner'''
    num_list = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        # Get current player
        current_player = players[i % 2]
        selected_indices = []
        prime = -1
        for idx, num in enumerate(num_list):
            # If already picked a prime number
            # find if num is multiple of the prime number
            if prime != -1:
                if num % prime == 0:
                    selected_indices.append(idx)
            # Else check if num is prime then pick it
            else:
                if isPrime(num):
                    selected_indices.append(idx)
                    prime = num
        # If failed to pick then current player lost
        if prime == -1:
            if current_player == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx, val in enumerate(selected_indices):
                del num_list[val - idx]
    return None


def isPrime(n):
    # 0, 1, even numbers greater than 2 are NOT PRIME
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        # Not prime if divisible by another number less
        # or equal to the square root of itself.
        # n**(1/2) returns square root of n
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                return False
        return True
