from random import choice

ENTER_NUMBER = 'Enter the number of friends joining (including you):'
ENTER_FRIENDS = 'Enter the name of every friend (including you), each on a new line:'
INVALID_NUMBER = 'No one is joining for the party'
ENTER_BILL = 'Enter the total bill value:'
LUCKY_QUESTION = 'Do you want to use the "Who is lucky?" feature? Write Yes/No:'
LUCKY_FRIEND = ' is the lucky one!'
LUCKY_DENIED = 'No one is going to be lucky'


print(ENTER_NUMBER)
friends_amount = int(input())
if friends_amount > 0:
    friend_dict = {}
    print(ENTER_FRIENDS)
    for _ in range(1, friends_amount + 1):
        friend_dict[input()] = 0
    print(ENTER_BILL)
    bill = int(input())
    bill_each = round(bill / friends_amount, 2)
    for friend in friend_dict:
        friend_dict.update({friend: bill_each})
    print(LUCKY_QUESTION)
    if input() == 'Yes':
        lucky = choice(list(friend_dict.keys()))
        print(lucky + LUCKY_FRIEND)
        bill_each = round(bill / (friends_amount - 1), 2)
        for friend in friend_dict:
            if friend != lucky:
                friend_dict.update({friend: bill_each})
            elif friend == lucky:
                friend_dict.update({friend: 0})
    else:
        print(LUCKY_DENIED)
    print(friend_dict)
else:
    print(INVALID_NUMBER)
