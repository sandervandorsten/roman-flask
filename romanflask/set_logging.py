import logging


def setup_logger(verbose: bool = False) -> logging.Logger:
    """
    Returns a logger for the application.
    :param verbose: Boolean that describes verbose mode to be on or off.
    :return: logging.Logger object with stdout handler
    """
    logging.basicConfig(
        format="%(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(levelname)s - %(message)s",
    )
    logger = logging.getLogger("roman.mapping")
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    return logger
