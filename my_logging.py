import logging
import sys
import logging.handlers

LOG_FMT = '%(module)s - %(asctime)s — %(name)s — %(levelname)s - %(funcName)s:%(lineno)d — %(message)s'


def logger_factory(logger_name, handlers_list, log_format, log_level):
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    if not isinstance(handlers_list, (list, tuple)):
        handlers_list = [handlers_list]
    for handler in handlers_list:
        handler.setFormatter(logging.Formatter(log_format))
        logger.addHandler(handler)

    return logger


def create_console_logger(logger_name, log_format=LOG_FMT, log_level=logging.DEBUG):
    return logger_factory(logger_name, handlers_list=[logging.StreamHandler(sys.stdout)],
                          log_format=log_format, log_level=log_level)


def create_file_logger(logger_name, log_file="execution.log", log_format=LOG_FMT, log_level=logging.DEBUG):
    return logger_factory(logger_name, handlers_list=[logging.FileHandler(log_file)],
                          log_format=log_format, log_level=log_level)


def create_rotating_file_logger(logger_name, log_file="out.log", max_log_bytes=2000000, max_log_backup_files=20,
                                log_format=LOG_FMT, log_level=logging.DEBUG):
    """ Creates rotating file logger with the given file name, max_log_bytes, max_log_backup_files and log_format.
         :param log_file: log file name
         :param max_log_bytes: the maximum size of file in Bytes
         :param max_log_backup_files: the number of backup files to store
         :param log_format: custom format as logging.Formatter object
         :param log_level: logging level
         :return: logging.Logger
     """
    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=max_log_bytes,
                                                   backupCount=max_log_backup_files)
    return logger_factory(logger_name, handlers_list=[handler],
                          log_format=log_format, log_level=log_level)


def create_file_console_logger(logger_name, log_file="execution.log", log_format=LOG_FMT, log_level=logging.DEBUG):
    handlers = [logging.FileHandler(log_file), logging.StreamHandler(sys.stdout)]
    return logger_factory(logger_name, handlers_list=handlers,
                          log_format=log_format, log_level=log_level)


if __name__ == "__main__":
    # To get a console handler, run this code
    console_logger = create_console_logger(logger_name="logger1")
    console_logger.debug("Hello World")

    # To get a file logger, run this code
    file_logger = create_file_logger(logger_name="logger3", log_file="out.log")
    file_logger.critical("This is a critical message")

    # To get a console and file logger, run this code
    console_file_logger = create_file_console_logger(logger_name="my_logging2", log_file="out3.log")
    console_file_logger.error("Error: This is from console file logger")
