# The handler code for AWS lambda. Add kaitabi_crawler/ to the PYTHONPATH

from crawl import run


def handler(event, context):
    return run()
