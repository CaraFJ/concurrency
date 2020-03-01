import logging


def EasyLogger(name,log_file_name,log_level='INFO'):
    #logger = logging.getLogger(__name__)
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # save as log file. create file handler 
    fh=logging.FileHandler(log_file_name)
    fh.setLevel(logging.INFO)

    # print in console. create console handler
    ch=logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # create formatter
    fmt_date="%Y-%m-%dT%T%Z"
    format_template="[%(asctime)s]: %(module)-25s %(levelname)s: %(message)-24s"
    formatter=logging.Formatter(format_template,fmt_date)

    # add formatter to hadlers
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add handler to logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger

    

