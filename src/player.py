import requests
import json

with open('data/api_config.json', 'r') as config_file :
    config_file = json.load(config_file)

class PlayerMethod:

    @staticmethod
    def get_informations(player_id : str, write_json = False):

        """Give API informations from an account

        Args:
            player_id (str): Player ID without #
            write_json (bool, optional): If function write a json file with API results informations. Defaults to False.

        Returns:
            json: A json object with API results
        """

        url = f"https://api.clashroyale.com/v1/players/%23{player_id}"
        headers_dict = {
            'Accept' : 'application/json',
            'authorization' : f"Bearer {config_file['token']}"
        }
        result = requests.get(url, headers=headers_dict)

        if not write_json :
            return result.json()
        else :
            with open('player_result.json', 'w') as result_file :
                json.dump(result.json(), result_file)
            return result.json()
        
    @staticmethod
    def get_next_chest(player_id : str, write_json = False):

        """Give API informations about given player next chests

        Args:
            player_id (str): Player ID without #
            write_json (bool, optional): If function write a json file with API results informations. Defaults to False.

        Returns:
            json: A json object with API results
        """
        url = f"https://api.clashroyale.com/v1/players/%23{player_id}/upcomingchests"
        headers_dict = {
            'Accept' : 'application/json',
            'authorization' : f"Bearer {config_file['token']}"
        }   
        result = requests.get(url, headers=headers_dict)

        if not write_json :
            return result.json()
        else :
            with open('chest_result.json', 'w') as result_file :
                json.dump(result.json(), result_file)
            return result.json()

    @staticmethod
    def battles_results(player_id : str, write_json = False):

        """Give API informations about given player battle results

        Args:
            player_id (str): Player ID without #
            write_json (bool, optional): If function write a json file with API results informations. Defaults to False.

        Returns:
            json: A json object with API results
        """

        url = f"https://api.clashroyale.com/v1/players/%23{player_id}/battlelog"
        headers_dict = {
            'Accept' : 'application/json',
            'authorization' : f"Bearer {config_file['token']}"
        }   
        result = requests.get(url, headers=headers_dict)

        if not write_json :
            return result.json()
        else :
            with open('battle_result.json', 'w') as result_file :
                json.dump(result.json(), result_file)
            return result.json()


class Player:
    """ A Player classes for use all player methods with a specific ID
    """

    def __init__(self, player_id : str):

        """Initialize a player instance in API

        Args:
            player_id (str): Player ID without #
        """

        self.player_id = player_id
    
    def __str__(self) -> str:
        """Return str representation of this object

        Returns:
            str: str representation of this object
        """
        return f"Player : {str({'player_id' : self.player_id})}"
    
    def informations(self):
        """Give API informations about player

        Returns:
            json: A json object with API results
        """
        return PlayerMethod.battles_results(self.player_id)
    
    def next_chest(self):
        """Give API informations about player's nexts chests

        Returns:
            json: A json object with API results
        """
        return PlayerMethod.get_next_chest(self.player_id)
    
    def battles(self):
        """Give API informations about player's battles

        Returns:
            json: A json object with API results
        """
        return PlayerMethod.battles_results(self.player_id, write_json=False)