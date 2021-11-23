from gameliftFunctions import describeGameSessions
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
            print(describeGameSessions(fleet_id))
        else:
            parser.print_help()
            sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)
    
if __name__ == "__main__":
    main()