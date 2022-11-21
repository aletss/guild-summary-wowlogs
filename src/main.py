from processing_functions import *
import config
import json
import os

# Paths
CURRENT_PATH = os.getcwd()
REPO_PATH = "/".join(CURRENT_PATH.split("\\")[:-1]) + "/"
DATA_FOLDER_PATH = REPO_PATH + config.DATA_FOLDER
JSON_FOLDER_PATH = REPO_PATH + config.JSON_FOLDER
JSON_FIGHT_FOLDER_PATH = REPO_PATH + config.JSON_FIGHT_FOLDER

# Create json folder if not exist
os.makedirs(JSON_FOLDER_PATH, exist_ok=True)
os.makedirs(JSON_FIGHT_FOLDER_PATH, exist_ok=True)
os.makedirs(DATA_FOLDER_PATH, exist_ok=True)

# List JSONs already loaded
logs_already_loaded = [id.replace(".json", "") for id in os.listdir(JSON_FOLDER_PATH)]

# Get list of logs
logs_guild, status = get_logs_guild(
    guild_name=config.GUILD_NAME,
    server_name = config.SERVER,
    server_region = config.REGION,
    key = config.V1_CLIENT_KEY
    )

# End script if did't get ids
if status != 200:
    print(status)
    exit()

# Save last version with all logs
data_json_path = DATA_FOLDER_PATH + "logs.json"
with open(file=data_json_path, mode="wb") as f:
    f.write(logs_guild)

logs_guild_json = json.loads(logs_guild)

print("Getting logs SUMMARY data")
for log in logs_guild_json:
    title = log["title"]
    owner = log["owner"]
    id = log["id"]
    
    print(f"title: {title}")
    print(f"owner: {owner}")
    print(f"id: {id}")
    print(f"url: https://classic.warcraftlogs.com/reports/{id}/")
    
    # Skip log if already loaded
    if id in logs_already_loaded:
        print("SKIPED. JSON Already loaded\n")
        continue

    # Load data
    log_json, status = get_log_summary(id_log=id, key=config.V1_CLIENT_KEY)
    
    # Break loop if did't get response
    if status != 200:
        print(status)
        break

    # Save data
    log_json_path = JSON_FOLDER_PATH + id + ".json"
    with open(file=log_json_path, mode="wb") as f:
        f.write(log_json)
    


# List JSONs already loaded
fights_already_loaded = [id.replace(".json", "") for id in os.listdir(JSON_FIGHT_FOLDER_PATH)]

print("Getting logs FIGHT data")
for log in logs_guild_json:
    title = log["title"]
    owner = log["owner"]
    id = log["id"]
    
    print(f"title: {title}")
    print(f"owner: {owner}")
    print(f"id: {id}")
    print(f"url: https://classic.warcraftlogs.com/reports/{id}/")
    
    # Skip log if already loaded
    if id in fights_already_loaded:
        print("SKIPED. JSON Already loaded\n")
        continue

    # Load data
    log_json, status = get_log_fight(id_log=id, key=config.V1_CLIENT_KEY)
    
    # Break loop if did't get response
    if status != 200:
        print(status)
        break

    # Save data
    log_json_path = JSON_FIGHT_FOLDER_PATH + id + ".json"
    with open(file=log_json_path, mode="wb") as f:
        f.write(log_json)
    
