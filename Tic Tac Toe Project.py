#!/usr/bin/env python
# coding: utf-8

# In[3]:


# function to print out the board

from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('   |   |') 
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

    pass


# In[4]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[5]:


def player_input():
    
    marker = ''
    
    while marker != 'X' and marker != 'O':
        
        marker = input('Player 1, choose X or O: ')
        
    Player1 = marker
        
    if Player1 == 'X':
         Player2 = 'O'
    else:
         Player2 = 'X'
    return (Player1,Player2)
            


# In[6]:


Player1_marker, Player2_marker = player_input()


# In[7]:


Player1_marker


# In[8]:


Player2_marker


# In[9]:


def place_marker(board, marker, position):
    board[position] = marker


# In[10]:


place_marker(test_board,'$',8)
display_board(test_board)


# In[11]:


# to check if someone has won

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
          (board[4] == mark and board[5] == mark and board[6] == mark) or
          (board[1] == mark and board[2] == mark and board[3] == mark) or
          (board[7] == mark and board[4] == mark and board[1] == mark) or
          (board[8] == mark and board[5] == mark and board[2] == mark) or
          (board[9] == mark and board[6] == mark and board[3] == mark) or
          (board[7] == mark and board[5] == mark and board[3] == mark) or
          (board[9] == mark and board[5] == mark and board[1] == mark))


# In[12]:


display_board(test_board)
win_check(test_board,'X')


# In[13]:


# to randomly decide which function goes first

import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[14]:


# to check whether a space on the board is freely available

def space_check(board, position):
    
    return board[position] == ' '


# In[15]:


# to check if the board is full and returns a boolean value

def full_board_check(board):
    for i in range(1,10):
        
        # SPACE_CHECK SE CHECK KARENGE SPACE H YA NHI
        
        if space_check(board,i):
            
            # AGR SPACE HAI TOH FALSE RETURN KRENGE KYUKI HMARA BOARD FULL NHI HAI
            
            return False
        
    # BOARD IS FULL IF WE RETURN TRUE
    return True


# In[16]:


def player_choice(board):
    
    position = 0
    
    # this check to see if it's an actual number that's on the board or it's going to check is that space still available?  
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
        
    return position


# In[17]:


# ASK THE PLAYER IF THEY WANT TO PLAY AGAIN AND RETURNS THE BOOLEAN TRUE IF THEY DO WANT TO PLAY

def replay():
    
    choice = input("Play again? Enter Yes or No ")
    
    return choice == 'Yes'
    


# In[ ]:


# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to Tic TAC TOE!')

while True:
    
    # PLAY THE GAME

    ## SET EVERYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKERS X,O)
    the_board = [' ']*10        # list of 10 empty strings
    Player1_marker, Player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are You Ready to play? y or n. ')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    ## GAME PLAY
    
    while game_on:
        
        ### PLAYER 1 TURN
        if turn == 'Player 1':
            
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on thr position
            place_marker(the_board, Player1_marker, position)
            
            # Check if they won
            if win_check(the_board, Player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player 2'
            
    
       ### PLAYER 2 TURN
       
    
        else:
            
            # Show the board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place the marker on thr position
            place_marker(the_board, Player2_marker, position)
            
            # Check if they won
            if win_check(the_board, Player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player 1'
        
    
    if not replay():
        break
# BREAK OUT OF THE WHILE LOOP ON replay()

