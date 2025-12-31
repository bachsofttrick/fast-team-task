from models.team import Team

teams = []
count = 1

team1 = Team(id=1, name='test team')
teams.append(team1)

class TeamRepo():
    @staticmethod
    def get(id: int) -> Team:
        # This is like FirstOrDefault of C# or find of JS
        result = next((team for team in teams if team.id == id), None)
        return result
        
    @staticmethod
    def getAll() -> list[Team]:
        return teams

    @staticmethod
    def add(team: Team) -> int:
        global count
        count += 1
        team.id = count
        teams.append(team)
        return count

    @staticmethod
    def update(id: int, team: Team) -> bool:
        updated = False
        result = next((team for team in teams if team.id == id), None)
        if result is not None:
            result.name = team.name
            updated = True
        
        return updated

    @staticmethod
    def delete(id: int) -> bool:
        global teams
        new_teams = [team for team in teams if team.id != id]
        deleted = len(new_teams) != len(teams)
        teams = new_teams
        return deleted