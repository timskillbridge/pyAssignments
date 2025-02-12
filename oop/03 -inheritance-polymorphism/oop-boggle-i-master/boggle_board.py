import pprint
import random
import subprocess
import time
class BoggleBoard:
  
  def __init__(self):
    self.letters = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    self.letters[16] = "Qu"
    self.board =""
    # self.board = [[ "x" for x in "ABCD"] for x in "ABCD"]

  
    self.clearScreen()
    print(
    f'''
    {self.randLetter()}   {self.randLetter()}   {self.randLetter()}   {self.randLetter()}
    {self.randLetter()}   {self.randLetter()}   {self.randLetter()}   {self.randLetter()}
    {self.randLetter()}   {self.randLetter()}   {self.randLetter()}   {self.randLetter()}
    {self.randLetter()}   {self.randLetter()}   {self.randLetter()}   {self.randLetter()}
    ''')
    # input("Press Any Key to Play")

  def randLetter(self):
    return self.letters[random.randint(0,25)]
  def clearScreen(self):
    subprocess.run('clear',shell=True)
  

  def shake(self):
    
    x = [self.randLetter() for x in "ASDF" for x in "ASDF"]

    # print(x)

    board = []



    for i,j in enumerate(x):
      if len(x[i]) == 1:
        board.append(f"{j}   ")
      else:
        board.append(f"{j}  ")
    # time.sleep(0.1)

    self.clearScreen()
    print(
    f'''
    {board[0]}{board[1]}{board[2]}{board[3]}
    {board[4]}{board[5]}{board[6]}{board[7]}
    {board[8]}{board[9]}{board[10]}{board[11]}
    {board[12]}{board[13]}{board[14]}{board[15]}
    '''
    )






    # print(
    # f'''

    # ''')
    # {self.randLetter()}   {self.randLetter()}   {self.randLetter()}   {self.randLetter()}
    # {self.randLetter()}   {self.randLetter()}   {self.randLetter()}   {self.randLetter()}
    # {self.randLetter()}   {self.randLetter()}   {self.randLetter()}   {self.randLetter()}
    # {self.randLetter()}   {self.randLetter()}   {self.randLetter()}   {self.randLetter()}


running = True
board1 = BoggleBoard()
while running:
  


  print('''
  1. Any Key but 2
  2. Quit
          ''')
  getInput = input( "? ")
  if getInput == "2":
    print("\n\ Thanks for playing!\n press any key to exit")
    board1.clearScreen()
    running = False

  else:
    board1.shake()




