import socket
import logging
from pathlib import Path
from qcp import daemon
from qcp import tasks

tmp_path = Path("/tmp")
lg = logging.getLogger("qcp")
logging.basicConfig(level="DEBUG")

HEADERSIZE = 2


with daemon.QcpDaemon(queue_path=tmp_path.joinpath("qcp.db")) as qcpd:
    qcpd.listen()
