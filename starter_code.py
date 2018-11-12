#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock', 'paper', 'scissors']
"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    previous_move_opp = ""
    previous_move_me = ""

    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        self.previous_move_opp = their_move
        self.previous_move_me = my_move


class RockPlayer(Player):
    def move(self):
        return moves[0]


class RandomPlayer(Player):
    def __init__(self):
        super(RandomPlayer, self).__init__()

    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def __init__(self):
        super(HumanPlayer, self).__init__()

    def move(self):
        input_str = input("rock, paper, scissors ?")
        if input_str == "quit":
            raise Exception("We quit")
        if input_str not in moves:
            raise ValueError('Try Again')
        else:
            return input_str


class ReflectPlayer(Player):
    def __init__(self):
        super(ReflectPlayer, self).__init__()

    def move(self):
        if self.previous_move_opp == "":
            return super(ReflectPlayer, self).move()
        return self.previous_move_opp


class CyclePlayer(Player):
    def __init__(self):
        super(CyclePlayer, self).__init__()

    def move(self):
        if self.previous_move_me == "":
            return super(CyclePlayer, self).move()
        my_index = moves.index(self.previous_move_me)
        return moves[my_index + 1] if my_index + 1 < len(moves) else moves[0]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    count1 = 0
    count2 = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        try:
            move1 = self.p1.move()
            move2 = self.p2.move()
            print(f'You played {move1}  Opponent played {move2}')
            self.p1.learn(move1, move2)
            self.p2.learn(move2, move1)
            return move1, move2
        except ValueError as e:
            raise ValueError('Try Again')

    def play_game_multiple(self):
        round = 0
        while True:
            try:
                print(f"Round {round}:")
                self.play_result()
                round += 1
            except ValueError as e:
                print("Try Again")
                continue
            except Exception as e:
                break
        print(f"\nFinal Score: You {self.count1}, Opponent {self.count2}")
        print("Game over!")

    def play_game_single(self):
        round = 0
        while True:
            try:
                print(f"Round one:")
                self.play_result()
            except ValueError as e:
                print("Try Again")
                continue
            except Exception as e:
                break
            else:
                break
        print("Game over!")

    def play_result(self):
        one, two = self.play_round()
        result = beats(one, two)
        if (result):
            self.count1 += 1
            print("\nYou win!")
        elif(one == two):
            print("\nTied")
        else:
            self.count2 += 1
            print("\nOpponent wins!")
        print("Score: You {}, Opponent {}".format(self.count1, self.count2))


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game_multiple()
