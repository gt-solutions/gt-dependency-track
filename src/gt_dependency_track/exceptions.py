class Error(Exception):
    """Base class for exceptions in this module."""

    pass


class AuthenticationError(Error):
    """Authentication error"""

    def __init__(self, url):
        self.url = url
        self.message = (
            f"An error occurred during authentication against {self.url}\n"
            f"Check your API Token and try again"
        )


class AuthorizationError(Error):
    """Authorization error"""

    def __init__(self, description, response):
        self.message = (
            f"{description}\n{response.json()['message']} ({response.status_code})"
        )


class DependencyTrackApiError(Error):
    """Error during a DependencyTrack GET request"""

    def __init__(self, description, response):
        self.message = (
            f"{description}: '{response.json()['message']}' ({response.status_code})"
        )
