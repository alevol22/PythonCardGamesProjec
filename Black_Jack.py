import tkinter


class BlackJackScreen(tkinter.Frame):
    def __init__(self, master, player1, player2, go_to_next):
        super(BlackJackScreen, self).__init__(master)

        # objects
        self.player1 = player1
        self.player2 = player2

        # for Exit
        self.call_on_results = go_to_next

        self.create_widgets()
        self.grid()

    def create_widgets(self):

        tkinter.Label(self, text='You', font=('Helvetica', 16)).grid(row=1, column=0)
        self.player1.start(3)
        self.player2.start(3)

        if self.player1.player_status() != 'True' or self.player2.player_status() != 'True':
            tkinter.Button(self, text='Results', command=self.results_clicked, bg='green', font=('Helvetica', 16)).grid(row=7, column=4)

        self.draw_bttn = tkinter.Button(self, text='Draw', command=self.draw_clicked, bg='green', font=('Helvetica', 16))
        self.draw_bttn.grid(row=6, column=1)

        self.display_image()

    def display_image(self):
        self.column = 1
        keys = list(self.player1.hand.keys())
        for k in keys:
            for card in self.player1.hand[k]:
                self.image_name = str(k) + str(card) + '.gif'
                image = tkinter.PhotoImage(file=self.image_name)
                w = tkinter.Label(self, image=image)
                w.photo = image
                w.grid(row=3, column=self.column)
                self.column += 1


    def draw_clicked(self):
        if self.player1.player_status() == 'True' and self.player2.player_status() == 'True':
            self.player1.draw()
            self.player2.draw()
            self.display_image()
        else:
            self.draw_bttn.destroy()
            tkinter.Button(self, text='Results', command=self.results_clicked, bg='green', font=('Helvetica', 16)).grid(row=7, column=4)

    def results_clicked(self):
        # called when the results button clicked
        self.call_on_results()
