from gameliftFunctions import createGameSessions
import sys, argparse
import dotenv

def main():
    try:
        parser = argparse.ArgumentParser(description='Create Game Sessions')
        
        parser.add_argument('-a', '--alias-id', help='Alias ID', required=False)
        parser.add_argument('-n', '--number-of-sessions', help='Number of sessions', required=False)
        
        arguments = parser.parse_args()
        
        if arguments.alias_id:
            alias_id = arguments.alias_id
        else:
            from dotenv import load_dotenv
            load_dotenv()
            from os import environ
            alias_id = environ.get('ALIAS_ID')
        if arguments.number_of_sessions:
            number_of_sessions = int(arguments.number_of_sessions)
        else:
            number_of_sessions = 10
        print(createGameSessions(alias_id, number_of_sessions))

    except Exception as e:
        print(e)
        sys.exit(1)
    
if __name__ == "__main__": 
    main()