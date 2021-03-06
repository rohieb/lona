class NotInteractiveError(Exception):
    pass


class Connection:
    def __init__(self, server, http_request, websocket=None):
        self.server = server
        self.http_request = http_request
        self.websocket = websocket

    @property
    def is_interactive(self):
        return self.websocket is not None

    def send_str(self, string):
        # TODO: error handling (disconnects, reconnects, etc.)
        # TODO: find right priority

        if not self.is_interactive:
            raise NotInteractiveError

        self.server.schedule(
            self.websocket.send_str(string),
            sync=True,
            priority=self.server.settings.DEFAULT_VIEW_PRIORITY,
        )
