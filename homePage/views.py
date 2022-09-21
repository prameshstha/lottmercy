from random import random, randint, shuffle, sample

import json
from django.shortcuts import render

# Create your views here.
from homePage.models import GameNumber, UserDetails


def HomePage(request):
    print("homepage is here")
    template = 'home.html'
    context = {'a': 'success homepage'}
    return render(request, template, context)


def BuyTicket(request):
    print("buyticket")
    template = 'buyTickTest.html'
    winningNumShuffle, pwBall, pArray, numbArray = winningNumber()
    context = {
        'b': 'ticket found here',
        'numbArray': numbArray,
        'pArray': pArray,
        'winningNumShuffle': winningNumShuffle,
        'pwBall': pwBall,
    }

    return render(request, template, context)


def BuyTicketStore(request):
    print("BuyTicketStore")
    gameNumbers = []
    #
    # print(request.POST)
    # print(request.POST['1gameNumber2'])

    ticketCount = int(request.POST['tickNumbers'])
    print(ticketCount)
    for i in range(1, ticketCount + 1):
        g = []
        j = 1
        # print(i)
        # print("done")
        for j in range(1, 8):
            g.append((request.POST[str(i) + 'gameNumber' + str(j)]))
            # print(j)
        g.append((request.POST['powerBall' + str(i)]))
        gameNumbers.append(g)

    print(gameNumbers, 'game numbers')
    # array to json
    # print(json.dumps(gameNumbers), 'json')
    myJsonString = json.dumps(gameNumbers)

    # a = gameNumbers[1]
    # print(a[7])
    # store = GameNumber(user_game=myJsonString, current_user_id=1)
    # store.save()

    winnNum = winningNumber()
    print("here", winnNum[0], winnNum[1], "winnnnnnn")

    value = GameNumber.objects.get(current_user_id=1)
    # print(value, 'value')
    choosenGameNumber = value.user_game
    # print(choosenGameNumber[1], 'number chosen')
    # json to array
    op = json.loads(choosenGameNumber)
    # print('choose', op, "haha", op[1])
    # Winpw = (op[1])[7]
    # print(len(op), Winpw)
    # print(op[1].pop(), 'pop', op)

    # numpy
    import numpy as np
    # num = np.array(op[1])
    # num1 = np.array(winnNum[0])
    # print(num, 'nummm', num1)

    for p in range(0, len(op)):
        print(p, 'p')
        pwNumOnly = op[p].pop()
        print(pwNumOnly, 'pb', winnNum[1], 'anowd', op[p])
        c = np.intersect1d(op[p], winnNum[0])
        print(c, 'ccccccccccccccc', p, len(c))
        if len(c) == 7 and pwNumOnly == winnNum[1]:
            print('Congratulation!! You won FIRST prize.')
        elif len(c) == 7:
            print('Congratulation!! You won SECOND prize.')
        elif len(c) == 6 and pwNumOnly == winnNum[1]:
            print('Congratulation!! You won THIRD prize.')
        elif len(c) == 6:
            print('Congratulation!! You won FOURTH prize.')
        elif len(c) == 5 and pwNumOnly == winnNum[1]:
            print('Congratulation!! You won FIFTH prize.')
        elif len(c) == 4 and pwNumOnly == winnNum[1]:
            print('Congratulation!! You won SIXTH prize.')
        elif len(c) == 5:
            print('Congratulation!! You won SEVENTH prize.')
        elif len(c) == 3 and pwNumOnly == winnNum[1]:
            print('Congratulation!! You won EIGHTH prize.')
        elif len(c) == 2 and pwNumOnly == winnNum[1]:
            print('Congratulation!! You won NINTH prize.')
        # elif len(c) >= 2:
        #     print('Nearly missed. Sorry No prize')
        else:
            print('Sorry!! No prize won today. Please try again')
    return render(request, template_name="home.html")


# function for winning number

def winningNumber():
    numbers = range(1, 36)
    numbArray = []
    for i in numbers:
        # print(i)
        numbArray.append(i)
    # print(numbArray)
    # print(numbers)
    p = range(1, 21)
    pArray = []
    for i in p:
        pArray.append(i)

    ### test for combination start
    # Import itertools package
    from itertools import combinations

    # Getting all combination of a particular length.
    combi = combinations(numbArray, 7)
    pwBall = randint(1, 20)
    # print(pwBall, "power ball")

    # Print the list of combinations
    randomPosition = randint(0, 6724520)
    # print(randomPosition)
    winningNumber = list(combi)[randomPosition]
    # print(list(winningNumber), "list", winningNumber[2])

    winningNumShuffle = sample(list(winningNumber), 7)
    # print(winningNumShuffle, pwBall)

    ### ### test for combination end

    return winningNumShuffle, pwBall, pArray, numbArray
