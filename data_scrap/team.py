class Team:
	def __init__(self, name, wins, loses, playoff, color):
		self.name = name
		self.wins = wins
		self.loses = loses
		self.playoff = playoff
		self.color = color

	def display_team(self):
		print(f"team name: {self.name} W: {self.wins} L: {self.loses} Playoff: {self.playoff}")