class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        
        team_to_number = dict()
        number_to_team = dict()
        
				# Mapping letter to number sorted by alphabet (To sort)
        for team in sorted(votes[0]):
            number = len(team_to_number)
            team_to_number[team] = number
            number_to_team[number] = team
        
				# ranking[i][j] means how many time team i get rank j
        ranking = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
					# because when tiebreak point, we sort by alphabet => need negative because in the end we sort by reverse
            ranking[i].append(-i) 
            
        for vote in votes:
            for rank, team in enumerate(vote):
                ranking[team_to_number[team]][rank] += 1
        
				# Convert to tuple for sort
        for i in range(n):
            ranking[i] = tuple(ranking[i])
        
        
        ranking.sort(reverse = True)
        result = ""

        for i in range(n):
            result += number_to_team[-ranking[i][n]]
        
        return result