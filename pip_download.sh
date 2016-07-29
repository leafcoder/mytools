#!/bin/sh

CURRENT=$(cd `dirname $0`; pwd)
PROJECT=`dirname $CURRENT`

PYTHON=""
if [ -f "$PROJECT/python.pth" ]; then
    PYTHON=`python -c "print open('$PROJECT/python.pth').read().strip()"`
fi

if [ -z "$PYTHON" ]; then
    echo "注意：$PROJECT/python.pth 文件不能为空"
    exit 1
fi

PYTHON_BIN=`dirname $PYTHON`
$PYTHON_BIN/pip freeze --> $PROJECT/requirement.txt
$PYTHON_BIN/pip download \
    --trusted-host pypi.douban.com \
    -i http://pypi.douban.com/simple \
    --extra-index-url https://pypi.python.org/simple \
    -r $PROJECT/requirement.txt \
    -d $PROJECT/deps/pip_packages \
    --no-binary :all: \
    --timeout 600
