from nextcord.ext import commands
import nextcord
class Info(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_ready")
  async def up(self):
    print("Bot connecter, veuillez faire une commande / et attendre 24 et aller ensuite sur https://discord.com/developers/active-developer")

  @nextcord.slash_command(name="ping", description="Pong!")
  async def userinfoslash(self, interaction: nextcord.Interaction):
    await interaction.response.send_message("Pong!")

def setup(bot):
  bot.add_cog(Info(bot))
