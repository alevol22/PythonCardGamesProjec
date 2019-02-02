import random


class Player(object):
    def __init__(self, name, hand=0):
        self.card_deck = {'Clubs': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'],
                          'Diamonds': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'],
                          'Hearts': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13'],
                          'Spades': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']}
        s1 = [1, 2, 3, 4, 5]
        s2 = [2, 3, 4, 5, 6]
        s3 = [3, 4, 5, 6, 7]
        s4 = [4, 5, 6, 7, 8]
        s5 = [5, 6, 7, 8, 9]
        s6 = [6, 7, 8, 9, 10]
        s7 = [7, 8, 9, 10, 'Jack']
        s8 = [8, 9, 10, 'Jack', 'Queen']
        s9 = [9, 10, 'Jack', 'Queen', 'King']
        s10 = [10, 'Jack', 'Queen', 'King', 'Ace']
        self.straight = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]

        self.name = name
        self.hand = hand
        self.hand = {'Clubs': [], 'Diamonds': [], 'Hearts': [], 'Spades': []}

    def start(self, t):
        for i in range(0, t):
            self.draw()

    def draw(self):
        keys = list(self.card_deck.keys())
        symbol = random.choice(keys)
        cards = list(self.card_deck.get(symbol))
        card = random.choice(cards)
        drawn_card = [symbol, self.get_card_name(card)]
        self.add_to_hand(drawn_card)
        cards.remove(card)
        del(self.card_deck[symbol])
        self.card_deck[symbol] = cards

    def get_card_name(self, card):
        if card == '2' or card == '3' or card == '4' or card == '5' or card == '6' or card == '7' or card == '8' or card == '9' or card == '10':
            return card
        elif card == '1':
            return 'Ace'
        elif card == '11':
            return 'Jack'
        elif card == '12':
            return 'Queen'
        elif card == '13':
            return 'King'

    def add_to_hand(self, new_card):
        symbol = new_card[0]
        number = new_card[1]
        self.hand[str(symbol)].append(number)

    def count_points(self):
        c = self.hand['Clubs']
        d = self.hand['Diamonds']
        h = self.hand['Hearts']
        s = self.hand['Spades']

        all = c + d + h + s
        total = 0

        for card in all:
            if card == '2' or card == '3' or card == '4' or card == '5' or card == '6' or card == '7' or card == '8' or card == '9' or card == '10':
                total += int(card)
            elif card == 'Ace':
                total += 1
            elif card == 'Jack':
                total += 11
            elif card == 'Queen':
                total += 12
            elif card == 'King':
                total += 13

        return total

    def player_status(self):
        points = self.count_points()
        if points == 21:
            return True
        elif points > 21:
            return False
        else:
            return 'True'

    def clear_hand(self):
        self.hand = {'Clubs': [], 'Diamonds': [], 'Hearts': [], 'Spades': []}

    def hand_value_e(self, player):
        self.hand_value = 0
        cards = []
        keys = list(player.hand.keys())
        for k in keys:
            if len(player.hand[k]) == 5:
                for card in player.hand[k]:
                    cards.append(card)
                RF = ['Ace', 'King', 'Queen', 'Jack', '10']
                if cards == RF:
                    self.hand_value = 9
                elif cards in self.straight:
                    # Straight Flush
                    self.hand_value = 8
                else:
                    # flush
                    self.hand_value = 5
            for card in player.hand[k]:
                cards.append(card)

        self.d = {}
        for c in cards:
            self.d[c] = self.d.get(c, 0) + 1

        self.v = list(self.d.values())
        self.k = list(self.d.keys()).sort
        for c in cards:
            if self.d[c] == 4:
                self.hand_value = 7
            elif 3 in self.v and 2 in self.v:
                self.hand_value = 6
            elif self.k in self.straight:
                self.hand_value = 4
            elif 3 in self.v:
                self.hand_value = 3
            elif 2 in self.v:
                self.v.remove(2)
                if 2 in self.v:
                    self.hand_value = 2
                else:
                    self.hand_value = 1

        return self.hand_value

    def hand_name(self, player):
        v = self.hand_value_e(player)

        if v == 9:
            return 'Royal Flush'
        elif v == 8:
            return 'Straight Flush'
        elif v == 7:
            return 'Four of a Kind'
        elif v == 6:
            return 'Full House'
        elif v == 5:
            return 'Flush'
        elif v == 4:
            return 'Mixed Straight'
        elif v == 3:
            return 'Three of a Kind'
        elif v == 2:
            return 'Two Pairs'
        elif v == 1:
            return 'One Pair'
        elif v == 0:
            return 'Nothing Special'
