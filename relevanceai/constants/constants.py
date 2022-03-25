import os

from relevanceai.constants.config import Config
from relevanceai.constants.links import *

PACKAGE_PATH = "\\".join(os.path.realpath(__file__).split("\\")[:-2])
CONFIG_PATH = "/constants/config.ini"
CONFIG_PATH = f"{PACKAGE_PATH}{CONFIG_PATH}"
CONFIG = Config(CONFIG_PATH)

MAX_CACHESIZE = (
    int(CONFIG["cache.max_size"]) if CONFIG["cache.max_size"] != "None" else None
)

TRANSIT_ENV_VAR = "_IS_ANALYTICS_IN_TRANSIT"

GLOBAL_DATASETS = ["_mock_dataset_"]

DATASETS = [
    "games",
    "ecommerce_1",
    "ecommerce_2",
    "ecommerce_3",
    "online_retail",
    "news",
    "flipkart",
    "realestate2",
]

MB_TO_BYTE = 1024 * 1024
LIST_SIZE_MULTIPLIER = 3

SUCCESS_CODES = [200]
RETRY_CODES = [400, 404]
HALF_CHUNK_CODES = [413, 524]

SIGNUP_URL = "https://cloud.relevance.ai/sdk/api"
OLD_AUSTRALIA_EAST = "old-australia-east"
AUSTRALIA_URL = "https://gateway-api-aueast.relevance.ai/latest"
WIDER_URL = "https://api.{}.relevance.ai/latest"
