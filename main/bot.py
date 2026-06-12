import discord
from discord.ext import commands
from discord import app_commands
import ques_ans
import random

class QuesButton(discord.ui.View):
    def __init__(self,ques,ans):
        super().__init__()
        self.ques=ques
        self.ans=ans

    @discord.ui.button(style=discord.ButtonStyle.secondary,label="Answer")
    async def on_call(self,interaction:discord.Interaction,button:discord.ui.Button):
        await interaction.response.defer()
        embed=discord.Embed(title="Answer",description=f"Question:\n{self.ques}\n\nAnswer:\n{self.ans}")
        await interaction.followup.send(embed=embed)

intents=discord.Intents.all()
bot=commands.Bot(commands.when_mentioned_or("?"),intents=intents)

@bot.event
async def on_ready():
    print(f"The bot {bot.user} is ready!")

@bot.command()
async def Ask(ctx:commands.Context):
    qa=random.choice(ques_ans.questions)
    ques=qa[0]
    ans=qa[1]
    button=QuesButton(ques,ans)
    embed=discord.Embed(title="Question!",description=f"Question:\n{ques}")
    await ctx.send(embed=embed,view=button)

bot.run("TOKEN")
