# Creating a baseball game 
#https://www.pythontutorial.net/python-oop/python-__repr__/
#https://pythonexamples.org/python-elif-example/


import random
import sys
import os
import time
import datetime

# setting up the variables for the game(types of hits you can get)
SINGLE = 1
DOUBLE = 2
TRIPLE = 3
WALK = 4
HOMERUN = 5
RUN = 6

MAXINNINGS = 9
TOP = 1
BOTTOM = 2

# Function to display per inning stats

def displayPerInningStats(inningsData):
    totalInnings = len(inningsData)
    headerLine = 'Inns: '
    awayLine = 'Away: '
    homeLine = 'Home: '
    finalLine = ''
    bannerLine = '-------'
    awayRuns = 0
    homeRuns = 0
    awayHits = 0
    homeHits = 0

    idx = 0
    totalInns = 0
    for anInningData in inningsData:
        if idx % 2 == 0:
            awayLine += str(anInningData.runs) + '  '
            headerLine += str(anInningData.number) + '  '
            awayRuns += anInningData.runs
            awayHits += anInningData.hits
            totalInns+=1
        else:
            homeLine += str(anInningData.runs) + '  '
            if anInningData.runs == 'X':
                homeRuns += 0
            else:
                homeRuns += anInningData.runs
            
            homeHits += anInningData.hits
        
        idx += 1

    #print('TotalInnings: {}'.format(totalInnings))
    for idx1 in range(totalInns):
        bannerLine += str('---')
    
    headerLine += '  ' + str('R') + '  ' + str('H')
    bannerLine += str('------')
    awayLine += '  ' + str(awayRuns) + '  ' + str(awayHits)
    homeLine += '  ' + str(homeRuns) + '  ' + str(homeHits)

    finalLine = str(bannerLine) + '\n' + str(headerLine) + '\n' + str(bannerLine) + '\n' + str(awayLine) + '\n' + str(homeLine) + '\n' + str(bannerLine)

    return finalLine


# Score Board Class to save the Home and Away team stats.
# A Scoreboard object for home and away team will instantiated

class bbScore(object):
    def __init__(self,tName):
        self.team = str(tName)
        self.hits = 0
        self.single = 0
        self.double = 0
        self.triple = 0
        self.hr = 0
        self.tb = 0
        self.bb = 0
        self.runs = 0
        
    # Update hitcounter for the team depending on the type of hit
    # Also, update other supporting counters for given hit.

    def addHit (self, type):
        if type == 'SINGLE':
            self.single += 1
            self.tb += 1
            self.hits += 1
        elif type == 'DOUBLE':
            self.double += 1
            self.tb += 2
            self.hits += 1
        elif type == 'TRIPLE':
            self.triple += 1
            self.tb += 3
            self.hits += 1
        elif type == 'WALK':
            self.bb += 1
            self.tb += 1
            self.hits += 1
        elif type == 'HOMERUN':
            self.hr += 1
            self.tb += 4
            self.hits += 1
            #print('HR Count: {}'.format(self.hr))
        elif type == 'RUN':
            self.runs += 1
        else: 
            print('Incorrect Hit type: {}'.format(type))

    def __repr__(self):
        #print('++++++++ {} Score Board +++++++++'.format(self.team))
        return('{}: H: {} BB: {} HR: {} TB: {} Runs: {}'.format(self.team,self.hits,self.bb,self.hr,self.tb,self.runs))


# Class to capture current inning stats, 
# It keeps track of inning number, top/bottom, runs scored, runners and outs
class inningStats ():
    def __init__(self,number, whichhalf):
        self.number = number
        self.outs = 0
        self.runs = 0
        self.hits = 0
        self.half = str(whichhalf).upper()
        self.runners = [0,0,0,0]
        self.rnrOnBase = 0
        self.rnrScored = 0

    def __repr__ (self):
        return ('START: {} {}'.format(self.half,self.number))

    def endInningBanner(self):
        return('\nEND: {} {}: {} outs, {} run(s), {} runner(s) left on the bases'.format(self.half,self.number,self.outs,self.runs, (self.rnrOnBase - self.rnrScored)))
        



inning = 1
hitList = ['SINGLE','SINGLE','SINGLE','DOUBLE','DOUBLE','SINGLE','SINGLE','SINGLE','DOUBLE','SINGLE','SINGLE','SINGLE','SINGLE','SINGLE','SINGLE','DOUBLE','DOUBLE','TRIPLE','TRIPLE','HOMERUN','SINGLE','SINGLE','SINGLE','SINGLE','SINGLE','SINGLE']
hitBaseCount = {
    'SINGLE' : 1,
    'DOUBLE' : 2,
    'TRIPLE' : 3,
    'HOMERUN' : 4
}

# Create scoreboard object for Home and Away team
homeSb = bbScore('Home')
awaySb = bbScore('Away')

    
innings = []


#main game loop 

print('///////////////////////////////////////////')
print('GAME START TIME: {}'.format(time.ctime()))
print('///////////////////////////////////////////')
start_time = datetime.datetime.now()

