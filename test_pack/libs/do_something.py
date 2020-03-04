import sys
from contextlib import contextmanager

sys.path.append("/Users/ainosh/works/test/test_repo")
from test_pack.logger import setup_logging

logger = setup_logging(__name__)


@contextmanager
def context_manager_sample():
    print('enter method')
    yield
    print('exit method')


def main(val):
    with context_manager_sample():
        print('hello context manager')
        logger.debug("debuggggggggg")
        logger.error("error")
        a = 1 + val
        print(a)
    return a


if __name__ == '__main__':
    main("2")
