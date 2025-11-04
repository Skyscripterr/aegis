from logger import logger

def trigger_alert(result):
    for entry in result:
        point = entry["point"]
        status = entry["status"]
        if status == "Violation":
            msg = f"⚠️ Boundary violation detected at {point}"
            print(msg)
            logger.warning(msg)
        else:
            logger.info(f"✅ Safe point: {point}")

