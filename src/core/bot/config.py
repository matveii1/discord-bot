from dotenv import load_dotenv
from os import getenv

load_dotenv()

GIFT_ROLES_CHANNEL_ID = int(getenv("GIFT_ROLES_CHANNEL_ID"))
GIFT_ROLES_EMOJI = {'🐲': int(getenv("GIFT_ROLES_EMOJI_1")),
                    '👦🏿': int(getenv("GIFT_ROLES_EMOJI_2")),
                    '😺': int(getenv("GIFT_ROLES_EMOJI_3"))}