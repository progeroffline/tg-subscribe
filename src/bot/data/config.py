import os
from pathlib import Path

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

database_filename = "database.db"
schema_filename = "database_schema.sql"
project_filepath = Path(__file__).resolve().parent.parent.parent

sqlite_database_filepath = os.path.join(project_filepath, "db", database_filename)
sqlite_schema_filepath = os.path.join(project_filepath, "db", schema_filename)


USDT_TRC20_WALLET_ADDRESS = "TF8aSMqpwtniPN77wS2EZTTcUKaaJhyorb"

# Key - count months
# Value - subscribe amount
# You can customise this dict
SUBSCRIBE_AMOUNT_BY_PLANS = {
    1: 5,
    # 3: 15,
    # 6: 30,
    # 7: 31,
}
NUMBER_DAYS_FROM_ONE_PAYMENT = 30
SUBSCRIBE_END_NOTIFICATION_DAYS = [7, 3, 1]
REFERAL_REWARD = 5

ADMINS_ID_LIST = [535327818]
private_channels = {
    "Channel 1": {"id": -100123456789, "invite_url": "https://t.me/+ABCDEFGHIJKL"},
}

"""
    Use HTML to format text

    <b>bold</b>, <strong>bold</strong>
    <i>italic</i>, <em>italic</em>
    <u>underline</u>, <ins>underline</ins>
    <s>strikethrough</s>, <strike>strikethrough</strike>, <del>strikethrough</del>
    <span class="tg-spoiler">spoiler</span>, <tg-spoiler>spoiler</tg-spoiler>
    <b>bold <i>italic bold <s>italic bold strikethrough <span class="tg-spoiler">italic bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> bold</b>
    <a href="http://www.example.com/">inline URL</a>
    <a href="tg://user?id=123456789">inline mention of a user</a>
    <tg-emoji emoji-id="5368324170671202286">👍</tg-emoji>
    <code>inline fixed-width code</code>
    <pre>pre-formatted fixed-width code block</pre>
    <pre><code class="language-python">pre-formatted fixed-width code block written in the Python programming language</code></pre>
    <blockquote>Block quotation started\nBlock quotation continued\nThe last line of the block quotation</blockquote>

    And user \n to print the next text on a new line
"""
MAILING_TEXT = "Hello"
