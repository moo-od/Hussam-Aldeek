class Duck:
    def __init__(self, nam):
        self.nam = nam
        self.x = 0
        self.y = 0

    def go_forwd(self):
        self.y += 1
        print(f"{self.nam} moved forwd. Now at ({self.x}, {self.y})")

    def go_backwd(self):
        self.y -= 1
        print(f"{self.nam} moved backwd. Now at ({self.x}, {self.y})")

    def go_left(self):
        self.x -= 1
        print(f"{self.nam} moved left. Now at ({self.x}, {self.y})")

    def go_rite(self):
        self.x += 1
        print(f"{self.nam} moved rite. Now at ({self.x}, {self.y})")

# run game
if __name__ == "__main__":
    name = input("Enter duck name: ")
    player_duck = Duck(name)

    while True:
        command = input("Move duck (forwd, backwd, left, rite) or type 'exit' to stop: ").lower()
        if command == "forwd":
            player_duck.go_forwd()
        elif command == "backwd":
            player_duck.go_backwd()
        elif command == "left":
            player_duck.go_left()
        elif command == "rite":
            player_duck.go_rite()
        elif command == "exit":
            print("Exiting the game!")
            break
        else:
            print("Unknown command, try again.")
