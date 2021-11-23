import boto3

def getActiveGameSessions(fleetId):
    client = boto3.client('gamelift')
    activeSessionCount = 0
    response = client.describe_game_sessions(
        FleetId=fleetId
    )
    for gameSession in response['GameSessions']:
        if gameSession['Status'] == 'ACTIVE':
            activeSessionCount += 1
    return activeSessionCount
            
def createGameSessions(fleetId, desiredNumberOfSessions=4):
    client = boto3.client('gamelift')
    currentNumberOfSessions = getActiveGameSessions(fleetId)
    if currentNumberOfSessions < desiredNumberOfSessions:
        for i in range(desiredNumberOfSessions - currentNumberOfSessions):
            response = client.create_game_session(
                FleetId=fleetId,
                MaximumPlayerSessionCount=10
            )
            return response
        
def describeGameSessions(fleet_id):
    gameSessionList = []
    client = boto3.client('gamelift')
    response = client.describe_game_sessions(FleetId=fleet_id)
    i = 0
    for gameSession in response['GameSessions']:
        if gameSession['Status'] == 'ACTIVE':
            gameSessionList.append("-sessionId" + alphabet[i] + "=" + gameSession['GameSessionId'])
            i+=1
    return " ".join(gameSessionList)