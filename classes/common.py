
from .dbconn import dbconn


class common(object):
    """
    Base class for xhms
    """

    def __init__(self, req):
        self.conn = dbconn()
