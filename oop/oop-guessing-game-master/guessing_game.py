class GuessingGame():
    # Write your code here
   def __init__(self,answer):
        self.answer = answer
        self.game_solved = False
   
   def guess(self,userGuess):
       if userGuess > self.answer:
           self.game_solved = False
           return "high"
       elif userGuess < self.answer:
           self.game_solved = False
           return "low"
       else:
           self.game_solved =True
           return "correct"
    
   def solved(self):
       if self.game_solved == True:
           return True
       else:
           return False
       
       
    

game = GuessingGame(10)
print(game.guess(10))