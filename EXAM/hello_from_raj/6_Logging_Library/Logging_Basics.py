import logging

logging.basicConfig(level=logging.DEBUG,
                    format=" %(asctime)s - %(levelname)s - %(message)s ")
logger = logging.getLogger("my_logger")
logger1 = logging.getLogger("parent_child")


logging.debug("Debug Message!")
logging.info("Information Message!")
logging.warning("Watch out!")
logging.error("Error Message!")
logging.critical("Critical Message!")
