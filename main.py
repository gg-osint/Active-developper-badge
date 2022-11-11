from nextcord.ext import commands
from nextcord import Intents
bot = commands.Bot(command_prefix=['?'], intents=Intents.all(), help_command=None)
from os import listdir, environ
from json import loads
for fn in listdir('cogs'):
  if fn.endswith(".py"):
    bot.load_extension(f'cogs.{fn}'[:-3])

token = loads(open('config.json').read())['token']
try:
  bot.run(environ['token'] if token == 'environ' else token)
except Exception as e:
  print("Possibles erreurs,\nToken invalide\nIntents invalides\nRateLimits", e)
