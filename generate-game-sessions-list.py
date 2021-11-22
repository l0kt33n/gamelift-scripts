import boto3
import sys, argparse
import json
import string
alphabet=string.ascii_uppercase

def main():
    try:
        parser = argparse.ArgumentParser(description='Create Game Sessions')
        
        parser.add_argument('-f', '--fleet-id', help='Fleet ID', required=True)
        
        arguments = parser.parse_args()
        
        if arguments.fleet_id:
            fleet_id = arguments.fleet_id
            describeGameSessions(fleet_id)
        else:
            parser.print_help()
            sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
        
def describeGameSessions(fleet_id):
    gameSessionList = []
    client = boto3.client('gamelift')
    response = client.describe_game_sessions(FleetId=fleet_id)
    i = 0
    for gameSession in response['GameSessions']:
        if gameSession['Status'] == 'ACTIVE':
            gameSessionList.append("-sessionId" + alphabet[i] + "=" + gameSession['GameSessionId'])
            i+=1
    print(" ".join(gameSessionList))
    
if __name__ == "__main__":
    main()