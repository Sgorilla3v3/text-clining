import logging
from pathlib import Path

def get_logger(name: str = "pipeline", log_dir: str | Path = "logs"):
    Path(log_dir).mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    ch = logging.StreamHandler()
    ch.setFormatter(fmt)
    ch.setLevel(logging.INFO)

    fh = logging.FileHandler(Path(log_dir) / f"{name}.log", encoding="utf-8")
    fh.setFormatter(fmt)
    fh.setLevel(logging.INFO)

    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)
    return logger