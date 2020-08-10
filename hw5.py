import basic_graphics
import tkinter as tk

def areLegalValues(vals):
    # returns true if all elements in vals are valid sudoku values (integers 1-9, or 0 for blank space)
    for elem in vals:
        if 0 > elem or elem > 9:
            print('Illegal Value!:', elem)
            return False
    return True

def isLegalRow(board, row):
    # returns true if row has no internal disagreements and no disagreements with rest of board
    if not areLegalValues(board[row]):
        #print('not legal values!!!')
        return False

    for i in range(len(board[row])):
        for j in range(i+1, len(board[row])):
            # check that row contains no duplicates
            #print("checking", board[row][i], board[row][j])
            if board[row][i] != 0 and board[row][i] == board[row][j]:
                return False
    return True

def isLegalCol(board, col):
    colVals = [ ]
    #get all column vals into 1D list since indexing columns is mad weird with Python lists
    for i in range(len(board[col])):
        colVals.append(board[i][col])

    # check to make sure all col elements are valid (0<elem<10 or elem=0 for blank spaces)
    if not areLegalValues(colVals):
        return False

    #check for duplicate values in column
    for i in range(len(colVals)):
        for j in range(i+1, len(colVals)):
            if colVals[i] != 0 and colVals[i] == colVals[j]:
                return False

    return True

def isLegalBlock(board, block):
    # block is a 3x3 part of sudoku board, block 0 is top left, 1 is center left, etc
    topLeftRow = 3*(block // 3)
    topLeftCol = 3*(block % 3)

    boxVals = [ ]

    for i in range(topLeftRow, topLeftRow+3):
        for j in range(topLeftCol, topLeftCol+3):
            #print(board[i][j], end='')
            boxVals.append(board[i][j])

    # check to make sure all box elements are valid (0<elem<10 or elem=0 for blank spaces)
    if not areLegalValues(boxVals):
        return False

    #check for duplicate values in box
    for i in range(len(boxVals)):
        for j in range(i+1, len(boxVals)):
            if boxVals[i] != 0 and boxVals[i] == boxVals[j]:
                return False
    return True

def isLegalSudoku(board):
    for i in range(len(board[0])):
        if not isLegalRow(board, i) or not isLegalCol(board, i) or not isLegalBlock(board, i):
            return False
    return True


test_doku = [
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
]

smaller_test_doku = [
  [ 5, 3, 0, 0],
  [ 6, 0, 0, 1],
  [ 0, 9, 8, 0],
  [ 8, 0, 0, 0],
]

#note: I ran more tests when coding these helper functions but didn't bother
#      writing up assert()s for each special case
assert(isLegalRow(test_doku, 1) == True)
assert(isLegalCol(test_doku, 1) == True)
assert(isLegalBlock(test_doku, 4) == True)
assert(isLegalSudoku(test_doku) == True)


# ======== BEGINNING OF HOMEWORK 6 ==========
TKroot = tk.Tk()




def drawSudoku(canvas, width, height, board, margin):
    # NOTE: Add a conditional to handle 4x4, 16x16 boards
    test = tk.Canvas(canvas, width=width, height=height)
    test.pack()

    #draw border lines
    borderWidth = 2.5
    test.create_line(margin, margin, (width - margin), margin, width=borderWidth)
    test.create_line(margin, margin, margin, (height - margin), width=borderWidth)
    test.create_line(margin, (height - margin), (width - margin), (height - margin), width=borderWidth)
    test.create_line( (width - margin), margin, (width - margin), (height - margin), width=borderWidth)

    heightGap = (height - 2*margin) // len(board[0])
    widthGap = (width - 2*margin) // len(board[0])



    #drawing inner border lines
    for i in range(1,len(board[0])):

        if i%3 == 0:
            #ensure every third line is darker to box in blocks
            lineWidth = borderWidth
        else:
            lineWidth = 1

        # vertical border line
        test.create_line((margin + i*widthGap), margin, (margin + i*widthGap), (height - margin), width=lineWidth)
        # horizontal split line
        test.create_line(margin, (margin + i*heightGap), (width - margin), (margin + i*heightGap), width=lineWidth)

    #test.create_text(margin + 0.5*widthGap, margin + 0.5*widthGap, text=board[0][0], fill="purple", font="Helvetica 12")


    for i in range(len(board[0])):
        for j in range(len(board[0])):
            test.create_text(margin + (j+0.5)*widthGap, margin + (i+0.5)*widthGap, text=board[i][j], fill="purple", font="Helvetica 12")

    TKroot.mainloop()


drawSudoku(TKroot, 400, 400, test_doku, 20)
#basic_graphics.run(width=400, height=600)
