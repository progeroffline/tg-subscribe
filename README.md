# Telegram Bot with Subscribing 🤖

This repository contains the source code for a Telegram bot designed to create subscription functionality. Whether you want to manage subscriptions, deliver timely updates, or engage with your audience, this bot, written in Python using the aiogram framework version 2 and an asynchronous SQLite3 wrapper called aiosqlite, has got you covered. 🤖📱

## Project Structure 📂

```css
.
├── .env-dist
├── README.md
├── requirements.txt
└── src
    ├── bot
    │   ├── app.py
    │   ├── data
    │   ├── database
    │   ├── filters
    │   ├── handlers
    │   ├── keyboards
    │   ├── loader.py
    │   ├── logs
    │   ├── middlewares
    │   ├── statesgroup.py
    │   └── utils
    └── db
        └── database_schema.sql
```

## Installation 🚀

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

4. Upgrade pip in environment:
   ```shell
   pip3 install --upgrade pip
   ```

5. Install the dependencies listed in the `requirements.txt` file:
   ```shell
   pip install -r requirements.txt
   ```

## Configuration ⚙️

Before running the bot, you need to configure the following parameters:

1. Create a bot on Telegram and obtain its token from BotFather.

2. Edit the `.env-dist` file, specifying the obtained token and other settings if necessary:
    ```env
    BOT_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
    ```
3. Rename the `.env-dist` file to `.env`.

## Running ▶️

After configuring, you can start the bot with the following command:
```shell
cd src/bot/
python3 app.py
```

The bot will be active and ready to handle commands and user requests on Telegram.
Of course, here's the complete text with the added information about the config file:

Of course, here's the complete text with the added information:

## Usage 📝

### Configuration File 🛠️

To configure specific aspects of your bot's behavior, you can utilize the `config.py` file located in the `src/bot/data/` directory. This file includes the following variables:

```python
# USDT TRC20 wallet address used for transactions
USDT_TRC20_WALLET_ADDRESS = 'TF8aSMqpwtniPN77wS2EZTTcUKaaJhyorb'

# Amount in USDT TRC20 required for subscription
SUBSCRIBE_AMOUNT_IN_USDT_TRC20 = 5

# Number of days between each payment for subscription
NUMBER_DAYS_FROM_ONE_PAYMENT = 30
```

You can utilize these variables in your code to tailor your Telegram bot's behavior in accordance with the specified values.

### Handling User Subscription 🤖

In the `handlers` module located at `src/bot/handlers/`, you have the flexibility to create your own `*.py` files and import them into your bot by editing the `__init__.py` file as follows:

```python
# -*- coding: utf-8 -*-

from .start import *
from .payment import *
```

Within any of your handler files, you can implement filters to determine whether a user is subscribed or not. Here's an example:

```python
# -*- coding: utf-8 -*-

from filters.user_not_subscribed import UserNotSubscribedFilter
from filters.user_subscribed import UserSubscribedFilter

# Start command for subscribed users
@dp.message_handler(UserSubscribedFilter(), commands=['start'], state="*")
...

# Same command, but for users who are not subscribed
@dp.message_handler(UserNotSubscribedFilter(), commands=['start'], state="*")
...
```

This allows you to handle messages differently based on whether a user is subscribed or not, providing greater flexibility in your bot's behavior.
