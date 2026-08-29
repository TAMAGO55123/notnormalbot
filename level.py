import discord
from discord.ext import commands
from discord import app_commands
from func.dc import Bot
from func.log import get_log

class LevelCog(commands.Cog):
    def __init__(self, bot:Bot):
        self.bot = bot
        self.log = get_log(self.__class__.__name__)
    @commands.Cog.listener()
    async def on_ready(self):
        self.log.info(f"{self.__class__.__name__}が読み込まれました！")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.guild.id == 1541248982712328287:
            if message.author.id == 437808476106784770:
                if "levelup" in message.content:
                    a = message.content.split(",")
                    ch = message.guild.get_channel(1541317547356594257)
                    em = []
                    if len(message.attachments) != 0:
                        if "image" in message.attachments[0].content_type:
                            em.append(
                                discord.Embed(
                                    colour=discord.Colour.random()
                                ).set_image(url=message.attachments[0].url)
                            )
                    await ch.send(
                        content=f"<@{a[1]}>さんが**Lv.{a[2]}**になりました!",
                        embeds=em,
                        allowed_mentions=discord.AllowedMentions(users=False)
                    )
        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(LevelCog(bot))
