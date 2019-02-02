import tkinter


class BJResultsScreen(tkinter.Frame):
    def __init__(self, master, player1, player2, go_to_exit):
        super(BJResultsScreen, self).__init__(master)

        # objects
        self.player1 = player1
        self.player2 = player2

        # for Exit
        self.exit_program = go_to_exit

        self.create_widgets()
        self.grid()

    def create_widgets(self):

        tkinter.Label(self, text='You', font=('Helvetica', 16)).grid(row=1, column=1)
        tkinter.Label(self, text='Points: ' + str(self.player1.count_points()), font=('Helvetica', 15)).grid(row=2, column=1)
        tkinter.Label(self, text='Computer', font=('Helvetica', 16)).grid(row=1, column=3)
        tkinter.Label(self, text='Points: ' + str(self.player2.count_points()), font=('Helvetica', 15)).grid(row=2, column=3)

        if self.player1.player_status():
            tkinter.Label(self, text='  ' + str(self.player1.name) + ' wins!!   ', font=('Helvetica', 15)).grid(row=5, column= 2)
        elif self.player2.player_status():
            tkinter.Label(self, text='  ' + str(self.player2.name) + ' wins!!   ', font=('Helvetica', 15)).grid(row=5, column=2)
        else:
            tkinter.Label(self, text='No one wins.', font=('Helvetica', 15)).grid(row=5, column= 2)

        for n in range(0, 2):
            if n == 0:
                player = self.player1
                column = 1
                self.row = 3
            else:
                player = self.player2
                column = 3
                self.row = 3
            keys = list(player.hand.keys())
            for k in keys:
                for card in player.hand[k]:
                    self.image_name = str(k) + str(card) + '.gif'
                    image = tkinter.PhotoImage(file=self.image_name)
                    w = tkinter.Label(self, image=image)
                    w.photo = image
                    w.grid(row=self.row, column=column)
                    self.row += 1

        tkinter.Button(self, text='Exit!', command=self.continue_clicked, bg='green', font=('Helvetica', 16)
                       ).grid(row=(self.row + 2), column=4)

    def continue_clicked(self):
        # when the Battle button is clicked
        self.exit_program()
