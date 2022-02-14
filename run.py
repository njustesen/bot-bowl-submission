import botbowl
import mybot
import argparse

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--agent', help='FFAI registered name of agent', required=True)
parser.add_argument('--token', help='Secret communication token', required=True)
parser.add_argument('--port', help='Port to listen on', type=int, default=5000)
args = parser.parse_args()

agent = botbowl.make_bot(args.agent)
server = botbowl.ai.PythonSocketServer(agent, args.port, args.token)
server.run()
