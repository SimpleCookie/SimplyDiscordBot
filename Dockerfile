FROM python:3
ADD src/* /
RUN pip install -R requirements
CMD [ "python", "./main.py" ]