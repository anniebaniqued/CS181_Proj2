import run_game_michael

p1wins = 0
p2wins = 0
tie = 0
for i in range(500):
	result = run_game_michael.run(None)
	if result == 1:
		p1wins += 1
	if result == 0:
		p2wins += 1
	if result == 2:
		tie += 1


print "Player 1 wins: " + str(p1wins) + " times"
print "Player 2 wins: " + str(p2wins) + " times"
print "Ratio: " + str(float(p1wins)/(p1wins+p2wins))
print "Tie: " + str(tie) + " times"

	