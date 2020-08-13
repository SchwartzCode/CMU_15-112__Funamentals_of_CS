import tkinter as tk
import random

class tetrisPiece(object):
    iPiece = [
        [  True,  True,  True,  True ]
    ]

    jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]

    lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]
    ]

    oPiece = [
        [  True,  True ],
        [  True,  True ]
    ]

    sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]

    tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]

    zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]
    ]

    tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece ]
    colorOptions = ["red", "yellow", "magenta", "pink", "cyan", "green", "orange"]

    def __init__(self):
        self.piece = self.tetrisPieces[ int(random.random()*7) ]
        self.color = self.colorOptions[ int(random.random()*7) ]
        self.xLoc = 4
        # idea of these conditionals was to have it so only bottom row printed
        #if len(self.piece[:][0]) == 1:
        #    self.yLoc = 0
        #else:
        #   self.yloc = -1
        self.yLoc = 0




class tetrisGame(object):

    def __init__(self, width = 400, margin = 40):
        self.TKroot = tk.Tk()

        self.boxWidth = (width - 2*margin) / 10

        self.width = width
        self.height = 2*margin + 15*self.boxWidth
        self.margin = margin

        self.board = [ ['gray']*10 for i in range(15)]
        self.score = 0
        self.gameRunning = False



        self.canvas = tk.Canvas(self.TKroot, width=self.width, height=self.height)
        self.canvas.bind("<Button-1>", self.handleClick)
        self.canvas.bind("<space>", self.rotatePiece)
        self.canvas.bind("<Left>", self.leftKey)
        self.canvas.bind("<Right>", self.rightKey)
        self.canvas.bind("<Down>", self.downKey)
        self.canvas.focus_set() #need this for canvas to detect arrow key presses
        self.canvas.pack()

    def drawTetris(self):
        #fill in background orange and fill tetris board in gray
        self.canvas.create_rectangle(0,0,self.width,self.height,fill='orange',outline="")
        self.canvas.create_text(self.width/2, self.margin/2,text=('Score: ' + str(self.score)), fill='purple', tags='score', font="Arial 14 bold")


        for i in range(16):
            # horizontal lines
            self.canvas.create_line(self.margin, self.margin+i*self.boxWidth, self.width - self.margin,  self.margin+i*self.boxWidth, width=2.5)
            if (i<11):
                # vertical lines
                self.canvas.create_line(self.margin+i*self.boxWidth, self.margin, self.margin+i*self.boxWidth, self.height - self.margin, width=2.5)

        self.fillBoard()

        self.canvas.create_oval(self.width/2 - 100, self.height/2 - 100, self.width/2 + 100, self.height/2 + 100, fill='purple', outline='', tags='startScreen')
        self.canvas.create_text(self.width/2, self.height/2, fill='white', text='Click to start!', font="Arial 20 bold", tags='startScreen')


        self.TKroot.mainloop()

    def fillBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.canvas.create_rectangle(self.margin+j*self.boxWidth, self.margin+i*self.boxWidth, self.margin+(j+1)*self.boxWidth, self.margin+(i+1)*self.boxWidth, fill=self.board[i][j], width=2.5)

    def updateScore(self):
        self.canvas.delete('score')
        self.canvas.create_text(self.width/2, self.margin/2,text=('Score: ' + str(self.score)), fill='purple', tags='score', font="Arial 14 bold")

    def handleClick(self, event):
        if not self.gameRunning:
            self.canvas.delete('startScreen')
            self.gameRunning = True

            self.activePiece = tetrisPiece()

            # if you want pieces to only drop one layer in to start
            #for i in range(len(self.activePiece.piece[-1])):
            #    if self.activePiece.piece[-1][i]:
            #        self.canvas.create_rectangle(self.margin+(i+self.activePiece.xLoc)*self.boxWidth, self.margin+(self.activePiece.yLoc)*self.boxWidth,
            #            self.margin+(i+1+self.activePiece.xLoc)*self.boxWidth, self.margin+(1+self.activePiece.yLoc)*self.boxWidth, fill=self.activePiece.color, width=2.5, tags='activePiece')

            #self.TKroot.after(750, self.updateClock)

            self.drawPiece()
            self.updateClock()

    def rotatePiece(self, event):
        print("shmoopie")
        print(self.activePiece.piece)
        self.activePiece.piece = list(zip(*self.activePiece.piece[::-1]))
        print(self.activePiece.piece, "\n\n")

    def leftKey(self, event):
        print("LEFT")
        if self.activePiece.xLoc != 0:
            self.activePiece.xLoc -= 1
            self.drawPiece()


    def rightKey(self, event):
        print("RIGHT")
        if self.activePiece.xLoc + len(self.activePiece.piece) < 9:
            self.activePiece.xLoc += 1
            self.drawPiece()

    def downKey(self, event):
        print("DOWN")
        self.activePiece.yLoc += 1
        self.drawPiece()

    def pieceTouch(self):
        #returns true if activePiece is touching old pieces left on board, false if not
        return False

    def mergePiece(self):
        #merges active piece and background
        print('merging piece')

    def drawPiece(self):
        if self.activePiece.yLoc == 14 or self.pieceTouch():
            self.mergePiece()
        else:
            self.canvas.delete('activePiece')
            #if self.activePiece.yLoc == 0:
            #    print('oi')
            #    print(self.activePiece.piece)
            #    for i in range(len(self.activePiece.piece[-1])):
            #        self.canvas.create_rectangle(self.margin+(i+self.activePiece.xLoc)*self.boxWidth, self.margin+(self.activePiece.yLoc)*self.boxWidth,
            #            self.margin+(i+1+self.activePiece.xLoc)*self.boxWidth, self.margin+(1+self.activePiece.yLoc)*self.boxWidth, fill=self.activePiece.color, width=2.5, tags='activePiece')
            #fix this so that it draws from bottom left corner instead of top left
            #else:
            for i in range(len(self.activePiece.piece)):
                for j in range(len(self.activePiece.piece[0])):
                    if self.activePiece.piece[i][j] == True:
                        self.canvas.create_rectangle(self.margin+(j+self.activePiece.xLoc)*self.boxWidth, self.margin+(i+self.activePiece.yLoc)*self.boxWidth,
                            self.margin+(j+1+self.activePiece.xLoc)*self.boxWidth, self.margin+(i+1+self.activePiece.yLoc)*self.boxWidth, fill=self.activePiece.color, width=2.5, tags='activePiece')

    def updateClock(self):
        print(self.score)
        self.drawPiece()
        self.activePiece.yLoc += 1

        self.TKroot.after(750, self.updateClock)

test = tetrisGame()

test.drawTetris()
#test.fillBoard()

oop = tetrisPiece()

print(oop.color, oop.piece)
