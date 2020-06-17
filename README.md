# Submission Template for Bot Bowl II

Before submitting, you should have read the [rules](https://njustesen.github.io/ffai/bot-bowl-ii) of Bot Bowl II.

## Dependencies
Specify all dependencies in requirements.py. 
The competition organizers will create a conda environment with python 3.7 and install the dependencies like this:

```
conda create --name bot python=3.7
pip install -r requirements
```

## Run your bot
Make sure your bot will run by calling:

```
python run.py --agent <bot-name> --token 1234 --port 6000
```
where ```<bot-name>``` is the name you have used to register your bot.

## Test in a Competition
You can test your bot by running it in two different processes (open another terminal window and run the above command again but with a different port). Then specify the tokens and ports of the two bots in competition.yaml.
Then run the competition server (in another process):

```
python competition.py --config competition.yaml  
```

## Docker

We may provide a Dockerfile at some point that will run the sample bot in a docker container. You are also welcome to use your own docker file as long as this README.txt describe how to run your bot.