while inning <= MAXINNINGS:
    #printing the game stats for home and away team
    thisInning = inningStats(inning, 'TOP')
    

    print('\n+++++++++++++++++++++++++++++++++++++++')
    print('START Inning {}'.format(inning))
    print('+++++++++++++++++++++++++++++++++++++++')
    print(awaySb)
    print(homeSb)
    print('+++++++++++++++++++++++++++++++++++++++\n')
    
    print('++++++++++++++++++++++++++++++++++++++++++++')
    print(thisInning)
    print('++++++++++++++++++++++++++++++++++++++++++++\n')
    
    #Away team batting
    print("Away team is hitting now\n")
    
    away_outs = 0

    #Loop for the away team's turn for hitting
    #Loop for when you get a hit
    while away_outs < 3:
        if random.random() < 0.3:
            ## Got a base hit. Update the hit in team database and CELEBRATE !!!
            ## Currently I am adding every hit as a "Single" only
            ## This game can be enhanced to derive a random probability of
            ## other types of hits like, doubles, triples, home runs, or even a walk

            thisInning.hits += 1
            whichHit = hitList[random.randint(0,len(hitList)-1)]
            print("It's a hit. {}".format(str(whichHit)))

            awaySb.addHit(str(whichHit))
            
            
            if (thisInning.runners.count('R')) < 4:
                if str(whichHit) == 'HOMERUN':
                    thisInning.runners[3] = 'R'
                    if thisInning.runners.count('R') == 4:
                        # It's a GRAND SLAM !!!

                        print('GRAND SLAM !!!!')
                        thisInning.runs += 4
                        thisInning.rnrOnBase += 1
                        thisInning.rnrScored += 4
                        for i in range(0,4):
                            thisInning.runners[i] = 0
                            awaySb.addHit('RUN')
                    else:
                        #clear the bases
                        howManyOnBase = thisInning.runners.count('R')
                        thisInning.runs += int(howManyOnBase)
                        thisInning.rnrOnBase += 1
                        thisInning.rnrScored += int(howManyOnBase)
                        for i in range(0,4):
                            if thisInning.runners[i] == 'R':
                                awaySb.addHit('RUN')
                            
                            thisInning.runners[i] = 0
                            
                else:
                    # Add the runner to the base queue
                    totalBases = hitBaseCount[str(whichHit)]
                    anyRunnerOnBases = thisInning.runners[:totalBases].count('R')

                    if anyRunnerOnBases == 0:
                        # Nobody on the base Place runner on the base
                        thisInning.runners[totalBases-1] = 'R'
                        thisInning.rnrOnBase += 1
                    elif anyRunnerOnBases > 0:
                        # Somebody on the base. Need to move runners
                        # Currently the game will move the runners on bases by exact number 
                        # of bases the batter got. For.e.g. if there is runner on 2nd and batter
                        # hits a single, runner of 2nd does not move and we have runner on first and second.
                        # if there is runner of 1st and batter hits a single, runner on first will only move
                        # to second. Similary, a runner on first and second and batter hits a single, everyone will
                        # move up one bases. In reality, runner on second could also score. 

                        #print('Moving Runners: {}'.format(thisInning.runners))
                        tIdx = 4
                        for aRunner in thisInning.runners[::-1]:
                            tIdx -= 1
                            if aRunner == 'R':
                                #runPos = thisInning.runners.index(aRunner)
                                runPos = tIdx
                                #print('aRunner: {} Index: {}'.format(aRunner,runPos))
                                moveRunnerIdx = runPos + (totalBases)
                                if moveRunnerIdx > 2:
                                    awaySb.addHit('RUN')
                                    thisInning.runs += 1
                                    print('Runs scored this inning: {}'.format(thisInning.runs))
                                    thisInning.runners[runPos] = 0
                                    thisInning.rnrScored += 1
                                    #print('Moved Runners with runs: {}'.format(thisInning.runners))
                                else:
                                    thisInning.runners[runPos] = 0
                                    thisInning.runners[moveRunnerIdx] = 'R'
                                    
                                    #print('Moved Runners: {}'.format(thisInning.runners))
                        
                        thisInning.rnrOnBase += 1
                        thisInning.runners[totalBases-1] = 'R'
                        #print('Added Runner: {}'.format(thisInning.runners))
                    
        #Hitter getting out
        else: 
            away_outs += 1
            thisInning.outs += 1
            print("Batter's out")
    

    # Print end of the inning stats
    print(thisInning.endInningBanner())
    # Append the inning to the innings list
    innings.append(thisInning)

    # Do we need to play bottom of last inning
    # If the home team is already up in runs at the end of 
    # the top half of last inning, no need to play the bottom
    # half.

    if awaySb.runs < homeSb.runs and inning == MAXINNINGS:
        thisInning = inningStats(inning, 'BOTTOM')
        thisInning.runs = 'X'
        innings.append(thisInning)
        break


    #Home team's turn hitting now
    home_outs = 0 
    
    thisInning = inningStats(inning, 'BOTTOM')

    print('\n++++++++++++++++++++++++++++++++++++++++++++')
    print(thisInning)
    print('++++++++++++++++++++++++++++++++++++++++++++\n')

    print("Home team is hitting now\n")

    #Loop for the home team's turn for hitting

    while home_outs < 3:

        if inning == MAXINNINGS and awaySb.runs < homeSb.runs:
            # If its bottom 9 and we scored winning run before
            # all outs are accounted. Its WALK OFF!!
            
            print('WALK OFF!!!')
            break

        if random.random() < 0.3:

            # If bottom 9 and we have scored winning run then just exit

            


            # Got a base hit. Update the hit in team database and CELEBRATE !!!
            # Currently I am adding every hit as a "Single" only
            # This game can be enhanced to derive a random probability of
            # other types of hits like, doubles, triples, home runs, or even a walk

            thisInning.hits += 1
            whichHit = hitList[random.randint(0,len(hitList)-1)]
            print("It's a hit. {}".format(str(whichHit)))

            homeSb.addHit(str(whichHit))
            
            
            if (thisInning.runners.count('R')) < 4:
                if str(whichHit) == 'HOMERUN':
                    thisInning.runners[3] = 'R'
                    if thisInning.runners.count('R') == 4:
                        # It's a GRAND SLAM !!!
                        print('GRAND SLAM !!!!')
                        thisInning.runs += 4
                        thisInning.rnrOnBase += 1
                        thisInning.rnrScored += 4
                        for i in range(0,4):
                            thisInning.runners[i] = 0
                            homeSb.addHit('RUN')
                    else:
                        #clear the bases
                        howManyOnBase = thisInning.runners.count('R')
                        thisInning.runs += int(howManyOnBase)
                        thisInning.rnrOnBase += 1
                        thisInning.rnrScored += int(howManyOnBase)
                        for i in range(0,4):
                            if thisInning.runners[i] == 'R':
                                homeSb.addHit('RUN')
                            
                            thisInning.runners[i] = 0
                            
                else:
                    # Add the runner to the base queue
                    totalBases = hitBaseCount[str(whichHit)]
                    anyRunnerOnBases = thisInning.runners[:totalBases].count('R')

                    if anyRunnerOnBases == 0:
                        # Nobody on the base Place runner on the base
                        thisInning.runners[totalBases-1] = 'R'
                        thisInning.rnrOnBase += 1
                    elif anyRunnerOnBases > 0:
                        # Somebody on the base. Need to move runners
                        # Currently the game will move the runners on bases by exact number 
                        # of bases the batter got. For.e.g. if there is runner on 2nd and batter
                        # hits a single, runner of 2nd does not move and we have runner on first and second.
                        # if there is runner of 1st and batter hits a single, runner on first will only move
                        # to second. Similary, a runner on first and second and batter hits a single, everyone will
                        # move up one bases. In reality, runner on second could also score. 

                        #print('Moving Runners: {}'.format(thisInning.runners))
                        tIdx = 4
                        for aRunner in thisInning.runners[::-1]:
                            tIdx -= 1
                            if aRunner == 'R':
                                #runPos = thisInning.runners.index(aRunner)
                                runPos = tIdx
                                #print('aRunner: {} Index: {}'.format(aRunner,runPos))
                                moveRunnerIdx = runPos + (totalBases)
                                if moveRunnerIdx > 2:
                                    homeSb.addHit('RUN')
                                    thisInning.runs += 1
                                    print('Runs scored this inning: {}'.format(thisInning.runs))
                                    thisInning.runners[runPos] = 0
                                    thisInning.rnrScored += 1
                                    #print('Moved Runners with runs: {}'.format(thisInning.runners))
                                else:
                                    thisInning.runners[runPos] = 0
                                    thisInning.runners[moveRunnerIdx] = 'R'
                                    
                                    #print('Moved Runners: {}'.format(thisInning.runners))
                        
                        thisInning.rnrOnBase += 1
                        thisInning.runners[totalBases-1] = 'R'
                        #print('Added Runner: {}'.format(thisInning.runners))
                        
        #Hitter getting out
        else: 
            home_outs += 1
            thisInning.outs += 1
            print("Batter's out")


    
    # Print end of the inning stats
    print(thisInning.endInningBanner())
    # Append the inning to the innings list
    innings.append(thisInning)

    # Increment the inning counter
    #time.sleep(1)
    inning+=1

print('\nGAME END TIME: {}'.format(time.ctime()))
end_time = datetime.datetime.now()

print('\n+++++++++++++++++++++++++++++++++++++++')
print('              FINAL SCORE                ')
print('+++++++++++++++++++++++++++++++++++++++')
print(awaySb)
print(homeSb)
print('+++++++++++++++++++++++++++++++++++++++\n')

print(displayPerInningStats(innings))

if awaySb.runs > homeSb.runs:
    print('\nAWAY Team Wins!!!')
elif awaySb.runs < homeSb.runs:
    print('\nHOME Team Wins!!!')
elif awaySb.runs == homeSb.runs:
    print('\nGAME IS TIED!!!')

print()
print('GAME Duration: {}'.format(str(end_time - start_time)))

