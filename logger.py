# -*- coding: utf-8 -*-
# @Time   : 2021/3/7
# @Author : lorineluo 

import logging
import os
import datetime
from .wecom_bot_utils  import post_text_message

class RobotMsgHandle(logging.StreamHandler):
    """
    A handler class which allows the cursor to stay on
    one line for selected messages
    """
    def emit(self, record):
        try:
            if record.levelno > logging.INFO:
                msg = self.format(record)
                post_text_message(msg)
                # stream = self.stream
                # stream.write(msg + self.terminator)
                # self.flush()
        except RecursionError:
            raise
        except Exception:
            self.handleError(record)

def init_logger(log_state, log_path = './logs/', prefix=''):
    """
    A logger that can show a message on standard output and write it into the
    file named `filename` simultaneously.
    All the message that you want to log MUST be str.

    Args:
        config (Config): An instance object of Config, used to record parameter information.

    Example:
        >>> logger = logging.getLogger(config)
        >>> logger.debug(train_state)
        >>> logger.info(train_result)
    """
    dir_name = os.path.dirname(log_path)
    ensure_dir(dir_name)

    logfilename = '{}_{}.log'.format(prefix, get_local_time())

    logfilepath = os.path.join(log_path, logfilename)

    filefmt = "%(asctime)s.%(msecs)03d %(levelname)s  %(message)s"
    filedatefmt = "[%a %d %b] %Y %H:%M:%S"
    fileformatter = logging.Formatter(filefmt, filedatefmt)

    sfmt = "%(log_color)s%(asctime)-15s %(levelname)s  %(message)s"
    sdatefmt = "%d-%b %H:%M:%S"
    sformatter = logging.Formatter('%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s', sdatefmt)
    if log_state is None or log_state.lower() == 'info':
        level = logging.INFO
    elif log_state.lower() == 'debug':
        level = logging.DEBUG
    elif log_state.lower() == 'error':
        level = logging.ERROR
    elif log_state.lower() == 'warning':
        level = logging.WARNING
    elif log_state.lower() == 'critical':
        level = logging.CRITICAL
    else:
        level = logging.INFO
    fh = logging.FileHandler(logfilepath, mode='a')
    fh.setLevel(level)
    fh.setFormatter(fileformatter)

    sh = logging.StreamHandler()
    sh.setLevel(level)
    sh.setFormatter(sformatter)

    msgdatefmt = "[%s] %d-%b %H:%M:%S"
    msgformatter = logging.Formatter('%(asctime)s.%(msecs)03d \n %(message)s', msgdatefmt)
    rh = RobotMsgHandle()
    rh.setLevel(level)
    rh.setFormatter(msgformatter)

    logging.basicConfig(level=level, handlers=[fh, sh, rh])
    # logging.basicConfig(level=level, handlers=[fh, sh])

def ensure_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def get_local_time():
    cur = datetime.datetime.now()
    cur = cur.strftime('%Y%m%d')

    return cur

if __name__ == '__main__':
    init_logger(log_state='info')
    log = logging.getLogger()
    log.info('test')
    log.warning('test')