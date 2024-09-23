import random

# The class that holds the game
class Gamee:
    def __init__(self):
        self.secrt_num = random.randint(1, 100)  # The secret number
        self.atemptz = 0  # Number of attempts

    def start_gam(self):
        print("Welcome to the guessing game!")
        while True:
            try:
                gess = int(input("Enter a number from 1 to 100: "))
                self.atemptz += 1
                if self.chek_gess(gess):
                    break
            except ValueError:
                print("Please enter a valid number!")

    def chek_gess(self, gess):
        if gess < self.secrt_num:
            print("The number is less than the secret number.")
            return False
        elif gess > self.secrt_num:
            print("The number is greater than the secret number.")
            return False
        else:
            print(f"Congrats! You guessed the correct number in {self.atemptz} attempts.")
            return True

# Run the game
if __name__ == "__main__":
    game = Gamee()
    game.start_gam()
