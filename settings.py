import os

# App settings
PREFERRED_URL_SCHEME = 'https'
SECRET_KEY = os.urandom(16)

# LDAP settings
LDAP_URL = os.environ.get('LDAP_URL', 'ldap:///')
BASE_DN = os.environ.get('BASE_DN') # Always required
assert BASE_DN, "BASE_DN environment variable must be set"

SCHEMA_DN = 'cn=subschema'

# Attribute to check for user login
LOGIN_ATTR = os.environ.get('LOGIN_ATTR', 'uid')

# Binding
#
# If the two following attributes are set in the environment,
# the UI will NOT ask for a login.
# You need to secure it otherwise!
BIND_DN = os.environ.get('BIND_DN')
BIND_PASSWORD = os.environ.get('BIND_PASSWORD')
if BIND_PASSWORD is None:
    PW_FILE = os.environ.get('BIND_PASSWORD_FILE')
    if PW_FILE is not None:
        with open(PW_FILE) as file:
            BIND_PASSWORD = file.read().rstrip('\n')

# Optional user DN pattern string for authentication,
# e.g. "uid=%s,ou=people,dc=example,dc=com".
# This can be used to authenticate with directories
# that do not allow anonymous users to search.
BIND_PATTERN = os.environ.get('BIND_PATTERN')

# Search
SEARCH_PATTERNS = ( # for search field and group members
    '(%s=%%s)' % LOGIN_ATTR,
    '(cn=%s)',
    '(gn=%s)',
    '(sn=%s)',
)
SEARCH_QUERY_MIN = 2 # Minimm length of query term
SEARCH_MAX = 50 # Maximum number of results
