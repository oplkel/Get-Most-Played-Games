## ik this is prob messy code but idc

from typing import List, Dict, Optional
import pip._vendor.requests as requests
import time
import json

DataObject = Dict[str, int | str]
FinalDataObject = Dict[str, int | str]

finalData: List[FinalDataObject] = []

def fetch(url: str, parameters = None, retries = 5, delay = 1) -> Optional[dict]:
    for attempt in range(retries):
        try:
            response = requests.get(url, params = parameters, timeout = 10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            if attempt == retries - 1:
                print(f"[X] Failed after {retries} retries: {url}")
                return None
            
            time.sleep(delay * (attempt + 1))

def getPlaceId(universeId: str) -> Optional[int]:
    data = fetch(
        "https://games.roproxy.com/v1/games",
        parameters={"universeIds": universeId}
    )

    if not data:
        return None

    try:
        return data["data"][0]["rootPlaceId"]
    except (KeyError, IndexError):
        return None

def getGameName(placeId: int) -> str:
    data = fetch(
        f"https://economy.roproxy.com/v2/assets/{placeId}/details"
    )

    if not data:
        return "Unknown Game"

    return data.get("Name", "Unknown Game")

def convertMinutesToHours(minutes: int) -> float:
    return minutes / 60

def writeJson(data):
    with open("output.json" , "r", encoding="utf-8") as jsonFile:
        fileData = json.loads(jsonFile.read())

    fileData.append(data)

    with open("output.json" , "w", encoding="utf-8") as jsonFile:
        jsonFile.write(json.dumps(fileData))

with open("data.json", "r", encoding="utf-8") as dataJson:
    currentData = json.load(dataJson)

total = len(currentData)

for i, entry in enumerate(currentData, start=1):
    print(f"Processing {i}/{total}")

    placeId = getPlaceId(entry["id"])
    gameName = getGameName(placeId)
    hours = convertMinutesToHours(entry["time_played"])

    if not placeId:
        print(f"[!] Skipping universe {entry['id']}")
        continue

    writeJson({
        "Id": placeId,
        "GameName": gameName,
        "TimePlayed": f"{hours:.2f}hrs",
    })

    finalData.append({
        "Id": placeId,
        "GameName": gameName,
        "TimePlayed": f"{hours:.2f}hrs",
    })
    time.sleep(0.2)

print(f"Completed processing {total}/{total}, the data was outputted into output.json")
