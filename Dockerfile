FROM python:3
ADD requirements.txt /
RUN pip install -r requirements
CMD [ "python", "./main.py" ]