<p align="center">
  <img width="60%" src="https://github.com/user-attachments/assets/a63d9e39-da60-40c9-a33f-57ecc3270848">
</p>

---
This project is pretty straight forward. The script uses the data given to it from the `data.json` file that comes straight from RoPro's API database and outputs the processed data into the `output.json` file.

Why should you use this instead of the existing UI that shows this information already? While not giving you the best looking experience, this tool does give you more information than RoPro's built-in tool. RoPro's UI only gives you a max of the top 24 games, but this theoretically gives you all the information that you can get. The raw data RoPro gives you is only the universe ID and the playtime (in minutes) you have spent in that game. The processed information gives you the place ID (so you can easily get a link to that game), game name (for quick looking), and time played (in hours).

## Information ℹ️

- You will have to provide it with the data since I am pretty sure that RoPro uses your Roblox cookies to be able to fetch the data from its database
- The more data, the more time it takes to process the data because of Roblox API rate limits
- Progress is constantly outputted for progress updates
- RoProxy API endpoints are used instead of Roblox's because it is more reliable
- I am not affiliated with RoPro or Roblox

> [!NOTE]
> - [/] after the creator's name means that they are verified
> - \u#### is just an emoji and it shows up like that because json does not support emoji utf-8 encoding (I think!!)

## Prerequisites 📦
- You have RoPro installed and verified your Roblox account
- You have basic knowledge on how to use a code editor (VS Code recommended)
- You have the Python programming language installed
- (Optional) You have the Prettier VS Code extension installed

## Guides 📖

### How to fetch the raw data? 📊

1. Open the developer console on the Roblox website.
2. Go onto the console tab of the developer console.
3. Change the time frame of the "Your Most Played" RoPro section of the Roblox home page to your desired option.
4. Notice the console log? The console should have printed out multiple print statements (text in white). They should appear in this format:

```
(number) [{...}, {...}, {...}, {...}, {...}, ...]
```

**OR**

```
(number) [Array(2), Array(2), Array(2), Array(2), Array(2), ...]
```

(number) indicates how big that piece of data is so pick whichever print statement that you want to process.
5. Right click on the print statement and copy object. 6. Paste into the `data.json` file.

### How to use? 📥
1. Go the [latest release](https://github.com/oplkel/Get-Most-Played-Games/releases/latest) of the project.
2. Download the `.zip` file.
3. Extract and open the project folder in a code editor (VS Code recommended).
4. Paste raw data into `data.json`.
5. Run the `main.py` file.
6. Wait until the processing has finished but `output.json` should have some data.
7. (Optional) Right click and format document on the `output.json` file to make it look nicer.

## Example Usage ✨
<p align="center">
	<img height="400px" width="auto" src="https://github.com/user-attachments/assets/c9c362dc-4878-4aac-890e-9630715b1986"> <img height="400px" width="auto" src="https://github.com/user-attachments/assets/620d7bac-7ea3-43f7-8b8b-055346c8e0c6">
</p>
<p align="center">
  <img height="400px" width="auto" src="https://github.com/user-attachments/assets/e21a46e4-0f36-4343-b1a7-70156bf3a79c">
</p>

oplkel :P
