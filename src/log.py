import logging
import os

import seqlog


def init_seqlog():
    seq_host = os.environ["SEQ_LOG_HOST"]

    seqlog.log_to_seq(
        server_url=f'http://{seq_host}:5341/',
        level=logging.INFO,
        batch_size=10,
        auto_flush_timeout=10,  # seconds
        override_root_logger=True
    )
