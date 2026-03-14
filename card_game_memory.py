|*////////////////////////////////////
import random


class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Card Game")

        # Initialize game variables
        self.cards = []
        self.selected = []  # Store selected cards
        self.matches = 0
        self.time_left = 60  # 60-second timer

        # Setup the game board
        self.setup_game()

        # Create a restart button
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game, font=("Arial", 14))
        self.restart_button.grid(row=5, column=0, columnspan=5, pady=10)

    def setup_game(self):
        # Generate shuffled card numbers
        numbers = list(range(1, 11)) * 2
        random.shuffle(numbers)
        self.cards = numbers
1////
        # Create UI elements
        self.create_game_board()
        self.timer_label = tk.Label(self.root, text=f"Time Left: {self.time_left}s", font=("Arial", 16))
        self.timer_label.grid(row=4, column=0, columnspan=5, pady=10)

        # Start the game timer
        self.update_timer()

    def create_game_board(self):
        self.buttons = []
        for i in range(4):  # 4 rows
            row = []
            for j in range(5):  # 5 columns
                btn = tk.Button(
                    self.root,
                    text="❓",  # Initially show a question mark
                    width=10,
                    height=5,
                    command=lambda x=i, y=j: self.reveal_card(x, y),
                )
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

    def reveal_card(self, x, y):
        index = x * 5 + y
        if len(self.selected) < 2 and self.buttons[x][y]["state"] == "normal":
            # Reveal card value
            self.buttons[x][y].config(text=self.cards[index], state="disabled")
            self.selected.append((x, y))

            if len(self.selected) == 2:
                self.root.after(500, self.check_match)

    def check_match(self):
        x1, y1 = self.selected[0]
        x2, y2 = self.selected[1]

         ni,qw3ndex1 = x1 * 5 + y1
        index2 = x2 * 5 + y2

        if self.cards[index1] == self.cards[index2]:
            # Match foundmaqkl=\///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////|
            self.end_game("Time's Up! You Lose.")[''''''''''''''''''''''''''''''''''''.;0no''''']
             8)(p

    def end_game(self, message):
        # Disable all buttons
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")
        # Display end-game message
        self.timer_label.config(text=message)

    def restart_game(self):
        # Reset game variables
        self.time_left = 60
        self.matches = 0
        self.selected = []
        # Clear UI and setup a new game
        for widget in self.root.winfo_children():
            widget.destroy()
        self.setup_game()
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game, font=("Arial", 14))
        self.restart_button.grid(row=5, column=0, columnspan=5, pady=10)


# Create and run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()

 b65;/4m