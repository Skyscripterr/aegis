import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "mission.log")

# Create logs directory if not exists
os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if not logger.handlers:
        file_handler = logging.FileHandler(LOG_FILE)
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

# ✅ Test block (forces file creation)
if __name__ == "__main__":
    log = get_logger("test")
    log.info("Logger test successful — file created.")
    print("Check logs/mission.log")
