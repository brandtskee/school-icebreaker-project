# Brandt Sanche 3086741
# Milestone 3

from graphics import *
import time

# Global constants that define window size and intializes the main informative message
WIN_H = 550
WIN_W = 555
SPLASH_H = 300
SPLASH_W = 250
msg_main = ''
info = ''

#Purpose: Creates quit and reset buttons and displays to user
#Parameter: Window (win)
#Return value: Quit (quit) button and Reset (reset) button
def create_buttons():
    #create quit button
    #need rectangle and text
    rect1 = Rectangle(Point(400, 475), Point(475, 500))#.draw(win)
    text1 = Text(Point(437.5, 487.5), 'QUIT')#.draw(win)
    #create reset button
    #rectangle and text object
    rect2 = Rectangle(Point(400, 505), Point(475, 530))#.draw(win)
    text2 = Text(Point(437.5, 517.5), 'RESET')#.draw(win)
    rect3 = Rectangle(Point(87.5, 210), Point (162.5, 235))
    text3 = Text(Point(125, 222.5), 'Play')
    rect4 = Rectangle(Point(87.5, 240), Point(162.5, 265))
    text4 = Text(Point(125, 252.5), 'Quit')
    rect5 = Rectangle(Point(87.5, 210), Point (162.5, 235))
    text5 = Text(Point(125, 222.5), 'RESET')
    quit = rect1, text1
    reset = rect2, text2
    play_game = rect3, text3
    splash_quit = rect4, text4
    splash_reset = rect5, text5
    return quit, reset, play_game, splash_quit, splash_reset

#Purpose: Checks if a button is clicked and returns boolean statement
#Parameter: Mouse click coordinate (pt), Button (btn)
#Return value: True or False
def btn_clicked(pt, btn):
    rect = btn[0]
    corner1 = btn[0].getP1()
    corner2 = btn[0].getP2()
    x1, y1, x2, y2 = corner1.getX(), corner1.getY(), corner2.getX(), corner2.getY()
    ptX = pt.getX()
    ptY = pt.getY()
    if (ptX >= x1) and (ptX <= x2) and (ptY >= y1) and (ptY <= y2):
        return True
    else:
        return False

#Purpose: Creates a player object for two players with pictures
#Parameter: Window (win)
#Return value: player1 and player2 (as images)
def create_players(win):
    # create a circle or image object for player 1
    player1 = Image(Point(30, 195), 'Dot_Blue.gif').draw(win)
    # create a circle or image object for player 2
    player2 = Image(Point(525, 195), 'Dot_Red.gif').draw(win)
    return player1, player2

#Purpose: Creates the squares in rows and appends them to a list
#Parameter: Window (win)
#Return value: List of rows as a board (board)
def create_board(win):
    # initialize board
    board = []
    #create a list that represents a row and then append it to the big list which is board
    row = []
    # nested for loop so we can create the board one row at a time
    # The outer for loop is for the rows
    for y in range(0, 7):
        # The inner for loop is for the columns range
        h = (y*50) + y*5 + 5
        row = []
        for i in range (0, 10):
            # create rectangle object
            w = (i*50) + (i*5) + 5
            square = Rectangle(Point(w, h), Point(w+50, h+50))
            square.setFill('white')
            square.draw(win)
            # append this object to a smaller list
            row.append(square)
        # append this small list to the big list
        board.append(row)
    return board

#Purpose: Checks to see if mouse click is in board area and returns boolean statement
#Parameter: Mouse click coordinate (pt)
#Return value: True or False
def in_board(pt, board):
    for rows in board:
        for i in rows:
            if in_square(pt, i) == True:
                return True

#Purpose: Get the position of the mouse click in terms of row and column  
#Parameter: Mouse click coordinate (pt), Board list (board)
#Return value: row_number, column_number
def position(pt, board):
    global msg_main
    row_number = 1
    column_number = 1
    for rows in board:
        for i in rows:
            in_square(pt, i)
            if in_square(pt, i) == True:
                return row_number, column_number, i
            column_number += 1
        # Updates cycled row and column
        row_number += 1
        column_number = 1

