import tkinter as tk
import numpy as np

def drawPoint(canvas, xPos, yPos, ptRad, colorStr):
    #python_green = "#476042"
    x1, y1 = (xPos - ptRad), (yPos - ptRad)
    x2, y2 = (xPos + ptRad), (yPos + ptRad)
    canvas.create_oval(x1, y1, x2, y2, fill=colorStr, outline="")

def drawSpiralPoints(canvas, xCenter, yCenter, rad):
    ptRad = rad / 50
    for i in range(32):
        #loop through all 32 rings of circles
        tmpRad = i*(rad - 3)/32
        offset = i*(np.pi/4) / 32

        #colors to match larger spiral in assignment
        greenVal = str(hex(int(250 - i*240/32)))[2:]
        while len(greenVal) < 2:
            greenVal = '0' + greenVal

        blueVal = str(hex(int(i*190/32)))[2:]
        while len(blueVal) < 2:
            blueVal = '0' + blueVal

        redVal = str(hex(int(250 - i*150/32)))[2:]
        while len(redVal) < 2:
            redVal = '0' + redVal

        color = "#" + redVal + greenVal + blueVal

        """
        #colors to match smaller spiral in assignment
        greenVal = str(hex(int(255 - i*200/32)))[2:]
        while len(greenVal) < 2:
            greenVal = '0' + greenVal

        blueVal = str(hex(int(i*180/32)))[2:]
        while len(blueVal) < 2:
            blueVal = '0' + blueVal

        color = "#" + '50' + greenVal + blueVal
        """

        for j in range(28):
            #loop through all cirlces in this ring
            angle = j*2*np.pi/28
            drawPoint(canvas, xCenter + tmpRad*np.sin(angle+offset), yCenter + tmpRad*np.cos(angle+offset), ptRad, color)


def drawSpiral(canvas, width, height):
    # 28 arms, 32 circles in each, 45 degrees between first and last in each arm
    # color gradients
    spiral = tk.Canvas(canvas, width=width, height=height)
    spiral.pack()

    #assign margin size to smaller of the two
    if width / 13 > height / 9:
        margin = height / 9
    else:
        margin = width / 13

    #add text
    fontString = 'Arial ' + str(int(margin // 3)) + ' bold'
    spiral.create_text(width/2, margin/2, text='drawSpiral', font=fontString)

    #add LARGE box
    spiral.create_rectangle(margin, margin, width - 6*margin, margin + (width - 7*margin), width=2)

    #add smol box
    spiral.create_rectangle(width - 4.25*margin, 2.5*margin, width-1.25*margin, 5.5*margin, width=2)

    bigCenter = [ (margin + width - 6*margin)/2, (margin + margin + width - 7*margin)/2]
    smolCenter = [ (width - 4.25*margin + width-1.25*margin)/2, (2.5*margin + 5.5*margin)/2]

    bigRad = (width - 7*margin) / 2
    smolRad = 3*margin / 2




    drawSpiralPoints(spiral, bigCenter[0], bigCenter[1], bigRad)
    drawSpiralPoints(spiral, smolCenter[0], smolCenter[1], smolRad)


    TKroot.mainloop()









TKroot = tk.Tk()
drawSpiral(TKroot, 600, 400)
