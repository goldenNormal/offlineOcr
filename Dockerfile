FROM python:3.7

MAINTAINER a957947142

ADD ./ /code

WORKDIR /code

RUN python -m pip install --upgrade pip

RUN pip3 install -r requirements.txt

RUN python -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple


CMD [ "python", "/code/app.py" ]



