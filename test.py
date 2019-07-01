import simplebot # grodbot
from ffai.ai.competition import Competition
from ffai.core.load import get_config

config = get_config('ff-11-bot-bowl-i.json')
competition = Competition(
	name='MyCompetition', 
	competitor_a_team_id='human-1', 
	competitor_b_team_id='human-2', 
	competitor_a_name='simplebot', 
	competitor_b_name='random', 
	config=config)
results = competition.run(num_games=2)
results.print()
