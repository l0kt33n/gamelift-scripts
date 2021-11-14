import boto3

import sys, argparse

def main():
    try:
        parser = argparse.ArgumentParser(description='Create Game Sessions')
        
        parser.add_argument('-f', '--fleet-id', help='Fleet ID', required=True)
        parser.add_argument('-n', '--number-of-sessions', help='Number of sessions', required=True)
        
        arguments = parser.parse_args()
        
        if arguments.fleet_id:
            fleet_id = arguments.fleet_id
            if arguments.number_of_sessions:
                number_of_sessions = int(arguments.number_of_sessions)
                createGameSessions(fleet_id, number_of_sessions)
            else:
                createGameSessions(fleet_id)
        else:
            parser.print_help()
            sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

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
            print(response)
    
if __name__ == "__main__": 
    main()