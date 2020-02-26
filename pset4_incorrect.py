#incorrect

while True:
       game = str(input("Enter n to deal a new hand, r to replay the last hand, or e to end the game: "))
       if game == 'e':
           break
       elif game == 'n':
            user = str(input("Enter u to have yourself play, c to have the computer play: "))
            if user == 'c':
                hand = dealHand(HAND_SIZE)
                compPlayHand(hand, wordList, HAND_SIZE)
            elif user == 'u':    
                hand=dealHand(HAND_SIZE)
                playHand(hand, wordList, HAND_SIZE)
            else:
                print("Invalid command.")
                user
       elif game == 'r':
            user = str(input("Enter u to have yourself play, c to have the computer play: "))
            if user == 'c':
                try:
                    compPlayHand(hand, wordList, HAND_SIZE)
                except:
                     print("You have not played a hand yet. Please play a new hand first!")
            elif user == 'u':
                try:
                    playHand(hand, wordList, HAND_SIZE)
                except:
                    print("You have not played a hand yet. Please play a new hand first!")
            else:
                print("You have not played a hand yet. Please play a new hand first!")
                user
        
       else:
            print("Invalid command")      