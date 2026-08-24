import discord
from discord.ext import commands
from discord import app_commands
from func.dc import Bot
from func.log import get_log

class ThreadCog(commands.Cog):
    def __init__(self, bot:Bot):
        self.bot = bot
        self.log = get_log(self.__class__.__name__)
    @commands.Cog.listener()
    async def on_ready(self):
        self.log.info(f"{self.__class__.__name__}が読み込まれました！")

    @commands.Cog.listener()
    async def on_thread_create(self, thread: discord.Thread):
        roles = [
            1541426163682119700
        ]
        mes = await thread.send(content=" ".join([f"<@&{i}>" for i in roles]))
        await mes.edit(content="ﾁｮﾜﾖ!")

async def setup(bot):
    await bot.add_cog(ThreadCog(bot))
