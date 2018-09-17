import random
import matplotlib
import matplotlib.pyplot as plt

def rollDice():
    roll = random.randint(1,100)

    if roll == 100:
        return False
    elif roll<=50:
        return False
    elif 100> roll > 50:
        return True

def duble_bettor(funds, inicial_wager, wager_count):
    value = funds
    wager = inicial_wager
    global broke_count
    broke_count = 0

    wX = []
    vY = []

    current_wager = 1
    previous_wager = 'win'
    previour_wager_amount = inicial_wager

    while current_wager <= wager_count:
        if previous_wager == 'win':
            if rollDice():
                value+= wager
                wX.append(current_wager)
                vY.append(value)
            else:
                value-=wager
                previous_wager='loss'
                previour_wager_amount=wager
                wX.append(current_wager)
                vY.append(value)
                if value<0:
                    broke_count += 1
                    break

        elif previous_wager == 'loss':
            if rollDice():
                wager=previour_wager_amount*2
                value+= wager
                wager = inicial_wager
                previous_wager='win'
                wX.append(current_wager)
                vY.append(value)
            else:
                wager = previour_wager_amount*2
                value -= wager
                if value < 0:
                    broke_count+=1
                    break
                previous_wager = 'loss'
                previour_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)

        current_wager +=1

    plt.plot(wX,vY)


def simple_bettor(funds, inicial_wager, wager_count):
    value = funds
    wager = inicial_wager
    global broke_count
    wX = []
    vY = []

    current_wager = 1

    while current_wager <= wager_count:
        if rollDice():
            value += wager
            wX.append(current_wager)
            vY.append(value)
        else:
            value-= wager


        current_wager += 1
    if value<0:
        value='broke'
        broke_count+=1

    plt.plot(wX, vY)


choice = input("select between simple bettor(1) or doubler bettor(2). ")

if choice == '2':
    xx = 0
    while xx < 1000:
        duble_bettor(10000, 100, 10000)
        xx += 1

    print('death rate:', ((broke_count / float(xx)) * 100))
    print('survival rate:', ((100 - ((broke_count / float(xx))) * 100)))
    plt.ylabel('Account Value')
    plt.xlabel('Wager Count')
    plt.axhline(0, color='r')
    plt.show()
elif choice == '1':

    x = 0
    broke_count=0
    while x < 100:
        simple_bettor(10000, 100, 100000)
        x += 1
    print('death rate:', ((broke_count / float(x)) * 100))
    print('survival rate:', ((100 - ((broke_count / float(x))) * 100)))
    plt.axhline(0, color='r')
    plt.ylabel('Account Value')
    plt.xlabel('Wager Count')
    plt.show()


