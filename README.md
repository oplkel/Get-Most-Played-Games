# --[=[ Get Most Played on Roblox (using RoPro) ]=]

## Overview

This is very self-explanatory. The script uses the data given to it from the `data.json` file that comes straight from RoPro's API database and outputs the processed data into the `output.json` file. Why should you use this instead of the existing UI that shows this information already? While not giving you the best looking experience, this tool does give you more information than RoPro's built-in tool. RoPro's UI only gives you a max of the top 24 games, but this theoretically gives you all the information that you can get. The raw data RoPro gives you is only the universe ID and the playtime (in minutes) you have spent in that game. The processed information gives you the place ID (so you can easily get a link to that game), game name (for quick looking), and time played (in hours).

## Prerequisites
- You have basic knowledge on how to use a code editor (VS Code recommended).
- You have the Python programming language installed.
- (Optional) You have the Prettier VS Code extension installed.

## Notes

- You will have to provide it with the data since I am pretty sure that RoPro uses your Roblox cookies to be able to fetch the data from its database.
- The more data, the more time it takes to process the data.
- Progress is constantly outputted for progress updates.

## How to fetch the raw data

1. Open the developer console on the Roblox website.
2. Go onto the console tab of the developer console.
3. Change the time frame of the "Your Most Played" RoPro section of the Roblox home page to your desired option.
4. Notice the console log? The console should have printed out multiple print statements (text in white). They should appear in this format:

```json
(number) [{...}, {...}, {...}, {...}, {...}, ...]
```

OR

```json
(number) [Array(2), Array(2), Array(2), Array(2), Array(2), ...]
```

(number) indicates how big that piece of data is so pick whichever print statement that you want to process.
5. Right click on the print statement and copy object. 6. Paste into the `data.json` file.

## How to use
1. Download the project.
2. Open the project folder in a code editor (VS Code recommended).
3. Paste raw data into `data.json`.
4. Run the `main.py` file.
5. Look at `output.json` - wait until it has finished.

### More features may be added in the future.

oplkel :P
