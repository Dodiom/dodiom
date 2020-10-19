import logging
import sys

import seqlog

from config import mwexpress_config

logging.getLogger().setLevel(logging.ERROR)


class OneLineExceptionFormatter(logging.Formatter):
    def formatException(self, exc_info):
        result = super().formatException(exc_info)
        return repr(result)

    def format(self, record):
        result = super().format(record)
        if record.exc_text:
            result = result.replace("\n", "")
        return result


handler = logging.StreamHandler(sys.stdout)
formatter = OneLineExceptionFormatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)

logging.getLogger("mwexpress").addHandler(handler)
logging.getLogger("mwexpress").setLevel(logging.INFO)

mwelog = logging.getLogger("mwexpress")


def init_seqlog():
    pass
    # seqlog.log_to_seq(
    #     server_url=f'http://{mwexpress_config.seq_host}:5341/',
    #     level=logging.INFO,
    #     batch_size=10,
    #     auto_flush_timeout=1,  # seconds
    #     override_root_logger=True,
    #     additional_handlers=[logging.StreamHandler()]
    # )
