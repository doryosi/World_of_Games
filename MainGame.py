from Live import load_game, welcome
import MainScore

print(welcome(input("Please enter your name: ")))
load_game()
MainScore.start_server()
