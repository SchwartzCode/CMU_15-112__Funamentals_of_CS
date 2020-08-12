import tkinter as tk
import random



class sudoku(object):

    cellPosx = 0
    cellPosy = 0
    board = [ ['0']*9 for i in range(9)]
    initNums = [ [0]*9 for i in range(9)]
    userInputs = [ ['0']*9 for i in range(9)]
    frameSideLen = 400
    height = frameSideLen
    width = frameSideLen
    margin = 20

    TKroot = tk.Tk()
    canvas = tk.Canvas(TKroot, width=width, height=height)

    def __init__(self):
        fpath = r"C:\Users\jonbs\Documents\JonathanStuff\CMU_Stuff\15-112__Fundamentals_of_CS\sudokus.txt"

        dokus = [ ]
        with open(fpath, 'r') as file:
            for line in file:
                line = line.rstrip("\n")
                dokus.append(line)
            choice = int(random.random()*50)

        for i in range(1,10):
            for j in range(9):
                self.board[i-1][j] = dokus[choice*10 + i][j]
                if dokus[choice*10 + i][j] != '0':
                    self.initNums[i-1][j] = 1


        self.canvas.bind("<Button-1>", self.mouseClick)
        self.canvas.bind("<Left>", self.leftKey)
        self.canvas.bind("<Right>", self.rightKey)
        self.canvas.bind("<Up>", self.upKey)
        self.canvas.bind("<Down>", self.downKey)
        self.canvas.bind("<BackSpace>", self.backspace)
        for i in range(1,10):
            self.canvas.bind(str(i), self.numberInput)
        self.canvas.focus_set() #need this for canvas to detect arrow key presses I think
        self.canvas.pack()

    def areLegalValues(self, vals):
        # returns true if all elements in vals are valid sudoku values (integers 1-9, or 0 for blank space)
        for elem in vals:
            if 0 > int(elem) or int(elem) > 9:
                print('Illegal Value!:', elem)
                return False
        return True

    def isLegalRow(self, row, inBoard):

        # returns true if row has no internal disagreements and no disagreements with rest of board
        if not self.areLegalValues(inBoard[row]):
            print('not legal values!!!')
            return False

        for i in range(len(inBoard[row])):
            for j in range(i+1, len(inBoard[row])):
                # check that row contains no duplicates
                #print("checking", board[row][i], board[row][j])
                if int(inBoard[row][i]) != 0 and inBoard[row][i] == inBoard[row][j]:
                    return False
        return True

    def isLegalCol(self, col, inBoard):
        colVals = [ ]
        #get all column vals into 1D list since indexing columns is mad weird with Python lists
        for i in range(len(inBoard[col])):
            colVals.append(inBoard[i][col])

        # check to make sure all col elements are valid (0<elem<10 or elem=0 for blank spaces)
        if not self.areLegalValues(colVals):
            return False

        #check for duplicate values in column
        for i in range(len(colVals)):
            for j in range(i+1, len(colVals)):
                if int(colVals[i]) != 0 and colVals[i] == colVals[j]:
                    return False

        return True

    def isLegalBlock(self, block, inBoard):
        # block is a 3x3 part of sudoku board, block 0 is top left, 1 is center left, etc
        topLeftRow = 3*(block // 3)
        topLeftCol = 3*(block % 3)

        boxVals = [ ]

        for i in range(topLeftRow, topLeftRow+3):
            for j in range(topLeftCol, topLeftCol+3):
                #print(board[i][j], end='')
                boxVals.append(inBoard[i][j])

        # check to make sure all box elements are valid (0<elem<10 or elem=0 for blank spaces)
        if not self.areLegalValues(boxVals):
            return False

        #check for duplicate values in box
        for i in range(len(boxVals)):
            for j in range(i+1, len(boxVals)):
                if int(boxVals[i]) != 0 and boxVals[i] == boxVals[j]:
                    return False
        return True

    def isLegalSudoku(self, inBoard):
        for i in range(len(inBoard[0])):
            if not self.isLegalRow(i, inBoard) or not self.isLegalCol(i, inBoard) or not self.isLegalBlock(i, inBoard):
                return False
        return True





    # ======== BEGINNING OF HOMEWORK 6 ==========
    def drawSudoku(self):
        #, canvas, width, height, board, initNums, margin
        # NOTE: Add a conditional to handle 4x4, 16x16 boards


        spacing = (self.height - 2*self.margin) // len(self.board[0])




        #draw border lines
        borderWidth = 2.5
        self.canvas.create_line(self.margin, self.margin, (self.width - self.margin), self.margin, width=borderWidth)
        self.canvas.create_line(self.margin, self.margin, self.margin, (self.height - self.margin), width=borderWidth)
        self.canvas.create_line(self.margin, (self.height - self.margin), (self.width - self.margin), (self.height - self.margin), width=borderWidth)
        self.canvas.create_line( (self.width - self.margin), self.margin, (self.width - self.margin), (self.height - self.margin), width=borderWidth)

        heightGap = (self.height - 2*self.margin) // len(self.board[0])
        widthGap = (self.width - 2*self.margin) // len(self.board[0])

        #drawing inner border lines
        for i in range(1,len(self.board[0])):

            if i%3 == 0:
                #ensure every third line is darker to box in blocks
                lineWidth = borderWidth
            else:
                lineWidth = 1

            # vertical border line
            self.canvas.create_line((self.margin + i*widthGap), self.margin, (self.margin + i*widthGap), (self.height - self.margin), width=lineWidth)
            # horizontal split line
            self.canvas.create_line(self.margin, (self.margin + i*heightGap), (self.width - self.margin), (self.margin + i*heightGap), width=lineWidth)

        #self.canvas.create_text(margin + 0.5*widthGap, margin + 0.5*widthGap, text=board[0][0], fill="purple", font="Helvetica 12")


        for i in range(len(self.board[0])):
            for j in range(len(self.board[0])):
                if self.initNums[i][j]:
                    self.canvas.create_text(self.margin + (j+0.5)*widthGap, self.margin + (i+0.5)*widthGap, text=self.board[i][j], fill="purple", font="Helvetica 12 bold")
                """
                if self.board[i][j] != '0':
                    if self.initNums[i][j]:
                        self.canvas.create_text(self.margin + (j+0.5)*widthGap, self.margin + (i+0.5)*widthGap, text=self.board[i][j], fill="purple", font="Helvetica 12 bold")
                    else:
                        self.canvas.create_text(self.margin + (j+0.5)*widthGap, self.margin + (i+0.5)*widthGap, text=self.board[i][j], font="Helvetica 12")
                """

        self.canvas.create_rectangle( (self.margin+spacing*self.cellPosx), (self.margin+spacing*self.cellPosy), (self.margin+spacing*(self.cellPosx+1)),
         (self.margin+spacing*(self.cellPosy+1)), width=2.5, outline='red', tags="activeSquare")

        self.TKroot.mainloop()


    def mouseClick(self, event):
        #print("clicked at", event.x, event.y)
        if (self.frameSideLen - self.margin) > event.x >self.margin and (self.frameSideLen - self.margin) > event.y > self.margin:
            spacing = (self.frameSideLen - 2*self.margin) / 9
            self.cellPosx = int( (event.x - self.margin) // spacing )
            self.cellPosy = int ( (event.y - self.margin) // spacing )

            self.canvas.delete("activeSquare")
            self.canvas.create_rectangle( (self.margin+spacing*self.cellPosx), (self.margin+spacing*self.cellPosy), (self.margin+spacing*(self.cellPosx+1)),
             (self.margin+spacing*(self.cellPosy+1)), width=2.5, outline='red', tags="activeSquare")


    def leftKey(self,event):

        if self.cellPosx == 0:
            self.cellPosx = len(self.board) - 1
        else:
            self.cellPosx -= 1

        spacing = (self.frameSideLen - 2*self.margin) / 9
        self.canvas.delete("activeSquare")
        self.canvas.create_rectangle( (self.margin+spacing*self.cellPosx), (self.margin+spacing*self.cellPosy), (self.margin+spacing*(self.cellPosx+1)),
         (self.margin+spacing*(self.cellPosy+1)), width=2.5, outline='red', tags="activeSquare")

    def rightKey(self,event):

        if self.cellPosx == len(self.board) - 1:
            self.cellPosx = 0
        else:
            self.cellPosx += 1

        spacing = (self.frameSideLen - 2*self.margin) / 9
        self.canvas.delete("activeSquare")
        self.canvas.create_rectangle( (self.margin+spacing*self.cellPosx), (self.margin+spacing*self.cellPosy), (self.margin+spacing*(self.cellPosx+1)),
         (self.margin+spacing*(self.cellPosy+1)), width=2.5, outline='red', tags="activeSquare")

    def upKey(self,event):

        if self.cellPosy == 0:
            self.cellPosy = len(self.board[0]) - 1
        else:
            self.cellPosy -= 1

        spacing = (self.frameSideLen - 2*self.margin) / 9
        self.canvas.delete("activeSquare")
        self.canvas.create_rectangle( (self.margin+spacing*self.cellPosx), (self.margin+spacing*self.cellPosy), (self.margin+spacing*(self.cellPosx+1)),
         (self.margin+spacing*(self.cellPosy+1)), width=2.5, outline='red', tags="activeSquare")

    def downKey(self,event):

        if self.cellPosy == len(self.board[0]) - 1:
            self.cellPosy = 0
        else:
            self.cellPosy += 1

        spacing = (self.frameSideLen - 2*self.margin) / 9
        self.canvas.delete("activeSquare")
        self.canvas.create_rectangle( (self.margin+spacing*self.cellPosx), (self.margin+spacing*self.cellPosy), (self.margin+spacing*(self.cellPosx+1)),
         (self.margin+spacing*(self.cellPosy+1)), width=2.5, outline='red', tags="activeSquare")

    def numberInput(self,event):
        #check that space isn't already occupied
        #print(self.board[self.cellPosy][self.cellPosx], self.cellPosx, self.cellPosy)
        if self.board[self.cellPosy][self.cellPosx] == '0':
            heightGap = (self.height - 2*self.margin) // len(self.board[0])
            widthGap = (self.width - 2*self.margin) // len(self.board[0])

            blockCol = self.cellPosx // 3
            blockRow = self.cellPosy // 3
            blockNum = blockCol + 3*blockRow

            numLabel = 'val' + str(self.cellPosx) + str(self.cellPosy)

            self.board[self.cellPosy][self.cellPosx] = event.char

            if self.isLegalRow(self.cellPosy, self.board) and self.isLegalCol(self.cellPosx, self.board) and self.isLegalBlock(blockNum, self.board):
                # no problem
                self.canvas.create_text(self.margin + (self.cellPosx+0.5)*widthGap, self.margin + (self.cellPosy+0.5)*widthGap, text=self.board[self.cellPosy][self.cellPosx], tags=numLabel, font="Helvetica 12")
            else:
                #problem
                self.canvas.create_text(self.margin + (self.cellPosx+0.5)*widthGap, self.margin + (self.cellPosy+0.5)*widthGap, text=self.board[self.cellPosy][self.cellPosx], tags=numLabel, fill='red', font="Helvetica 12")

            if self.gameWon(self.board) and self.isLegalSudoku(self.board):
                print("You won woot woot!")
                self.canvas.create_text(self.frameSideLen/2, self.frameSideLen/2, text="You won!", tags=numLabel, fill='purple', font="Helvetica 36 bold italic")

    def backspace(self, event):
        if self.initNums[self.cellPosy][self.cellPosx] == 0:
            numLabel = 'val' + str(self.cellPosx) + str(self.cellPosy)
            self.canvas.delete(numLabel)
            self.board[self.cellPosy][self.cellPosx] = '0'

    def gameWon(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '0':
                    return False
        return True



    def playSudoku(self):
        #this isn't even used anymore
        masterBoard, initNums = starterBoard()
        global updateWaiting
        updateWaiting = False

        drawSudoku(TKroot, frameSideLen, frameSideLen, masterBoard, initNums, marginMaster)

        while not gameWon(masterBoard):

            print("oo")
            if updateWaiting:
                drawSudoku(TKroot, frameSideLen, frameSideLen, masterBoard, initNums, marginMaster)
                updateWaiting = False

            #gonna need some more stoofs here



tester = sudoku()

#note: I ran more tests when coding these helper functions but didn't bother
#      writing up assert()s for each special case
assert(tester.isLegalRow(1, tester.board) == True)
assert(tester.isLegalCol(1, tester.board) == True)
assert(tester.isLegalBlock(4, tester.board) == True)
assert(tester.isLegalSudoku(tester.board) == True)
tester.drawSudoku()
