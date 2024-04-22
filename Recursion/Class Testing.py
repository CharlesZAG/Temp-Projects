class Enemy:
    lives = 3

    def hit(self):
        print("Ouch!")
        self.lives -= 1

    def checkLives(self):
        if self.lives != 1 and self.lives != -1:
            print(f"I have {self.lives} lives left")
        else:
            print(f"I have {self.lives} life left")

def main():
    evilOne = Enemy()
    evilTwo = Enemy()

    evilOne.hit()
    evilOne.hit()
    evilTwo.hit()
    evilOne.checkLives()
    evilTwo.checkLives()


if __name__ == "__main__":
    main()