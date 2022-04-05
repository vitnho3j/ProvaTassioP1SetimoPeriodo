# -*- coding: utf-8 -*-
const_Love = 0
const_Fifteen = 15
const_Thirty = 30
const_All = 40

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

    def get_Love():
        return "Love"

    def get_Fifteen():
        return "Fifteen"

    def get_Thirty():
        return "Thirty"


    def get_Forty():
        return "Forty"

    def get_All():
        return "-All"

    def get_Deuce():
        return "Deuce"

    def score(self):
        result = ""
        if (self.p1points == self.p2points and self.p1points < 3):
            if (self.player1points==const_Love):
                result = self.get_Love()
            if (self.player1points==const_Fifteen):
                result = self.get_Fifteen()
            if (self.player1points==const_Thirty):
                result = self.get_Thirty()
            result += self.get_All()

        if (self.player1points==self.player2points and self.player1points > 2):
            result = self.get_Deuce()
        
        P1res = ""
        P2res = ""
        if (self.player1points > 0 and self.player2points==0):
            if (self.player1points==1):
                P1res = self.get_Fifteen()
            if (self.player1points==2):
                P1res = self.get_Thirty()
            if (self.player1points==3):
                P1res = self.get_Forty()
            
            P2res = self.get_Love()
            result = P1res + "-" + P2res
        if (self.player2points > 0 and self.player1points==0):
            if (self.player2points==1):
                P2res = self.get_Fifteen()
            if (self.player2points==2):
                P2res = self.get_Thirty()
            if (self.player2points==3):
                P2res = self.get_Forty()
            
            P1res = self.get_Love()
            result = P1res + "-" + P2res
        
        
        if (self.player1points>self.player2points and self.player1points < 4):
            if (self.player1points==2):
                P1res=self.get_Thirty()
            if (self.player1points==3):
                P1res=self.get_Forty()
            if (self.player2points==1):
                P2res=self.get_Fifteen()
            if (self.player2points==2):
                P2res=self.get_Forty()
            result = P1res + "-" + P2res
        if (self.player2points>self.player1points and self.player2points < 4):
            if (self.player2points==2):
                P2res=self.get_Thirty()
            if (self.player2points==3):
                P2res=self.get_Forty()
            if (self.player1points==1):
                P1res=self.get_Fifteen()
            if (self.player1points==2):
                P1res=self.get_Thirty()
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
