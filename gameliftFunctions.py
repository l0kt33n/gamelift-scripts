import boto3
import string
alphabet=string.ascii_uppercase

def getActiveGameSessions(alias):
    client = boto3.client('gamelift')
    activeSessionCount = 0
    response = client.describe_game_sessions(
        AliasId=alias
    )
    for gameSession in response['GameSessions']:
        if gameSession['Status'] == 'ACTIVE':
            activeSessionCount += 1
    return activeSessionCount
            
def createGameSessions(alias, desiredNumberOfSessions):
    client = boto3.client('gamelift')
    currentNumberOfSessions = getActiveGameSessions(alias)
    responseList = []
    if currentNumberOfSessions < desiredNumberOfSessions:
        for i in range(desiredNumberOfSessions - currentNumberOfSessions):
            response = client.create_game_session(
                AliasId=alias,
                MaximumPlayerSessionCount=desiredNumberOfSessions
            )
            responseList.append(response)
    return responseList
        
def describeGameSessions(alias):
    gameSessionList = []
    client = boto3.client('gamelift')
    response = client.describe_game_sessions(AliasId=alias)
    i = 0
    for gameSession in response['GameSessions']:
        if gameSession['Status'] == 'ACTIVE':
            gameSessionList.append("-sessionId" + alphabet[i] + "=" + gameSession['GameSessionId'])
            i+=1
    return " ".join(gameSessionList)