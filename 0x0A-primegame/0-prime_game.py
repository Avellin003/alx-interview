#!/usr/bin/python3
'''game module'''


def isWinner(x, nums):
    '''gets the winner'''
    winnerC = {'Maria': 0, 'Ben': 0}

    for i in range(x):
        roundW = RoundW(nums[i], x)
        if roundW is not None:
            winnerC[roundW] += 1

    if winnerC['Maria'] > winnerC['Ben']:
        return 'Maria'
    elif winnerC['Ben'] > winnerC['Maria']:
        return 'Ben'
    else:
        return None


def RoundW(n, x):
    '''RoundW'''
    list = [i for i in range(1, n + 1)]
    players = ['Maria', 'Ben']

    for i in range(n):
        currentPlayer = players[i % 2]
        selectedIdxs = []
        prime = -1
        for idx, num in enumerate(list):
            if prime != -1:
                if num % prime == 0:
                    selectedIdxs.append(idx)
            else:
                if Prime(num):
                    selectedIdxs.append(idx)
                    prime = num
        if prime == -1:
            if currentPlayer == players[0]:
                return players[1]
            else:
                return players[0]
        else:
            for idx, val in enumerate(selectedIdxs):
                del list[val - idx]
    return None


def Prime(n):
    if n == 1 or n == 0 or (n % 2 == 0 and n > 2):
        return False
    else:
        for i in range(3, int(n**(1/2))+1, 2):
            if n % i == 0:
                return "Not prime"
        return True
