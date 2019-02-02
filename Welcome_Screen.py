import tkinter


class CardGameWelcomeScreen(tkinter.Frame):
    def __init__(self, master, return_control):
        super(CardGameWelcomeScreen, self).__init__(master)

        self.return_control = return_control
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        tkinter.Label(self, text='Welcome to Card Games!', font=('Helvetica', 16)).grid(row=2, column=2)
        tkinter.Label(self, text='Enter your name:').grid(row=4, column=2)

        self.name_ent = tkinter.Entry(self)
        self.name_ent.grid(row=5, column=2)

        tkinter.Label(self, text="Choose game:").grid(row=6, column=0)
        self.game_choice = tkinter.StringVar()
        self.game_choice.set(None)

        games = ["Black Jack", "Poker"]
        row = 7
        for game in games:
            tkinter.Radiobutton(self, text=game, variable=self.game_choice, value=game).grid(row=row, column=1)
            row += 1

        tkinter.Button(self, text='Start Game', command=self.start_clicked, bg='green', font=('Helvetica', 16)
                       ).grid(row=row + 1, column=4)

    def start_clicked(self):
        # called when the Start button is clicked: self.name_ent to callback
        self.return_control(self.name_ent.get(), self.game_choice.get())
