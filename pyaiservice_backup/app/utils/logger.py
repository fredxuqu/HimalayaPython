from app.config.settings import LOGGER_LEVEL


class Logger:
    @classmethod
    def debug(cls, v_log_info):
        if LOGGER_LEVEL is not None and LOGGER_LEVEL == "debug":
            print(v_log_info)

    @classmethod
    def info(cls, v_log_info):
        if LOGGER_LEVEL is not None and (LOGGER_LEVEL == "info"):
            print(v_log_info)

    @classmethod
    def error(cls, v_log_info):
        if LOGGER_LEVEL is not None and LOGGER_LEVEL == "error":
            print(v_log_info)
