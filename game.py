# -*- coding: utf-8 -*-
from unittest import result


const_Love = 1
const_Fifteen = 2 
const_Thirty = 3
const_All = 4

const_Advantage = "Advantage"
const_Win = "Win For"



result = ""



class Player:
    def __init__(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name

class Game:

    def __init__(self, player1, player2):
        self.__player1Name = player1
        self.__player2Name = player2
        self.__player1points = 0
        self.__player2points = 0
        self.__result = ""
        self.__Player1result = ""
        self.__Player2result = ""


        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.Player1Score()
        else:
            self.Player2Score()


    def get_Player1Name(self):
        return self.__player1Name.getName()
    
    def get_Player2Name(self):
        return self.__player2Name.getName()
        
    
    def get_Player1Points(self):
        return self.__player1points
    
    def get_Player2Points(self):
        return self.__player2points

    def set_Player1Points(self):
        self.__player1points += 1

    def set_Player2Points(self):
        self.__player1points += 1

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


    def result_tying_score(self):
        if (self.get_Player1Points()==const_Love):
            self.__result = self.get_Love()
        if (self.get_Player1Points()==const_Fifteen):
            self.__result = self.get_Fifteen()
        if (self.get_Player1Points()==const_Thirty):
            self.__result = self.get_Thirty()
        self.__result += self.get_All()
        return self.__result



    def result_Player1_Winning(self):
        if (self.get_Player1Points()==1):
            self.__Player1result = self.get_Fifteen()
        if (self.get_Player1Points()==2):
            self.__Player1result = self.get_Thirty()
        if (self.get_Player1Points()==3):
            self.__Player1result = self.get_Forty()
        self.__Player2result = self.get_Love()
        self.__result = self.__Player1result + "-" + self.__Player2result
        return self.__result



    def result_Player2_Winning(self):
        if (self.get_Player2Points()==1):
            self.__Player2result = self.get_Fifteen()
        if (self.get_Player2Points()==2):
            self.__Player2result = self.get_Thirty()
        if (self.get_Player2Points()==3):
            self.__Player2result = self.get_Forty()
            
        self.__Player1result = self.get_Love()
        self.__result = self.__Player1result + "-" + self.__Player2result
        return self.__result



    def result_Player1_Won(self):
        if (self.get_Player1Points()==2):
            self.__Player1result=self.get_Thirty()
        if (self.get_Player1Points()==3):
            self.__Player1result=self.get_Forty()
        if (self.get_Player2Points()==1):
            self.__Player2result=self.get_Fifteen()
        if (self.get_Player2Points()==2):
            self.__Player2result=self.get_Forty()
        self.__result = self.__Player1result + "-" + self.__Player2result
        return self.__result



    def result_Player2_Won(self):
        if (self.get_Player2Points()==2):
            self.__Player2result=self.get_Thirty()
        if (self.get_Player2Points()==3):
            self.__Player2result=self.get_Forty()
        if (self.get_Player1Points()==1):
            self.__Player1result=self.get_Fifteen()
        if (self.get_Player2Points()==2):
            self.__Player1result=self.get_Thirty()
        self.__result = self.__Player1result + "-" + self.__Player2result
        return self.__result


    def score_calculation(self):


        if (self.get_Player1Points() == self.get_Player2Points() and self.get_Player1Points() < 3):
            self.result_tying_score()

        if (self.get_Player1Points()==self.get_Player2Points() and self.get_Player1Points() > 2):
            self.__result = self.get_Deuce()
        



        if (self.get_Player1Points() > 0 and self.get_Player2Points()==0):
            self.result_Player1_Winning()

        if (self.get_Player2Points() > 0 and self.get_Player1Points()==0):
            self.result_Player2_Winning()
        


        
        if (self.get_Player1Points()>self.get_Player2Points() and self.get_Player1Points()< 4):
            self.result_Player1_Won()

        if (self.get_Player2Points()>self.get_Player1Points() and self.get_Player2Points() < 4):
            self.result_Player2_Won()



    def result_score(self):
        
        if (self.get_Player1Points() > self.get_Player2Points() and self.get_Player2Points() >= 3):
            self.__result = const_Advantage + self.get_Player1Name()
        
        if (self.get_Player2Points() > self.get_Player1Points() and self.get_Player1Points() >= 3):
            self.__result = const_Advantage + self.get_Player2Name()
        
        if (self.get_Player1Points()>=4 and self.get_Player2Points()>=0 and (self.get_Player1Points()-self.get_Player2Points())>=2):
            self.__result = const_Win + self.get_Player1Name()

        if (self.get_Player2Points()>=4 and self.get_Player1Points()>=0 and (self.get_Player2Points()-self.get_Player1Points())>=2):
            self.__result = const_Win + self.get_Player2Name()

        return self.__result



    
    def SetPlayer1Score(self, number):
        for i in range(number):
            self.Player1Score()
    
    def SetPlayer2Score(self, number):
        for i in range(number):
            self.Player2Score()


    
    def Player1Score(self):
        self.set_Player1Points()
    
    
    def Player2Score(self):
        self.set_Player2Points()

