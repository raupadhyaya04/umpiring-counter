def ballIncrement(ball, ballCount, wickets):
    if (ball == "runs" or ball == "wicket" or ball == "dot ball"):
        ballCount += 1
        if (ball == "wicket"):
            wickets += 1
    return ballCount, wickets

def countOver(wickets, overCount, maxWickets):
    ballCount = 0
    while (ballCount != 6):
        ball = input("What happened?\n")
        ballCount, wickets = ballIncrement(ball, ballCount, wickets)
        if wickets == maxWickets:
            break
    if (wickets != maxWickets):
        overCount += 1
    if (ballCount == 6):
        ballCount = 0
    print("Over, change position\nOvers gone:", str(overCount) + "." + str(ballCount), "\nWickets gone:", str(wickets))
    return wickets, overCount

def countInnings(format, maxWickets):
    overCount = 0
    wickets = 0
    while (overCount < format and wickets < maxWickets):
        wickets, overCount = countOver(wickets, overCount, maxWickets)

def countMatch(format): # Might be more frontend
    countInnings(format, 10)

def superOver():
    countInnings(1, 2)
