import logging
from config import MISSION_LOG_FILE, LOG_DIR
import os

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=MISSION_LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
)

logger = logging.getLogger("AegisLogger")