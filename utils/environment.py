from os import environ


def env(e, d):
    '''
    Function to get environment variables value if they exist.
    '''
    if e in environ:
        return environ[e]
    else:
        return d
