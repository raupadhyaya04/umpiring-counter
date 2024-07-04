from UmpireLogic import countMatch, superOver
overs = int(input("How many overs per innings in the match?\n"))
countMatch(overs)

result = input("Who won? Team 1 or 2\n")
if result == "draw":
    superOver()