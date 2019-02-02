'''
welcome screen: title of games, start buttons, optional: amount of players
    code: labels, maybe radio
'''
import tkinter

from CardGame.Objects import Player
from CardGame.Welcome_Screen import CardGameWelcomeScreen
from CardGame.Black_Jack import BlackJackScreen
from CardGame.BJ_Results import BJResultsScreen
from CardGame.Poker import PokerScreen
from CardGame.Poker_Results import PokerResultsScreen


class CardGameMain(object):

    def __init__(self):

        self.root = tkinter.Tk()

    def setup_game_welcome(self):
        self.root.title("Welcome to Card Games!")
        self.game_wel = CardGameWelcomeScreen(self.root, self.onclose_game_welcome)

    def onclose_game_welcome(self, char_name, game_choice):

        char_name = str(char_name)
        game_choice = str(game_choice)

        # Saves players name choice
        self.player = Player(char_name)
        self.computer = Player('Computer')

        # Destroys the "Game welcome" frame
        self.game_wel.destroy()

        if game_choice == 'Black Jack':
            # Retitle the main frame.
            self.root.title("Let's Play Black Jack!")
            # Creates the "Game" frame
            self.game_run = BlackJackScreen(self.root, self.player, self.computer, self.onclose_BJ_play)
        elif game_choice == 'Poker':
            self.root.title("Let's Play Poker!")
            self.game_run = PokerScreen(self.root, self.player, self.computer, self.onclose_Poker_play)

    def onclose_BJ_play(self):
        # Destroy the "Game" frame.
        self.game_run.destroy()
        # Re-title the main frame.
        self.root.title("Results:")
        # Create the Result frame
        self.results = BJResultsScreen(self.root, self.player, self.computer, self.onclose_all)

    def onclose_Poker_play(self):
        self.game_run.destroy()
        self.root.title("Results:")
        self.results = PokerResultsScreen(self.root, self.player, self.computer, self.onclose_all)

    def onclose_all(self):
        self.root.destroy()


def main():
    game = CardGameMain()
    game.setup_game_welcome()
    game.root.mainloop()


main()
