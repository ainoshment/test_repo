from logging import getLogger
from flask import Flask

from test_pack.libs.do_something import main
from test_pack.logger import setup_logging

logger = setup_logging(__name__)


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def do_some():
    result = main(1)
    print("result:", result)
    logger.debug("debugです")
    logger.critical("criticalです")
    try:
        # 意図的にエラー
        a = 1
        b = a + "2"
        print(b)
    except Exception as e:
        # exc_info=Trueだったら構造化logにtracebackをいれる
        logger.error(e, exc_info=True)
    return {"message": "response", "status_code": 200}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
