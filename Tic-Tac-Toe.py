# Tic-Tac-Toe Game

from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import random
import sys


FONT_L = ("Cooper black", 12)
class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.StartAndEnd()
        self.Player = 'X'
        self.Computer = 'O'
        self.MainPadButton()
        self.ButtonList = [self.btn1, self.btn2, self.btn3, self.btn4,
                           self.btn5, self.btn6, self.btn7, self.btn8, self.btn9]
        self.originalX = Image.open('imageX.png')
        self.imgX = ImageTk.PhotoImage(self.originalX)
        self.originalO = Image.open('imageO.png')
        self.imgO = ImageTk.PhotoImage(self.originalO)
        self.gameOn = False
        self.ply = True
        self.board = ['', '', '', '', '', '', '', '', '']
        self.move = 0
        self.turn = "player"
        self.whoPlays = self.Player
        self.turnSignal = True
        self.InitWindow()
        tkinter.messagebox.showinfo('Tic-Tac-Toe',
            'WELCOME TO TIC-TAC-TOE\n Click the "Play" button to start and the "End" button to quit')
        self.lengthP = 0
        self.lengthC = 0
                
    def InitWindow(self):
        self.master.title("Tic-Tac-Toe")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)
        
        file = Menu(menu)
        file.add_command(label = 'Play With "X" ', command = self.PlayX)
        file.add_command(label = 'Play With "O" ', command = self.PlayO)
        file.add_command(label = 'Go First ', command = self.goFirst)
        file.add_command(label = 'Go Second ', command = self.goSecond)
        file.add_command(label = 'Exit', command = self.ClientExit)
        menu.add_cascade(label = 'Game', menu=file)      

    def StartAndEnd(self):
        self.topFrame = Frame(self.master)
        self.topFrame.pack(side = TOP)
        self.btnPlay = Button(self.topFrame, padx = 66, pady = 5, bd = 20, text = "PLAY",
          activebackground = "Green", bg = "Green", fg="Yellow", font = FONT_L,
          command = self.StartGame)
        self.btnPlay.config()
        self.btnPlay.pack(side = LEFT)

        self.btnEnd = Button(self.topFrame, padx = 66, pady = 5, bd = 20, text = "END",
          activebackground = "Red", bg = "Red", fg="Yellow", font = FONT_L,
          command = self.ClientExit)
        self.btnEnd.pack(side = RIGHT)
        
    def StartGame(self):

        self.btnPlay.config(relief = SUNKEN)
        self.gameOn = True
        if self.turn == "computer":
            random.seed()
            self.turnSignal = False
            self.move = random.randint(0,8)
            self.CmdPlayPad(self.move)
        
    def ClientExit(self):
        reply = tkinter.messagebox.askquestion("Exit", "Are you sure, you want exit the program?")
        if reply == 'yes':
            self.master.destroy()
                
    def MainPadButton(self):
        self.nextFrame = Frame(self.master)
        self.nextFrame.pack(side = TOP)
        self.btn1 = Button(self.nextFrame, padx = 52, pady = 52, bd = 20,
            bg = "grey", command = lambda: self.CmdPlayPad(0),
            activebackground = "grey")             
        self.btn1.pack(side = LEFT)
        self.btn2 = Button(self.nextFrame, padx = 52, pady = 52, bd = 20,
            bg = "grey", command = lambda: self.CmdPlayPad(1),
            activebackground = "grey")
        self.btn2.pack(side = LEFT)
        self.btn3 = Button(self.nextFrame, padx = 52, pady = 52, bd = 20, 
            bg = "grey", command = lambda: self.CmdPlayPad(2),
            activebackground = "grey")
        self.btn3.pack(side = LEFT)

        self.middleFrame = Frame(self.master)
        self.middleFrame.pack(side = TOP)

        self.btn4 = Button(self.middleFrame, padx = 52, pady = 52, bd = 20,
            bg = "grey", command = lambda: self.CmdPlayPad(3),
            activebackground = "grey")
        self.btn4.pack(side = LEFT)
        self.btn5 = Button(self.middleFrame, padx = 52, pady = 52, bd = 20, 
            bg = "grey", command = lambda: self.CmdPlayPad(4),
            activebackground = "grey")
        self.btn5.pack(side = LEFT)
        self.btn6 = Button(self.middleFrame, padx = 52, pady = 52, bd = 20, 
            bg = "grey", command = lambda: self.CmdPlayPad(5),
            activebackground = "grey")
        self.btn6.pack(side = LEFT)

        self.bottomFrame = Frame(self.master)
        self.bottomFrame.pack(side = TOP)

        self.btn7 = Button(self.bottomFrame, padx = 52, pady = 52, bd = 20,
            bg = "grey", command = lambda: self.CmdPlayPad(6),
            activebackground = "grey")
        self.btn7.pack(side = LEFT)
        self.btn8 = Button(self.bottomFrame, padx = 52, pady = 52, bd = 20, 
            bg = "grey", command = lambda: self.CmdPlayPad(7),
            activebackground = "grey")
        self.btn8.pack(side = LEFT)
        self.btn9 = Button(self.bottomFrame, padx = 52, pady = 52, bd = 20,
            bg = "grey", command = lambda: self.CmdPlayPad(8),
            activebackground = "grey")
        self.btn9.pack(side = LEFT)
        
    def CmdPlayPad(self, index):
        if self.board[index] == '':
            if self.ply:
                if self.Player == 'X' and self.gameOn:
                    if self.turnSignal:
                        self.ButtonList[index].config(relief=SUNKEN, bg = "sandybrown", image = self.imgX)
                        self.board[index] = self.Player
                    self.computerMove()
                    
                elif self.Player == 'O' and self.gameOn:
                    if self.turnSignal:
                        self.ButtonList[index].config(relief=SUNKEN, bg = "cyan", image = self.imgO)
                        self.board[index] = self.Player
                    self.computerMove()
                    
            playerWin = self.winner(self.board, self.Player)
            computerWin = self.winner(self.board, self.Computer)
            
            if (playerWin and computerWin):
                tkinter.messagebox.showinfo('Game result', 'The game is draw')
                self.ply = False
            elif (playerWin):
                tkinter.messagebox.showinfo('Game result', 'Congratulations! You won!')
                self.ply = False
            elif (computerWin):
                tkinter.messagebox.showinfo('Game result', 'Game over, You lost.')
                self.play = False
            elif self.checkFull():
                tkinter.messagebox.showinfo('Game result', 'The game is draw')
                self.ply = False

    def ListAndLength(self, char):
        charList = []
        length = 0
        for i, j in enumerate(self.board):
            if j == char:
                charList.append(i)
                length += 1
        return charList, length
         
    def computerMove(self):
        ply, self.lengthP = self.ListAndLength(self.Player)
        com, self.lengthC = self.ListAndLength(self.Computer)
        option = True
        if self.Player == "X":
            backGround = "cyan",
            iDisplay = self.imgO
        else:
            backGround = "sandybrown"
            iDisplay = self.imgX            
                          
        if self.board[4] == '':
            self.move = 4
        else:
            if 4 in com:
                if self.lengthC > 1:
                    if com[0] == 4 and self.board[8 - com[1]] == '':
                        self.move = 8 - com[1]
                    elif com[0] < 4 and self.board[8 - self.move] == '':
                        self.move = 8 - self.move
                    else:
                        random.seed()
                        self.move = random.randint(0,8)
                        while(self.board[self.move] != ''):
                            self.move = random.randint(0,8)
                            if self.checkFull():
                                option = False
                                break
                        
                else:
                    if 8 - ply[0] > 2 and self.board[6 - ply[0]] == '':
                        self.move = 6 - ply[0]
                    elif self.board[10 - ply[0]] == '':
                        self.move = 10 - ply[0]
                    else:
                        random.seed()
                        self.move = random.randint(0,8)
                        while(self.board[self.move] != ''):
                            self.move = random.randint(0,8)
                            if self.checkFull():
                                option = False
                                break
                        
            else:
                if self.board[8 - ply[0]] == '':
                    self.move = 8 - ply[0]
                else:
                    random.seed()
                    self.move = random.randint(0,8)
                    while(self.board[self.move] != ''):
                        self.move = random.randint(0,8)
                        if self.checkFull():
                            option = False
                            break

        if option:
            self.ButtonList[self.move].config(relief=SUNKEN, bg = backGround, image = iDisplay)
            self.board[self.move] = self.Computer
        self.turnSignal = True
                
    def winner(self, board, letter):
        if (
        (self.board[0] == self.board[1] == self.board[2] == letter) or
        (self.board[3] == self.board[4] == self.board[5] == letter) or
        (self.board[6] == self.board[7] == self.board[8] == letter) or
        (self.board[0] == self.board[3] == self.board[6] == letter) or
        (self.board[1] == self.board[4] == self.board[7] == letter) or
        (self.board[2] == self.board[5] == self.board[8] == letter) or
        (self.board[0] == self.board[4] == self.board[8] == letter) or
        (self.board[2] == self.board[4] == self.board[6] == letter)):
            return (True)
        else:
            return (False)
        
    def checkFull(self):
        x = '' in self.board        
        if x:
            return False
        else:
            return True
        
    def PlayX(self):
        self.Player = 'X'
        self.Computer = 'O'
        tkinter.messagebox.showinfo('Player Name', "You play ' X '")
        
    def PlayO(self):
        self.Player = 'O'
        self.Computer = 'X'
        tkinter.messagebox.showinfo('Player Name', "You play ' O '")


    def goFirst(self):
        self.turn = 'player'
        tkinter.messagebox.showinfo('First move', 'You move first')

    def goSecond(self):
        self.turn = 'computer'
        tkinter.messagebox.showinfo(' First move', 'The computer moves first') 

    def playAgain(self):
        Application()


root = Tk()
app = Application(root)
root.mainloop()
