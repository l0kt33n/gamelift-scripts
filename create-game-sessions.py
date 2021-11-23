from gameliftFunctions import createGameSessions

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
                print(createGameSessions(fleet_id, number_of_sessions))
            else:
                print(createGameSessions(fleet_id))
        else:
            parser.print_help()
            sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
    
if __name__ == "__main__": 
    main()