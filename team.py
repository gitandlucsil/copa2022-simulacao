import random

class Team(object):

    BEST_SCORE = 1837.6 # Brasil (BRA)

    def __init__(self, cellData):
        teamData = cellData.split('|')
        self.name = teamData[0]
        self.score = float(teamData[1])


    def motivate(self):
        """ 
        A pior seleção da copa (GAN, segundo a FIFA) têm 1393.5 de score, o qual equivale a 75% do melhor score (BRA).
        Sendo assim, para que a aleatoriedade não seja tão determinante, podemos definir um intervalo inicial próximo de 75.
        Por exemplo, GAN poderia ter valores entre 70~75 (aproximadamente). Por outro lado, BRA teria 70~100 (maior chance de vitória).
        1837.6 (BRA)  ----- 100
        1393.5 (GAN) -----  X
        """
        self.lastMotivation = random.uniform(70, (self.score * 100)/Team.BEST_SCORE)
        return self.lastMotivation