import tkinter


class PokerScreen(tkinter.Frame):
    def __init__(self, master, player1, player2, go_to_next):
        super(PokerScreen, self).__init__(master)

        # objects
        self.player1 = player1
        self.player2 = player2

        # for Exit
        self.times = 0
        self.call_on_results = go_to_next

        self.create_widgets()
        self.grid()

    def create_widgets(self):

        tkinter.Label(self, text='Your Hand', font=('Helvetica', 16)).grid(row=1, column=0)
        self.rule_lbl = tkinter.Label(self, text='Rules: Choose whether to draw new cards or to keep these cards.', font=('Helvetica', 12))
        self.rule_lbl.grid(row=2, column=0, columnspan=5)
        self.player1.start(5)
        self.player2.start(5)

        self.draw_bttn = tkinter.Button(self, text='Re-Draw', command=self.draw_clicked, bg='green', font=('Helvetica', 16))
        self.draw_bttn.grid(row=7, column=1)

        self.keep_bttn = tkinter.Button(self, text='Keep', command=self.keep_clicked, bg='green', font=('Helvetica', 16))
        self.keep_bttn.grid(row=7, column=3)

        self.display_image()

    def display_image(self):
        self.column = 0
        keys = list(self.player1.hand.keys())
        for k in keys:
            for card in self.player1.hand[k]:
                self.image_name = str(k) + str(card) + '.gif'
                image = tkinter.PhotoImage(file=self.image_name)
                w = tkinter.Label(self, image=image)
                w.photo = image
                w.grid(row=5, column=self.column)
                self.column += 1

    def draw_clicked(self):
        self.player1.clear_hand()
        self.player1.start(5)
        if self.player2.hand_value_e(self.player2) <= 2:
            self.player2.clear_hand()
            self.player2.start(5)
        self.times += 1
        if self.times > 1:
            self.draw_bttn.destroy()
        self.display_image()

    def keep_clicked(self):
        self.rule_lbl.destroy()
        # called when the results button clicked
        self.call_on_results()
