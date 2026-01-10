"""
--[=[

Author: oplkel
Version: 0.1.0
Updated: January 10, 2026

]=]
"""

## ik this is prob messy code but idc

import pip._vendor.requests as requests
import time
import json

maxRetries = 5
requestDelay = 1

with open("data.json", "r", encoding="utf-8") as dataJson:
    currentData = json.load(dataJson)

total = len(currentData)

def fetch(url: str, parameters = None, retries = maxRetries, delay = requestDelay) -> dict | None:
    for attempt in range(retries):
        try:
            response = requests.get(url, params = parameters, timeout = 10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            if attempt == retries - 1:
                print(f"[X] Failed after {retries} retries: {url}")
                return
            
            time.sleep(delay * (attempt + 1))

def getGameData(universeId: str) -> int | None:
    data = fetch(
        "https://games.roproxy.com/v1/games",
        parameters={"universeIds": universeId}
    )

    if not data:
        return

    return data["data"][0]

def convertMinutesToHours(minutes: int) -> float:
    return minutes / 60

def writeJson(data: dict["UniverseId": int, "PlaceId": int, "GameName": str, "Creator": str, "TimePlayed": str]):
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

        gameData = getGameData(v["id"])

        if not gameData:
            print(f"[!] Skipping universe {id[1]}")
            continue

        placeId = gameData.get("rootPlaceId", 0)
        gameName = gameData.get("name", "Unknown Game")
        creator = gameData.get("creator", "Unknown Creator")
        creatorName = creator.get("name", "Unknown Creator")
        hours = convertMinutesToHours(v["time_played"])

        if creator != "Unknown Creator":
            if creator["type"] == "user":
                creatorName = f"@{creatorName}"

            if creator["hasVerifiedBadge"] == True:
                creatorName = f"{creatorName} [✔]"

        outputData(int(v["id"]), placeId, gameName, creatorName, hours)
        time.sleep(0.2)
elif isinstance(currentData, list):
    for i, v in enumerate(currentData, 1):
        print(f"Processing {i}/{total}")

        gameData = getGameData(v[0])

        if not gameData:
            print(f"[!] Skipping universe {id[1]}")
            continue

        placeId = gameData.get("rootPlaceId", 0)
        gameName = gameData.get("name", "Unknown Game")
        creator = gameData.get("creator", "Unknown Creator")
        creatorName = creator.get("name", "Unknown Creator")
        hours = convertMinutesToHours(v[1])

        if creator != "Unknown Creator":
            if creator["type"] == "User":
                creatorName = f"@{creatorName}"

            if creator["hasVerifiedBadge"] == True:
                creatorName = f"{creatorName} [/]"

        outputData(int(v[0]), placeId, gameName, creatorName, hours)
        time.sleep(0.2)
else:
    print("An error ocurred when iterating through the raw data: invalid data structure")

print(f"Completed processing {total}/{total}, the data was outputted into output.json")
printExtra()
