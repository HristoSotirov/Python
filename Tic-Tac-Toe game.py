#  Игра на морски шах

board = { 1:"-",
          2:"-",
          3:"-",
          4:"-",
          5:"-",
          6:"-",
          7:"-",
          8:"-",
          9:"-"  }
     
player = "X"
winner = None
restart = None
GameRunning = True

print('!TIC-TAC-TOE GAME!')
print(' 7 | 8 | 9 ')
print('---+---+---')
print(' 4 | 5 | 6 ')
print('---+---+---')
print(' 1 | 2 | 3 ')
print(f"\nIt is {player} turn!")

def printBoard():
  print(f' {board[7]} | {board[8]} | {board[9]} ')
  print('---+---+---')
  print(f' {board[4]} | {board[5]} | {board[6]} ')
  print('---+---+---')
  print(f' {board[1]} | {board[2]} | {board[3]} ')

#input
def pInput():
  global playerInput
  global player
  printBoard()
  while True:
    try:
        playerInput = int(input("Enter a number between 1 and 9: "))
        if playerInput < 1 and playerInput > 9 or board[playerInput] != "-":
            raise Exception
        break
    except ValueError:
        print("Wrong input. Try again.")
    except Exception:
        print("This position is probably taken. Try again!")
  board[playerInput] = player




#check
def rowCheck():
  global winner
  if board[7] == board[8] == board[9] != "-":
    winner = board[7]
    return True
  elif board[4] == board[5] == board[6] != "-":
    winner = board[4]
    return True
  elif board[1] == board[2] == board[3] != "-":
    winner = board[1]
    return True

def columnCheck():
  global winner
  if board[7] == board[4] == board[1] != "-":
    winner = board[7]
    return True
  elif board[8] == board[5] == board[2] != "-":
    winner = board[8]
    return True
  elif board[9] == board[6] == board[3] != "-":
    winner = board[9]
    return True

def diagonalCheck():
  global winner
  if board[7] == board[5] == board[3] != "-":
    winner = board[7]
    return True
  elif board[9] == board[5] == board[1] != "-":
    winner = board[9]
    return True

def win():
  global GameRunning
  global winner
  if columnCheck() or rowCheck() or diagonalCheck():
    printBoard()
    print(f'The winner is {winner}!')
    GameRunning = 'end' 

def tie():
  global GameRunning
  if board[1] != '-' and board[2] != '-' and board[3] != '-' and board[4] != '-' and board[5] != '-' and board[6] != '-' and board[7] != '-' and board[8] != '-' and board[9] != '-':
    printBoard()
    print("It is a tie!")
    GameRunning = 'end'

#switch
def switch():
  global player
  if player == "X":
    player = "O"
    print(f"\nIt is {player} turn!")
  elif player == "O":
    player = "X"
    print(f"\nIt is {player} turn!")

#restart
def rest():
  global GameRunning
  global board
  global printBoard
  global restart
  if GameRunning == 'end':
    restart = (input("\nDo you want to play again y/n: "))
    if restart == "y":
      board = { 1:"-",
                2:"-",
                3:"-",
                4:"-",
                5:"-",
                6:"-",
                7:"-",
                8:"-",
                9:"-"  }
      print("\nNew Game!")
      print(f"\nIt is {player} turn!")
      GameRunning = True
    elif restart == "n":
      print("\nThangs for playing!")
        
while GameRunning == True:
  pInput()
  switch()
  win()
  tie() 
  rest()
