<p align="center">
  <img width="60%" alt="Get Most Played Games" src="https://github.com/user-attachments/assets/a63d9e39-da60-40c9-a33f-57ecc3270848">
</p>

---
This project is pretty straight forward. The script uses the data given to it from the `data.json` file that comes straight from RoPro's API database and outputs the processed data into the `output.json` file.

Why should you use this instead of the existing UI that shows this information already? While not giving you the best looking experience, this tool does give you more information than RoPro's built-in tool. RoPro's UI only gives you a max of the top 24 games, but this theoretically gives you all the information that you can get. The raw data RoPro gives you is only the universe ID and the playtime (in minutes) you have spent in that game. The processed information gives you the place ID (so you can easily get a link to that game), game name (for quick looking), and time played (in hours).

## Information ℹ️
### How it works
This will be a more in-depth dive into how the project actually works than what is told above. It will first load all of `data.json`'s data and store it in the variable *currentData*. Next, it will define all of the required functions for processing the data and then actually start doing the processing. Finally, it will loop through each item in *currentData*, getting universe ID to fetch the game data and time played to convert from minutes to hours. If it finds that no *gameData* has been returned, it will print out that it is skipping that universe ID (no data will be logged for it) and continue looping. It will save all the data it needs to `output.json` into the following data structure:

<details>
<summary>Processed Data Structure</summary>
	
	[
		{
				"UniverseId": number,
				"PlaceId": number,
				"GameName": string,
				"Creator": string,
				"TimePlayed": string
		},
		...
	]
	
</details>

### Details
- You will have to provide it with the data (since I think that RoPro uses your Roblox cookies to be able to fetch the data from its database)
- The more data, the more time it takes to process the data because of Roblox API rate limits
- Progress is constantly outputted for progress updates
- [RoProxy](https://devforum.roblox.com/t/roproxycom-a-free-rotating-proxy-for-roblox-apis/1508367) API endpoints can be used instead of Roblox's because it is faster and more reliable (in theory)
- Comments are in `main.py` for you

> [!IMPORTANT]
> This project is not affliliated, sponsored by, or endorsed by RoPro or Roblox. All trademarks, logos, and assets remain the exclusive property of their respective owners.

> [!NOTE]
> - [/] after the creator's name means that they are verified
> - \u#### is just an emoji and it shows up like that because json does not support emoji utf-8 encoding (I think!!)

## Prerequisites 📦
- You have RoPro installed and verified your Roblox account
- You have basic knowledge on how to use a code editor (VS Code recommended)
- You have Python and Pip installed
- (Optional) You have the [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) VS Code extension installed

## Guides 📖
### How to fetch the raw data?
1. Open the developer console on the Roblox website.
2. Go onto the console tab of the developer console.
3. Change the time frame of the "Your Most Played" RoPro section of the Roblox home page to your desired option (e.g. Past 30 Days).
4. Notice the console log? The console should have printed out multiple print statements (text in white). They should appear in this format:
```
(number) [{...}, {...}, {...}, {...}, {...}, ...]
```
**OR**
```
(number) [Array(2), Array(2), Array(2), Array(2), Array(2), ...]
```
(number) indicates how big that piece of data is so pick whichever print statement that you want to process.

5. Right click on the print statement and copy object.
6. Paste into the `data.json` file.

### How to install?
1. Go the [latest release](https://github.com/oplkel/Get-Most-Played-Games/releases/latest) of the project.
2. Download the `Get-Most-Played-Games.zip` file.
3. Extract and open the project folder in a code editor (VS Code recommended).
4. Create a new terminal and run the following command to install the dependencies:
```
pip install -r requirements.txt
```

### How to use?
1. Paste raw data into `data.json`.
2. Run the `main.py` file.
3. Wait until the processing has finished but `output.json` should have some data.
4. (Optional) Right click and format document on the `output.json` file to make it look nicer with Prettier.

## Example Usage ✨
I have followed the exact same steps as in the guide section; turning the raw data from RoPro into processed data with detailed information. In the images below, there is the raw data, processed data, and terminal with all the print statements from VS Code.
<div align="center">
	<img height="400px" width="auto" alt="data.json" src="https://github.com/user-attachments/assets/c9c362dc-4878-4aac-890e-9630715b1986"> <img height="400px" width="auto" alt="output.json" src="https://github.com/user-attachments/assets/620d7bac-7ea3-43f7-8b8b-055346c8e0c6"> <img height="400px" width="auto" alt="Terminal" src="https://github.com/user-attachments/assets/e21a46e4-0f36-4343-b1a7-70156bf3a79c">
</div>

## Credits 🙌
[oplkel](https://github.com/oplkel) - Developer

### Dependencies
This project needs the following dependencies to run:
- `requests` - Use HTTP/1.1 requests
