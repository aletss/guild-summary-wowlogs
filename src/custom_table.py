import config
import os
import json
import pandas as pd

# Paths
CURRENT_PATH = os.getcwd()
REPO_PATH = "/".join(CURRENT_PATH.split("\\")[:-1]) + "/"
DATA_FOLDER_PATH = REPO_PATH + config.DATA_FOLDER
JSON_FIGHT_FOLDER_PATH = REPO_PATH + config.JSON_FIGHT_FOLDER
CSV_FOLDER_PATH = REPO_PATH + config.CSV_FOLDER

WOW_CLASSES = [
    "warrior",
    "priest",
    "druid",
    "warlock",
    "shaman",
    "mage",
    "rogue",
    "paladin",
    "hunter"
]

# Create csv folder if not exist
os.makedirs(CSV_FOLDER_PATH, exist_ok=True)

# List JSONs already loaded
json_already_loaded = [id.replace(".json", "") for id in os.listdir(JSON_FIGHT_FOLDER_PATH)]

# Load basic info from all logs
path = DATA_FOLDER_PATH + "logs.json"
with open(path, encoding='utf-8') as f:
    all_logs_info = json.load(f)

df_all_logs = pd.DataFrame(all_logs_info)
df_all_logs.to_csv(CSV_FOLDER_PATH + "all_logs.csv", encoding="utf8")

# Create csvs
df_fights = pd.DataFrame()
df_friendlies = pd.DataFrame()

print("Creating new CSVs")
for id in json_already_loaded:
    print(id)

    path = JSON_FIGHT_FOLDER_PATH + id + ".json"
    with open(path, encoding='utf-8') as f:
        j = json.load(f)
    
    # Skip if no data
    if len(j["fights"])==0:
        continue

    # Keep only bosses
    boss_fights = [c for c in j['fights'] if c['boss']>0]

    df = pd.DataFrame(boss_fights)
    df['log_id'] = id

    df_fights = df_fights.append(df, ignore_index=True)

    # Keep participants
    friendlies = [c for c in j['friendlies'] if c['type'].lower() in WOW_CLASSES]

    df = pd.DataFrame(friendlies)
    df['log_id'] = id

    df_friendlies = df_friendlies.append(df, ignore_index=True)


df_fights.to_csv(CSV_FOLDER_PATH + "fights.csv", encoding="utf8")
df_friendlies.to_csv(CSV_FOLDER_PATH + "friendlies.csv", encoding="utf8")
