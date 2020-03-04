import json
import os
import sys
import traceback
from logging import getLogger, Formatter, StreamHandler, DEBUG, ERROR

from flask import request


class FormatterJSON(Formatter):
    def format(self, record):
        record.asctime = self.formatTime(record, self.datefmt)

        structed_log = {
            'logLevel': record.levelname,
            'timestamp': '%(asctime)s.%(msecs)dZ' % dict(asctime=record.asctime, msecs=record.msecs),
            'timestamp_epoch': record.created,
            'logging.googleapis.com/trace': create_gcp_trace_str(),
            'message': record.getMessage(),
            'module': record.module,
            'filename': record.filename,
            'funcName': record.funcName,
            'levelno': record.levelno,
            'lineno': record.lineno,
            'processName': record.processName,
            'process': record.process,
            'traceback': {},
            'extra_data': record.__dict__.get('extra_data', {})
        }

        if record.exc_info:
            exception_data = traceback.format_exc().splitlines()
            structed_log['traceback'] = exception_data

        return json.dumps(structed_log, ensure_ascii=False)


def create_gcp_trace_str():
    try:
        trace_id = request.headers.get('X-Cloud-Trace-Context', 'no_trace_id').split('/')[0]
        trace_str = "projects/{project_id}/traces/{trace_id}".format(
            project_id=os.getenv('PROJECT_ID'),
            trace_id=trace_id)
        return trace_str
    except:
        pass


def setup_logging(name):
    logger = getLogger(name)
    logger.setLevel(DEBUG)
    handler = StreamHandler(sys.stdout)
    formatter = FormatterJSON()
    handler.setFormatter(formatter)
    handler.setLevel(ERROR)
    logger.addHandler(handler)
    logger.propagate = False
    return logger
