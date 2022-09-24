from Live import load_game, welcome
import MainScore

MainScore.start_server()
print(welcome(input("Please enter your name: ")))
load_game()

