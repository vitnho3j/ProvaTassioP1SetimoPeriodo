# -*- coding: utf-8 -*-
const_ = 
class Game:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.player1points = 0
        self.player2points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.Player1Score()
        else:
            self.Player2Score()
    
    def score(self):
        result = ""
        if (self.p1points == self.p2points and self.p1points < 3):
            if (self.player1points==0):
                result = "Love"
            if (self.player1points==1):
                result = "Fifteen"
            if (self.player1points==2):
                result = "Thirty"
            result += "-All"
        if (self.player1points==self.player2points and self.player1points>2):
            result = "Deuce"
        
        P1res = ""
        P2res = ""
        if (self.player1points > 0 and self.player2points==0):
            if (self.player1points==1):
                P1res = "Fifteen"
            if (self.player1points==2):
                P1res = "Thirty"
            if (self.player1points==3):
                P1res = "Forty"
            
            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.player2points > 0 and self.player1points==0):
            if (self.player2points==1):
                P2res = "Fifteen"
            if (self.player2points==2):
                P2res = "Thirty"
            if (self.player2points==3):
                P2res = "Forty"
            
            P1res = "Love"
            result = P1res + "-" + P2res
        
        
        if (self.player1points>self.player2points and self.player1points < 4):
            if (self.player1points==2):
                P1res="Thirty"
            if (self.player1points==3):
                P1res="Forty"
            if (self.player2points==1):
                P2res="Fifteen"
            if (self.player2points==2):
                P2res="Thirty"
            result = P1res + "-" + P2res
        if (self.player2points>self.player1points and self.player2points < 4):
            if (self.player2points==2):
                P2res="Thirty"
            if (self.player2points==3):
                P2res="Forty"
            if (self.player1points==1):
                P1res="Fifteen"
            if (self.player1points==2):
                P1res="Thirty"
            result = P1res + "-" + P2res
        
        if (self.player1points > self.player2points and self.player2points >= 3):
            result = "Advantage " + self.player1Name
        
        if (self.player2points > self.player1points and self.player1points >= 3):
            result = "Advantage " + self.player2Name
        
        if (self.player1points>=4 and self.player2points>=0 and (self.player1points-self.player2points)>=2):
            result = "Win for " + self.player1Name
        if (self.p2points>=4 and self.player1points>=0 and (self.player2points-self.player1points)>=2):
            result = "Win for " + self.player2Name
        return result
    
    def SetPlayer1Score(self, number):
        for i in range(number):
            self.P1Score()
    
    def SetPlayer2Score(self, number):
        for i in range(number):
            self.P2Score()
    
    def Player1Score(self):
        self.player1points +=1
    
    
    def Player2Score(self):
        self.player2points +=1
