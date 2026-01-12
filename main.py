"""
--[=[

Author: oplkel
Version: 0.1.0
Notes: For README.md go to https://github.com/oplkel/Get-Most-Played-Games
Updated: January 10, 2026

]=]
"""

## ik this is prob messy code but idc

import pip._vendor.requests as requests
import time
import json

maxRetries = 3 ## Default: 3
requestDelay = 1 ## Default: 1

with open("data.json", "r", encoding="utf-8") as dataJson:
    currentData = json.load(dataJson)

total = len(currentData)

def formatData(data: dict | list) -> tuple[str, int] | None:
    if isinstance(data, dict):
        return data["id"], data["time_played"]
    elif isinstance(data, list):
        return data[0], data[1]
    else:
        print("An error ocurred when iterating through the raw data: invalid data structure") ## Your data format is invalid; look at the guides in README.md.
        return

def fetch(url: str, parameters=None, retries=maxRetries, delay=requestDelay) -> dict | None:
    for attempt in range(retries):
        try:
            response = requests.get(url, params = parameters, timeout = 10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            if attempt == retries - 1:
                print(f"[X] Failed after {retries} retries: {url}") ## It failed to get game data after the max amount of retries
                return
            
            time.sleep(delay * (attempt + 1))

def getGameData(universeId: str) -> None | dict:
    data = fetch(
        "https://games.roproxy.com/v1/games",
        parameters = { "universeIds": universeId }
    )

    if not data:
        return

    try:
        return data["data"][0]
    except:
        return

def convertMinutesToHours(minutes: int) -> float:
    return minutes / 60

def writeJson(data: dict[ "UniverseId": int, "PlaceId": int, "GameName": str, "Creator": str, "TimePlayed": str] ):
    with open("output.json" , "r", encoding="utf-8") as outputJson:
        fileData = json.loads(outputJson.read())

    fileData.append(data)

    with open("output.json" , "w", encoding="utf-8") as outputJson:
        outputJson.write(json.dumps(fileData))

def outputData(universeId: int, placeId: int, gameName: str, creatorName: str, hours: float) -> None:
    data = {
        "UniverseId": universeId,
        "PlaceId": placeId,
        "GameName": gameName,
        "Creator": creatorName,
        "TimePlayed": f"{hours:.2f} hours",
    }

    writeJson(data)
    time.sleep(0.2)

def printExtra() -> None:
    with open("output.json" , "r", encoding="utf-8") as outputJson:
        fileData = json.loads(outputJson.read())

    mostPlayed = fileData[0]
    leastPlayed = fileData[len(fileData) - 1]
    totalPlayed = 0

    for v in fileData:
        totalPlayed += float(str.split(v["TimePlayed"], " ")[0])
        time.sleep(0.01)

    print(f"Your most played game was {mostPlayed["GameName"]} with {mostPlayed["TimePlayed"]}")
    print(f"Your least played game was {leastPlayed["GameName"]} with {leastPlayed["TimePlayed"]}")
    print(f"You played {round(totalPlayed, 2)} hours in total")

with open("output.json" , "w", encoding="utf-8") as outputJson:
    outputJson.write(json.dumps([]))

for i, v in enumerate(currentData, 1):
    universeId, timePlayed = formatData(v)
    gameData = getGameData(universeId)

    print(f"Processing {i}/{total}")

    if not gameData:
        print(f"[!] Skipping universe ID {universeId}: unknown game data")
        continue

    placeId = gameData.get("rootPlaceId", 0)
    gameName = gameData.get("name", "Unknown Game")
    creator = gameData.get("creator", {})
    creatorName = creator.get("name", "Unknown Creator")
    hours = convertMinutesToHours(timePlayed)

    if creator.get("type") == "User":
        creatorName = f"@{creatorName}"

    if creator.get("hasVerifiedBadge"):
        creatorName = f"{creatorName} [/]"

    outputData(int(universeId), placeId, gameName, creatorName, hours)
    time.sleep(0.2)

print(f"Completed processing {total}/{total}, the data was outputted into output.json")
printExtra()
