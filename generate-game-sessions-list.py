from gameliftFunctions import describeGameSessions
import sys, argparse
from dotenv import load_dotenv
from os import environ

def main():
    try:
        parser = argparse.ArgumentParser(description='Create Game Sessions')
        
        parser.add_argument('-a', '--alias_id', help='Fleet ID', required=False)
        
        arguments = parser.parse_args()
        
        if arguments.alias_id:
            alias_id = arguments.alias_id
        else:
            load_dotenv()            
            alias_id = environ.get('ALIAS_ID')
        print(describeGameSessions(alias_id))
    except Exception as e:
        print(e)
        sys.exit(1)
    
if __name__ == "__main__":
    main()