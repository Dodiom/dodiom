import logging

import seqlog

from config import mwexpress_config

logging.getLogger().setLevel(logging.ERROR)


seq_handler = seqlog.log_to_seq(
    server_url=f'http://{mwexpress_config.seq_host}:5341/',
    level=logging.INFO,
    batch_size=10,
    auto_flush_timeout=1,  # seconds
    override_root_logger=False,
    additional_handlers=[],
)

mwelog = logging.getLogger("mwexpress")
