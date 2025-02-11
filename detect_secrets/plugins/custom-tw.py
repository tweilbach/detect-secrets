import re

from .base import RegexBasedDetector


# This list is derived from RFC 3986 Section 2.2.
#
# We don't expect any of these delimiter characters to appear in
# the username/password component of the URL, seeing that this would probably
# result in an unexpected URL parsing (and probably won't even work).
RESERVED_CHARACTERS = ':/?#[]@'
SUB_DELIMITER_CHARACTERS = '!$&\'()*+,;='


class BasicAuthDetector(RegexBasedDetector):
    """Scans for Custom defined patterns"""
    secret_type = 'Custom'

    denylist = [
        re.compile(
            r'://[^{}\s]+:([^{}\s]+)@'.format(
                re.escape(RESERVED_CHARACTERS + SUB_DELIMITER_CHARACTERS),
                re.escape(RESERVED_CHARACTERS + SUB_DELIMITER_CHARACTERS),
            ),
        ),
    ]
