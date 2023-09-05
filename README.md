# Telegram Bot with Subscribing

This repository contains the source code for a Telegram bot written in Python using the aiogram framework version 2 and an asynchronous SQLite3 wrapper called aiosqlite. This bot provides the ability to manage various functions through Telegram.

## Project Structure

```
.
├── README.md
├── requirements.txt
└── src
    ├── bot
    │   ├── app.py
    │   ├── data
    │   ├── database
    │   ├── handlers
    │   ├── keyboards
    │   ├── loader.py
    │   ├── logs
    │   ├── middlewares
    │   ├── __pycache__
    │   ├── statesgroup.py
    │   └── utils
    └── db
        └── database_schema.sql
```

## Installation

Before running the bot, make sure you have Python 3.8+ installed and follow these steps:

1. Clone the repository to your computer:
   ```shell
   git clone https://github.com/ProgerOffline/subscribe.git
   cd subscribe
   ```

2. Create a virtual environment (recommended but optional):
   ```shell
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```shell
   source venv/bin/activate
   ```

4. Install the dependencies listed in the `requirements.txt` file:
   ```shell
   pip install -r requirements.txt
   ```

## Configuration

Before running the bot, you need to configure the following parameters:

1. Create a bot on Telegram and obtain its token from BotFather.

2. Edit the `config.py` file, specifying the obtained token and other settings if necessary:
   ```python
   TOKEN = 'your_token'
   DATABASE = 'база_данных.db'
   ```

## Running

After configuring, you can start the bot with the following command:
```shell
python app.py
```

The bot will be active and ready to handle commands and user requests on Telegram.

## Usage

This bot provides various commands and functions for interacting with users on Telegram. You can add your own commands and functions by editing the `handlers.py` file according to the aiogram and aiosqlite documentation.
