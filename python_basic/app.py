import logging

## Configure the basic logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArthimethicApp")

def add(a, b):
    result = a + b
    logger.debug(f"Adding {a} + {b} -> {result}")
    return result

def sub(a, b):
    result = a - b
    logger.debug(f"Subtracting {a} - {b} -> {result}")
    return result

def mul(a, b):
    result = a * b
    logger.debug(f"Multipling {a} X {b} -> {result}")
    return result

add(10, 15)
sub(10, 15)
mul(10, 15)
