#Function that computes player's score.
def getScore(player):
  #You receive 1 point for each 25 yards of passing
  score = int(player[2])//25
  #Each passing TD is worth 4 points
  score += 4*int(player[3])
  #You receive 1 point for each 10 yards of rushing
  score += int(player[4])//10
  #Each rushing TD is worth 6 points
  score += 6*int(player[5])
  #You receive 1 point for each 10 yards of receiving
  score += int(player[6])//10
  #Each receiving TD is worth 6 points
  score += 6*int(player[7])
  
  return score

#Function that selects player with the best score.
#A player must be of the suitable role and to be not chosen yet.
#The list of roles is roleList, the list of chosen marks is chosen.
def chooseRole(roleList,players,chosen):
  maxI = -1
  maxScore = -1
  
  for I in range(len(players)):
    player = players[I]
    #not chosen and of a suitable role
    if(chosen[I] == 0 and player[0] in roleList):
      score = getScore(player)
      if(score > maxScore): #with maximum score
        maxI = I
        maxScore = score

  if(maxI >= 0):
    chosen[maxI] = 1 #mark the player as chosen
    
  return maxI #returns the number in list
# START OF THE PROGRAM  
players = [] #list of players
chosen  = [] #list of chosen marks

f = open("players.txt","r")
for line in f:
  data = line.split()

  role = data[0]
  name = data[1]
  score = getScore(data)
  #print(role,name,score)

  players.append(data)
  chosen.append(0) #no player is chosen yet

nQB  = chooseRole(["QB"],players,chosen) #choose the best QB
nRB1 = chooseRole(["RB"],players,chosen) #choose the best RB
nRB2 = chooseRole(["RB"],players,chosen) #choose the second best RB
nWR1 = chooseRole(["WR"],players,chosen) #choose the best WR
nWR2 = chooseRole(["WR"],players,chosen) #choose the second best WR
nTE  = chooseRole(["TE"],players,chosen) #choose the best TE
#choose the best of remaining RBs, WRs and TEs
nFLX = chooseRole(["RB", "WR", "TE"],players,chosen)

#output the results
print()
print("QB  " ,players[nQB ][1],getScore(players[nQB ]))
print("RB1 " ,players[nRB1][1],getScore(players[nRB1]))
print("RB2 " ,players[nRB2][1],getScore(players[nRB2]))
print("WR1 " ,players[nWR1][1],getScore(players[nWR1]))
print("WR2 " ,players[nWR2][1],getScore(players[nWR2]))
print("TE  " ,players[nTE ][1],getScore(players[nTE ]))
print("FLEX" ,players[nFLX][1],getScore(players[nFLX]))
