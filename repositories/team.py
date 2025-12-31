from models.team import Team

teams = []
count = 1

team1 = Team(id=1, name='test team')
teams.append(team1)

class TeamRepo():
    def __init__(self):
        pass

    def get(self, id: int) -> Team:
        # This is like FirstOrDefault of C# or find of JS
        result = next((team for team in teams if team.id == id), None)
        return result
        
    def getAll(self) -> list[Team]:
        return teams

    def add(self, team: Team) -> int:
        global count
        count += 1
        team.id = count
        teams.append(team)
        return count

    def update(self, id: int, team: Team) -> bool:
        updated = False
        result = next((team for team in teams if team.id == id), None)
        if result is not None:
            result.name = team.name
            updated = True
        
        return updated

    def delete(self, id: int) -> bool:
        global teams
        new_teams = [team for team in teams if team.id != id]
        deleted = len(new_teams) != len(teams)
        teams = new_teams
        return deleted