import os
import logging

VERBOSE_DEBUG = True
FILE = "logging.log"

def setup(name, verbose=True):
    """
    Initialize logger, standard among codes.
    Returns logging object.
    """

    logger = None       # Store the logger object and makes logs.
    fh = None           # File handler.
    ch = None           # Console handler.
    formatter = None    # Format of the output.

    try:
        os.remove(FILE)
    except:
        pass
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if verbose:
        fh = logging.FileHandler(FILE)
        fh.setLevel(logging.DEBUG)
    else:
        fh = logging.FileHandler(FILE)
        fh.setLevel(logging.WARNING)

    if verbose:
        if VERBOSE_DEBUG:
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
        else:
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
    else:
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
    print(type(logger))

    return logger

if __name__ == "__main__":
    pass