#Purpose: Determines if click is inside a square
#Parameter: Mouse click coordinate (pt), square
#Return value: True or False
def in_square(pt, square):
    corner1 = square.getP1()
    corner2 = square.getP2()
    # Extracts X and Y values from each corner
    topX = corner1.getX()
    topY = corner1.getY()
    bottomX = corner2.getX()
    bottomY = corner2.getY()
    ptX = pt.getX()
    ptY = pt.getY()
    # Determines if mouse click is inside square
    if (ptX >= topX) and (ptY >= topY) and (ptX <= bottomX) and (ptY <= bottomY):
        return True
    else:
        return False

#Purpose: Updates msg_main with useful info in the form of text
#Parameter: Window (win)
#Return value: Updated text (msg_main)
def create_messgage(win):
    global msg_main
    # Update global text onject
    msg_main = Text(Point(250, 517.5), 'Hello').draw(win)
    return msg_main

#Purpose: Defines the column and row the player is in, and checks the turn to determine the next action
#Parameter: turn, selected column (column), selected row (row), player1, player2, selected square (square)
#Return value: turn
def check_turn(turn, column, row, player1, player2, square, board):
    global info, msg_main
    # Determines anchor point of the player and divieds by 55 (in accordance with 55 pixels between blocks due to spacing) to determine the location of each player
    anchor1 = player1.getAnchor()
    player1_column = (anchor1.getX())//55 + 1
    player1_row = (anchor1.getY())//55 + 1
    anchor2 = player2.getAnchor()
    player2_column = (anchor2.getX())//55 + 1
    player2_row = (anchor2.getY())//55 + 1
    # Turn 0 defines moving stage of Player 0, Turn 2 is moving stage of Player 2, and turns 1 and 3 are ice breaking turns for Player 1 and Player 2 respectively
    # If turn is 10, then Player 0 is the winner. If turn is 11, then Player 1 is the winner
    # is_trapped is called every turn in order to keep checking if a player is trapped
    if turn == 0:
        if is_trapped(player1_row, player1_column, player2_row, player2_column, board) == True:
            turn = 11
            return turn
        info.setText('Player: 0')
        turn, new_row, new_column = move_player(player1, player1_column, player1_row, player2_column, player2_row, row, column, square, turn)
        if is_trapped(new_row, new_column, player2_row, player2_column, board) == True:
            turn = 11
            return turn
        # used to determine if other player is trapped before ice is placed
        if is_trapped(player2_row, player2_column, new_row, new_column, board) == True:
            turn = 10
            return turn
        return turn
    if turn == 1 or turn == 3:
        turn = break_ice(player1_column, player1_row, player2_column, player2_row, column, row, square, turn)
        if is_trapped(player2_row, player2_column, player1_row, player1_column, board) == True:
            turn = 10
            return turn
        if is_trapped(player1_row, player1_column, player2_row, player2_column, board) == True:
            turn = 11
            return turn
        return turn
    if turn == 2:
        if is_trapped(player2_row, player2_column, player1_row, player1_column, board) == True:
            turn = 10
            return turn
        info.setText('Player: 1')
        turn, new_row, new_column = move_player(player2, player2_column, player2_row, player1_column, player1_row, row, column, square, turn)
        if is_trapped(new_row, new_column, player1_row, player1_column, board) == True:
            turn = 10
            return turn
        # used to determine if other player is trapped before ice is placed
        if is_trapped(player1_row, player1_column, new_row, new_column, board) == True:
            turn = 11
            return turn
        return turn

#Purpose: Moves the player to the selected spot and checks to see if move is valid
#Parameter: Player thats moving (player), player location (player_row, player_column), other players location (other_player_column, other_player_row), row and column of selected square (row, column, square), turn
#Return value: turn
def move_player(player, player_column, player_row, other_player_column, other_player_row, row, column, square, turn):
        anchor = player.getAnchor()
        # This long if statement checks everything at once. Checks to make sure the selected square is no further than one block in each direction, checks to make sure the block is not a broken block of ice, checks to make sure you are not staying in one spot and checks to ensure you cannot move to the same spot as other player
        if (player_column == column or player_column == column-1 or player_column == column+1) and (player_row == row or player_row == row-1 or player_row == row+1) and square.config['fill'] != (color_rgb(173, 216, 230)) and (column != other_player_column or row != other_player_row) and (column != player_column or row != player_row):
            player.move(-(player_column-column)*55, -(player_row-row)*55)
            new_row = ((player.getAnchor()).getY())//55 + 1
            new_column = ((player.getAnchor()).getX())//55 + 1
            msg_main.setText("Moved to " + "("+str(row) + "," + str(column) + ")")
            turn += 1
            return turn, new_row, new_column
        else:
            msg_main.setText("Invalid Move")
            return turn, player_row, player_column

