# . Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками

def card_num(card):
    print('*' * len(card[:-4]) + card[-4:])

card_num("456986445574563214")


