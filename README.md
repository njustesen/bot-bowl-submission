# Submission Template for Bot Bowl

Before submitting, you should have read the competition [rules](https://njustesen.github.io/ffai/bot-bowl-iii) of Bot Bowl III.

## Dependencies
The competition organizers will create a conda environment with python 3.8 and install the dependencies like this:

```
conda create --name bot python=3.8
conda activate bot
pip install -r requirements.txt
```

Please specify in your README.txt if you have additional installation instructions for your bot. 
If your bot is difficult to setup, you can provide a docker file and a one-liner to start your bot.

## Run your bot
Include your bot script to run.py and make sure it can be loaded correctly when running:

```
python run.py --agent <bot-name> --token 1234 --port 6000
```
where ```<bot-name>``` is the name you have used to register your bot.
```my-random-bot``` is already imported and can be used without editing the script.

## Test in a Competition
You can test your bot by running it in two different processes (open another terminal window and run the above command again but with a different port). Then specify the tokens and ports of the two bots in competition.yaml.
If you installed this repo in a conda environment, remember to activate in all three processes.

When the two bots are loaded and are waiting for a game to start, run the competition server (in another process):
```
python competition.py --config competition.yaml  
```

When the competition is over, you should see the resutls printed in your terminal.
