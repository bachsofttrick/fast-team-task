from models.team import Team

teams = []
count = 1

team1 = Team(id=1, name='test team')
teams.append(team1)

class TeamRepo():
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
        for old_team in teams:
            if old_team.id == id:
                old_team.name = team.name
                updated = True
        
        return updated

    @staticmethod
    def delete(id: int) -> bool:
        global teams
        deleted = False
        new_teams = []
        for old_team in teams:
            if old_team.id != id:
                new_teams.append(old_team)
            else:
                deleted = True
        
        teams = new_teams
        return deleted