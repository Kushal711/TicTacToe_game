import tkinter as tk
from tkinter import messagebox
class TicTacToe:
    def __init__(self):
        self.current_player="X"
        self.board=[["","",""],["","",""],["","",""]]
        self.window=tk.Tk()
        self.window.title("TicTacToe")
        self.buttongrid=[]
        for i in range(3):
            row=[]
            for j in range(3):
                button=tk.Button(self.window,text="",width=20,height=10,command=lambda row=i,col=j:self.operations(row,col))
                button.grid(row=i,column=j)
                row.append(button)
            self.buttongrid.append(row)
    
    def operations(self,row,col):
        if self.board[row][col]=="":
            self.board[row][col]=self.current_player
            self.buttongrid[row][col].config(text=self.current_player)
            if self.check_board_win(self.current_player):
                if messagebox.askyesno("Game Over","Winner is "+self.current_player+".Do you want to play it again?"):
                    self.restartgame()
                else:    
                    self.window.destroy()
            elif self.check_board_draw():
                if messagebox.askyesno("Game Over","Game is Draw.Do you want to paly again"):
                    self.restartgame()
                else:
                    self.window.destroy()
                self.window.destroy()
            if self.current_player=="X":
                self.current_player="O"
            else:
                self.current_player="X"

    def check_board_win(self,current_player):
        for i in range(3):
            if current_player==self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return True
            if current_player==self.board[0][i]==self.board[1][i]==self.board[2][i]:
                return True
        if current_player==self.board[0][0]==self.board[1][1]==self.board[2][2]:
            return True
        if current_player==self.board[0][2]==self.board[1][1]==self.board[2][0]:
            return True
        return False
    def check_board_draw(self):
        for i in self.board:
            if "" in i:
                return False
        return True
    def restartgame(self):
        self.current_player = "X"
        self.board = [["","",""],["","",""],["","",""]]
        for row in self.buttongrid:
            for button in row:
                button.config(text="")
        
    def run(self):
        self.window.mainloop()



game=TicTacToe()
game.run()
            
    
