import json
import os


def importoken(token):
    stuff = {
        "token": token,
        "prefix": f"b!",
        "owner_id": token,
        
    }
    config = "Code\Python_stuff\config.json"
    with open(config,'r') as jsonfile:
        json_content = json.load(jsonfile)
    print("here1")
    try:
        json_content["token"] = token
        with open(config,'w') as jsonfile:
            json.dump(json_content, jsonfile, indent=4)
    except:
        print("Couldn't dump json")
    print("here2")
    return

    
        

    
    