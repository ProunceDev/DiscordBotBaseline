# Baseline Discord Bot

![Bot Logo](assets/logo.png)

## Overview
This is a basic Discord bot template using [interactions.py](https://github.com/interactions-py/interactions.py) and extensions. It provides the minimal setup required to start developing a bot with command handling and configuration management.

## Features
- Uses `interactions.py` for bot interactions
- Supports extensions for modular code structure
- Loads settings from a configuration file
- Uses `.env` for storing sensitive information like the bot token

## Requirements
- Python 3.8+
- `pip` (Python package manager)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/prouncedev/baseline-discord-bot.git
   cd baseline-discord-bot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your bot token:
   ```sh
   TOKEN=your_bot_token_here
   ```
4. Configure the bot settings in `config.json`.

## Running the Bot
Run the bot with:
```sh
python bot.py
```

## Folder Structure
```
baseline-discord-bot/
│── Assets/
│   └── logo.png
│── bot.py
│── config.json
│── constants.py
│── Extensions/
│   └── utilities.py
│── requirements.txt
│── settings.py
│── .env
│── README.md
```

## License
This project is open-source under the MIT License.

