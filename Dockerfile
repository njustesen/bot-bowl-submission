FROM python:3
EXPOSE 5004-5050
ADD * /
RUN pip install -r requirements.txt
CMD [ "python", "./run.py", "--agent", "my-random-bot", "--token", "" ]