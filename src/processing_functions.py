import requests

def get_logs_guild(guild_name, server_name, server_region, key):
    """
    Docs: https://classic.warcraftlogs.com/v1/docs/#!/Reports/reports_guild_guildName_serverName_serverRegion_get
    """

    url = f"https://classic.warcraftlogs.com:443/v1/reports/guild/{guild_name}/{server_name}/{server_region}?api_key={key}"
    s = requests.Session()
    r = s.get(url)
    
    if r.status_code!=200:
        print("Status code:", r.status_code)
    
    return r.content, r.status_code

def get_log_summary(id_log, key):
    url = f"https://classic.warcraftlogs.com:443/v1/report/tables/summary/{id_log}?api_key={key}"
    s = requests.Session()
    r = s.get(url)
    
    if r.status_code!=200:
        print("Status code:", r.status_code)
    
    return r.content, r.status_code

def get_log_fight(id_log, key):
    url = f"https://classic.warcraftlogs.com:443/v1/report/fights/{id_log}?api_key={key}"

    s = requests.Session()
    r = s.get(url)
    
    if r.status_code!=200:
        print("Status code:", r.status_code)
    
    return r.content, r.status_code