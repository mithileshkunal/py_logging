import logging
import sys
import logging.handlers


def get_default_log_format():
    """ Method to return the default log format"""
    log_format = logging.Formatter("%(module)s - %(asctime)s — %(name)s — %(levelname)s - %(funcName)s:%(lineno)d — %(message)s")
    return log_format


def get_new_console_handler(log_format=None):
    """This method returns a console handler with the given log_format
        Keyword Arg: log_format accepts logging.Formatter object.
    """
    console_handler = logging.StreamHandler(sys.stdout)
    if log_format is None:
        log_format = get_default_log_format()
    console_handler.setFormatter(log_format)
    return console_handler


def get_new_file_handler(log_format=None, log_file_name="out.log"):
    file_handler = logging.FileHandler(log_file_name)
    if log_format is None:
        log_format = get_default_log_format()
    file_handler.setFormatter(log_format)
    return file_handler


def get_new_rotating_file_handler(log_file_name="out.log", max_log_bytes=2000000, max_log_backup_files=20, log_format=None):
    """ This method returns a file handler with the given file name, max_log_bytes, max_log_backup_files and log_format. This log_format accepts logging.Formatter object"""
# Here, max_log_bytes is the maximum size of file in Bytes and max_log_backup_files is the number of backup files to store.
    file_handler = logging.handlers.RotatingFileHandler(log_file_name, maxBytes=max_log_bytes, backupCount=max_log_backup_files)
    if log_format is None:
        log_format = get_default_log_format()
    file_handler.setFormatter(log_format)
    return file_handler


def get_new_console_logger(logger_name, log_format=None, log_level=logging.DEBUG):
    handler = get_new_console_handler()
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    logger.addHandler(handler)
    return logger


def get_new_file_logger(logger_name, log_file, log_format=None, log_level=logging.DEBUG):
    handler = get_new_file_handler(log_format, log_file)
    if log_file is None:
        log_file = "execution.log"
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    logger.addHandler(handler)
    return logger


def get_new_file_console_logger(logger_name, log_file, log_format=None, log_level=logging.DEBUG):
    if log_file is None:
        log_file = "execution.log"
    logger = get_new_file_logger(logger_name, log_file)
    console_handler = get_new_console_handler()
    logger.addHandler(console_handler)
    return logger


if __name__ == "__main__":
    # To get a console handler, run this code
    console_logger = get_new_console_logger(logger_name="logger1")
    console_logger.debug("Hello World")

    # To get a file logger, run this code
    file_logger = get_new_file_logger(logger_name="logger3", log_file="out.log")
    file_logger.critical("This is a critical message")

    # To get a console and file logger, run this code
    console_file_logger = get_new_file_console_logger(logger_name="my_logging2", log_file="out3.log")
    console_file_logger.error("Error: This is from console file logger")

    # logger.info("Begining of execution")
    # logger.info("logging Info message")
    # logger.debug("This is a debug message")
    # logger.debug(logging.DEBUG)
    # logger.info(logging.INFO)
    # logger.warning(logging.WARNING)
    # logger.error(logging.ERROR)
    # logger.critical(logging.CRITICAL)
    # logger.info("End of Execution")
