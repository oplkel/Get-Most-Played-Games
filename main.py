"""
--[=[

Author: oplkel
Version: 0.0.2
Updated: January 10, 2026

]=]
"""

## ik this is prob messy code but idc

from typing import List, Dict, Optional
import pip._vendor.requests as requests
import time
import json

maxRetries = 5
requestDelay = 1

DataObject = Dict[str, int | str]
##FinalDataObject = Dict[str, int | str]

##finalData: List[FinalDataObject] = []

with open("data.json", "r", encoding="utf-8") as dataJson:
    currentData = json.load(dataJson)

total = len(currentData)

def fetch(url: str, parameters = None, retries = maxRetries, delay = requestDelay) -> Optional[dict]:
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

def writeJson(data: dict["Id": str, "GameName": str, "TimePlayed": str]):
    with open("output.json" , "r", encoding="utf-8") as outputJson:
        fileData = json.loads(outputJson.read())

    fileData.append(data)

    with open("output.json" , "w", encoding="utf-8") as outputJson:
        outputJson.write(json.dumps(fileData))

def outputData(placeId: str, gameName: str, hours: float) -> None:
    writeJson({
        "Id": placeId,
        "GameName": gameName,
        "TimePlayed": f"{hours:.2f} hours",
    })

    """
    finalData.append({
        "Id": placeId,
        "GameName": gameName,
        "TimePlayed": f"{hours:.2f} hours",
    })
    """
    time.sleep(0.2)

def printExtra() -> None:
    with open("output.json" , "r", encoding="utf-8") as outputJson:
        fileData = json.loads(outputJson.read())

    mostPlayed = fileData[0]
    leastPlayed = fileData[total - 1]
    totalPlayed = 0

    for v in fileData:
        totalPlayed += float(str.split(v["TimePlayed"], " ")[0])
        time.sleep(0.01)

    print(f"Your most played game was {mostPlayed["GameName"]} with {mostPlayed["TimePlayed"]}")
    print(f"Your least played game was {leastPlayed["GameName"]} with {leastPlayed["TimePlayed"]}")
    print(f"You played {round(totalPlayed, 2)} hours in total")

with open("output.json" , "w", encoding="utf-8") as outputJson:
    outputJson.write(json.dumps([]))

if isinstance(currentData, dict):
    for i, v in enumerate(currentData, 1):
        print(f"Processing {i}/{total}")

        placeId = getPlaceId(v["id"])
        gameName = getGameName(placeId)
        hours = convertMinutesToHours(v["time_played"])

        if not placeId:
            print(f"[!] Skipping universe {v["id"]}")
            continue

        outputData(placeId, gameName, hours)
        time.sleep(0.2)
elif isinstance(currentData, list):
    for i, v in enumerate(currentData, 1):
        print(f"Processing {i}/{total}")

        placeId = getPlaceId(v[0])
        gameName = getGameName(placeId)
        hours = convertMinutesToHours(v[1])

        if not placeId:
            print(f"[!] Skipping universe {id[1]}")
            continue

        outputData(placeId, gameName, hours)
        time.sleep(0.2)
else:
    print("An error ocurred when iterating through the raw data: invalid data structure")

print(f"Completed processing {total}/{total}, the data was outputted into output.json")
printExtra()
