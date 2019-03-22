'''
Created on 12-Mar-2019

@author: guruk
'''

class football:
    
    def __init__(self, name, country):
        self.name= name
        self.country = country
    
    def club(self, player):
        self.player = player
        print("{} is the best club in the {}".format(self.name,self.country ))
        print("{} is my favourite player in {}".format(self.player, self.name))

barcelona = football("Barcelona", 'Spain')
arsenal = football("Arsenal", 'England')

arsenal.club('Monreal')


print('------------------------')


barcelona.club('Messi')
