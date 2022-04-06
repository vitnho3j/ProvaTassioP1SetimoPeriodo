# -*- coding: utf-8 -*-
const_Love = 0
const_Fifteen = 15
const_Thirty = 30
const_All = 40

class Game:
    def __init__(self, player1Name, player2Name):
        self.__player1Name = player1Name
        self.__player2Name = player2Name
        self.__player1points = 0
        self.__player2points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.Player1Score()
        else:
            self.Player2Score()
            
    def get_Player1Name(self):
        return self.__player1Name
    
    def get_Player2Name(self):
        return self.__player2Name
    
    def get_Player1Points(self):
        return self.__player1points
    
    def get_Player2Points(self):
        return self.__player2points

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
        if (self.get_Player1Points() == self.get_Player2Points() and self.get_Player1Points() < 3):
            if (self.get_Player1Points()==const_Love):
                result = self.get_Love()
            if (self.get_Player1Points()==const_Fifteen):
                result = self.get_Fifteen()
            if (self.get_Player1Points()==const_Thirty):
                result = self.get_Thirty()
            result += self.get_All()

        if (self.get_Player1Points()==self.get_Player2Points() and self.get_Player1Points() > 2):
            result = self.get_Deuce()
        
        Player1result = ""
        Player2result = ""
        if (self.get_Player1Points() > 0 and self.get_Player2Points()==0):
            if (self.get_Player1Points()==1):
                Player1result = self.get_Fifteen()
            if (self.get_Player1Points()==2):
                Player1result = self.get_Thirty()
            if (self.get_Player1Points()==3):
                Player1result = self.get_Forty()
            
            Player2result = self.get_Love()
            result = Player1result + "-" + Player2result
        if (self.get_Player2Points() > 0 and self.get_Player1Points()==0):
            if (self.get_Player2Points()==1):
                Player2result = self.get_Fifteen()
            if (self.get_Player2Points()==2):
                Player2result = self.get_Thirty()
            if (self.get_Player2Points()==3):
                Player2result = self.get_Forty()
            
            Player1result = self.get_Love()
            result = Player1result + "-" + Player2result
        
        
        if (self.get_Player1Points()>self.get_Player2Points() and self.get_Player1Points()< 4):
            if (self.get_Player1Points()==2):
                Player1result=self.get_Thirty()
            if (self.get_Player1Points()==3):
                Player1result=self.get_Forty()
            if (self.get_Player2Points()==1):
                Player2result=self.get_Fifteen()
            if (self.get_Player2Points()==2):
                Player2result=self.get_Forty()
            result = Player1result + "-" + Player2result
        if (self.get_Player2Points()>self.get_Player1Points() and self.get_Player2Points() < 4):
            if (self.get_Player2Points()==2):
                Player2result=self.get_Thirty()
            if (self.get_Player2Points()==3):
                Player2result=self.get_Forty()
            if (self.get_Player1Points()==1):
                Player1result=self.get_Fifteen()
            if (self.get_Player2Points()==2):
                Player1result=self.get_Thirty()
            result = Player1result + "-" + Player2result
        
        if (self.get_Player1Points() > self.get_Player2Points() and self.get_Player2Points() >= 3):
            result = "Advantage " + self.get_Player1Name()
        
        if (self.get_Player2Points() > self.get_Player1Points() and self.get_Player1Points() >= 3):
            result = "Advantage " + self.get_Player2Name()
        
        if (self.get_Player1Points()>=4 and self.get_Player2Points()>=0 and (self.get_Player1Points()-self.get_Player2Points())>=2):
            result = "Win for " + self.get_Player1Name()
        if (self.get_Player2Points()>=4 and self.get_Player1Points()>=0 and (self.get_Player2Points()-self.get_Player1Points())>=2):
            result = "Win for " + self.get_Player2Name()
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