#Purpose: Breaks the ice on the selected square
#Parameter: Player 1 position (player1_column, player1_row), Player 2 position (player2_column, player2_row), location of selected square (column, row, square), turn
#Return value: turn
def break_ice(player1_column, player1_row, player2_column, player2_row, column, row, square, turn):
    # if statement checks to make sure the selected square is not already broken or occupied by a player
    if square.config['fill'] == 'white' and (column != player1_column or row != player1_row) and (column != player2_column or row != player2_row):
        square.setFill(color_rgb(173, 216, 230))
        msg_main.setText('Broke ice at ' + "(" + str(row) + "," + str(column) + ")")
        time.sleep(1)
        msg_main.setText('')
        turn += 1
        # if statements that update the screen to display which players turn it is
        if turn == 1:
            info.setText('Player: 0')
        if turn == 2:
            info.setText('Player: 1')
        if turn == 3:
            info.setText('Player: 1')
        if turn == 4:
            turn = 0
            info.setText('Player: 0')
        return turn
    else:
        msg_main.setText('Invalid Break')
        return turn

#Purpose: Gives the reset button function and restarts the game
#Parameter: board, Player images (player1, player2)
#Return value: None
def reset_game(board, player1, player2):
    for rows in board:
        for i in rows:
            i.setFill('white')
    player1.undraw()
    player2.undraw()

#Purpose: Initial splash window that opens when the program is started
#Parameter: Play button (play_game), Quit button (splash_quit)
#Return: True or False
def splash(play_game, splash_quit):
    splash_win = GraphWin('', SPLASH_W, SPLASH_H)
    splash_win.setBackground(color_rgb(173, 216, 230))
    play_game[0].draw(splash_win)
    play_game[1].draw(splash_win)
    splash_quit[0].draw(splash_win)
    splash_quit[1].draw(splash_win)
    welcome_text = Text(Point(125, 100), 'Welcome to Icebreaker!').draw(splash_win)
    while True:
        try:
            pt = splash_win.getMouse()
        except:
            splash_win.close()
        # Returns True if Play is clicked and closes window
        if btn_clicked(pt, play_game) == True:
            splash_win.close()
            return True
        # Returns False if Quit is clicked and closes window
        if btn_clicked(pt, splash_quit) == True:
            splash_win.close()
            return False

#Purpose: Final splash Window that displays who won the game and gives options to the player
#Parameter: Reset button (reset), Quit button (quit), turn
#Return: True or False
def end_splash(reset, quit, turn):
    end_win = GraphWin('', SPLASH_W, SPLASH_H)
    reset[0].draw(end_win)
    quit[0].draw(end_win)
    reset[1].draw(end_win)
    quit[1].draw(end_win)
    # Uses turn to check who won and set background to matching color of the winning player and displays text showing who won
    if turn == 10:
        end_win.setBackground('blue')
        winner_text = Text(Point(125, 100), 'Player 0 Wins!').draw(end_win)
    if turn == 11:
        end_win.setBackground('red')
        winner_text = Text(Point(125, 100), 'Player 1 Wins!').draw(end_win)
    while True:
        try:
            pt = end_win.getMouse()
        except:
            end_win.close()
        # Returns True if Reset is clicked and closes the window
        if btn_clicked(pt, reset) == True:
            end_win.close()
            return True
        # Returns False if Quit is clicked and closes the window
        if btn_clicked(pt, quit) == True:
            end_win.close()
            return False

