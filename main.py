from team import Team
import pandas as pd

class Main(object):

    def __init__(self):
        df = pd.read_csv('https://raw.githubusercontent.com/digitalinnovationone/live-coding-evitando-o-7x1-com-python-e-sql/main/data.csv')
        df.head()
        print(df)
        # Mapa em que a chave será a letra do grupo e o valor as seleções (que ordenaremos pelas "melhores").
        bestTeamsByGroup = {}
        # Percorre o dataframe (dados do CSV) para criar nossos objetos/seleções.
        for label, content in df.items():
            team1 = Team(content[0])
            team2 = Team(content[1])
            team3 = Team(content[2])
            team4 = Team(content[3])
            bestTeamsByGroup[label] = sorted([team1, team2, team3, team4], key=Team.motivate, reverse=True)
        for group, motivatedTeams in bestTeamsByGroup.items():
            print(f'Grupo {group}: ', end = "")
            for team in motivatedTeams:
                print(f'{team.name} ({team.lastMotivation:.2f})', end="")
            print()
        # Criando vaiáveis para as 2 melhores seleções de cada grupo:
        team1A = bestTeamsByGroup['A'][0]
        team2A = bestTeamsByGroup['A'][1]
        team1B = bestTeamsByGroup['B'][0]
        team2B = bestTeamsByGroup['B'][1]
        team1C = bestTeamsByGroup['C'][0]
        team2C = bestTeamsByGroup['C'][1]
        team1D = bestTeamsByGroup['D'][0]
        team2D = bestTeamsByGroup['D'][1]
        team1E = bestTeamsByGroup['E'][0]
        team2E = bestTeamsByGroup['E'][1]
        team1F = bestTeamsByGroup['F'][0]
        team2F = bestTeamsByGroup['F'][1]
        team1G = bestTeamsByGroup['G'][0]
        team2G = bestTeamsByGroup['G'][1]
        team1H = bestTeamsByGroup['H'][0]
        team2H = bestTeamsByGroup['H'][1]
        # Confronto oitavas
        print('Oitavas')
        quarter1 = self.match(team1A, team2B)
        quarter2 = self.match(team1C, team2D)
        quarter3 = self.match(team1E, team2F)
        quarter4 = self.match(team1G, team2H)
        quarter5 = self.match(team1B, team2A)
        quarter6 = self.match(team1D, team2C)
        quarter7 = self.match(team1F, team2E)
        quarter8 = self.match(team1H, team2G)
        # Confronto quartas
        print('Quartas')
        semi1 = self.match(quarter1, quarter2)
        semi2 = self.match(quarter3, quarter4)
        semi3 = self.match(quarter5, quarter6)
        semi4 = self.match(quarter7, quarter8)
        # Confronto semifinal
        print('Semi')
        final1 = self.match(semi1, semi2) 
        final2 = self.match(semi3, semi4) 
        # Confronto final
        print('Final')
        champion = self.match(final1, final2)


    def match(self, team1, team2):
        team1.motivate()
        team2.motivate()
        print(f'{team1.name} ({team1.lastMotivation:.2f}) x {team2.name} ({team2.lastMotivation:.2f})')
        return team1 if team1.lastMotivation > team2.lastMotivation else team2

def main():
    mainClass = Main()

if __name__ == "__main__":
    main()
