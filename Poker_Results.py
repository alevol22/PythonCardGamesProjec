import tkinter


class PokerResultsScreen(tkinter.Frame):
    def __init__(self, master, player1, player2, go_to_exit):
        super(PokerResultsScreen, self).__init__(master)

        # objects
        self.player1 = player1
        self.player2 = player2

        # for Exit
        self.exit_program = go_to_exit

        self.create_widgets()
        self.grid()

    def create_widgets(self):

        tkinter.Label(self, text='Your Hand: ' + str(self.player1.hand_name(self.player1)), font=('Helvetica', 16)).grid(row=1, column=1)
        tkinter.Label(self, text='Computer Hand: ' + str(self.player2.hand_name(self.player2)), font=('Helvetica', 16)).grid(row=3, column=1)

        if self.player1.hand_value_e(self.player1) > self.player2.hand_value_e(self.player2):
            tkinter.Label(self, text='  ' + str(self.player1.name) + ' wins!!   ', font=('Helvetica', 15)).grid(row=5, column= 1)
        elif self.player2.hand_value_e(self.player2) > self.player1.hand_value_e(self.player1):
            tkinter.Label(self, text='  ' + str(self.player2.name) + ' wins!!   ', font=('Helvetica', 15)).grid(row=5, column=1)
        else:
            tkinter.Label(self, text='Result: Draw', font=('Helvetica', 15)).grid(row=5, column=1)

        for n in range(0, 2):
            if n == 0:
                player = self.player1
                self.column = 4
                row = 2
            else:
                player = self.player2
                self.column = 4
                row = 4
            keys = list(player.hand.keys())
            for k in keys:
                for card in player.hand[k]:
                    self.image_name = str(k) + str(card) + '.gif'
                    image = tkinter.PhotoImage(file=self.image_name)
                    w = tkinter.Label(self, image=image)
                    w.photo = image
                    w.grid(row=row, column=self.column)
                    self.column += 1

        tkinter.Button(self, text='Exit!', command=self.continue_clicked, bg='green', font=('Helvetica', 16)
                       ).grid(row=(self.column + 2), column=4)

    def continue_clicked(self):
        # when the Battle button is clicked
        self.exit_program()