#Purpose: Determines whether the player is trapped on the board by broken blocks and/or by the other player
#Parameter: Player row and column (player_row, player_column), other player coordinates (other_player_row, other_player_column), board list that contains all the squares (board)
#Return: True or False
def is_trapped(player_row, player_column, other_player_row, other_player_column, board):
    row = int(player_row)
    column = int(player_column)
    # list of all possible moves
    moves = [[row-1, column-1], [row-1, column], [row-1, column+1], [row, column-1], [row, column+1], [row+1, column-1], [row+1, column], [row+1, column+1]]
    counter = 0
    # if statements that remove possible moves if player is on the edge of the board
    # Top left corner
    if row == 1 and column == 1:
        moves.pop(5)
        moves.pop(3)
        moves.pop(2)
        moves.pop(1)
        moves.pop(0)
    # Bottom left corner
    elif row == 7 and column == 1:
        moves.pop(7)
        moves.pop(6)
        moves.pop(5)
        moves.pop(3)
        moves.pop(0)
    # Top right corner
    elif row == 1 and column == 10:
        moves.pop(7)
        moves.pop(4)
        moves.pop(2)
        moves.pop(1)
        moves.pop(0)
    # Bottom right corner
    elif row == 7 and column == 10:
        moves.pop(7)
        moves.pop(6)
        moves.pop(5)
        moves.pop(4)
        moves.pop(2)
    # Top edge
    elif row == 1:
        moves.pop(2)
        moves.pop(1)
        moves.pop(0)
    # Bottom edge
    elif row == 7:
        moves.pop(7)
        moves.pop(6)
        moves.pop(5)
    # Left edge
    elif column == 1:
        moves.pop(5)
        moves.pop(3)
        moves.pop(0)
    # Right edge
    elif column == 10:
        moves.pop(7)
        moves.pop(4)
        moves.pop(2)
    for items in moves:
        # Checks if each surrounding square is not broken. If broken, adds 1 to the counter
        if board[items[0]-1][items[1]-1].config['fill'] != 'white':
            counter += 1
        # Checks if each surrounding square is occupied by a player. If so, adds 1 to the counter
        if items == ([int(other_player_row), int(other_player_column)]):
            counter += 1
    # If counter equals the amount of moves remaining, the player is Trapped and True is returned
    if counter == len(moves):
        return True
    else:
        return False


#Purpose: Main function that runs the UI in a loop
#Parameter: None
#Return value: None
def main():
    global WIN_H, WIN_W, msg_main, info, SPLASH_W, SPLASH_H
    quit, reset, play_game, splash_quit, splash_reset = create_buttons()
    # initiate splash screen for beginning of the game and close if quit button is clicked
    initiate = splash(play_game, splash_quit)
    if initiate == False:
        return
    #create graphics window
    win = GraphWin('Icebreaker - Brandt Sanche', WIN_W, WIN_H)
    reset[0].draw(win)
    quit[0].draw(win)
    quit[1].draw(win)
    reset[1].draw(win)
    info = Text(Point(250, 500), 'Player: 0').draw(win)
    # call create_board to create the board
    board = create_board(win)
    # call create_players in order to return player 1 and 2
    player1, player2 = create_players(win)
    # call create_message to create the text object for the message
    create_messgage(win)
    turn = 0
    while True:
        try:
            pt = win.getMouse()
        except:
            win.close()
        if btn_clicked(pt, quit) == True:
            msg_main.setText('Bye Bye!')
            # Breaks loop when QUIT is pressed
            break
        elif btn_clicked(pt, reset) == True:
            msg_main.setText('RESET')
            reset_game(board, player1, player2)
            player1, player2 = create_players(win)
            info.setText('Player: 0')
            turn = 0
        elif in_board(pt, board) == True:
            # If mouse click is in a square on the board, return the row and column number from position() as a tuple
            row_number, column_number, square = position(pt, board)
            turn = check_turn(turn, column_number, row_number, player1, player2, square, board)
            # If turn is 10 or 11, opens final splash window
            if turn == 10 or turn == 11:
                user_input = end_splash(splash_reset, splash_quit, turn)
                # if Reset is clicked it resets the board
                if user_input == True:
                    msg_main.setText('RESET')
                    reset_game(board, player1, player2)
                    player1, player2 = create_players(win)
                    info.setText('Player: 0')
                    turn = 0
                # if Quit is clicked it closes game window, breaks loop and ends the program
                if user_input == False:
                    win.close()
                    break
        # Displays click coordinates if not in a square
        else:
            ptX = int(pt.getX())
            ptY = int(pt.getY())
            msg_main.setText('(' + str(ptX) + ', ' + str(ptY) + ')')
    try:
        pt = win.getMouse()
    except:
        win.close()
main()
