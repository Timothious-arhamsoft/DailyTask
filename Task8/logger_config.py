import logging
# Task 3: PathLib
from pathlib import Path

def setup_logging() -> None:
    base = Path(__file__).parent
    log_folder = base / "logs"
    log_folder.mkdir(parents=True, exist_ok=True)

    log_file = log_folder/"bank.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_file),
        ],
    )
