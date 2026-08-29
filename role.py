import discord
from discord.ext import commands
from discord import app_commands
from func.dc import Bot
from func.log import get_log

class Supiki_RoleCog(commands.Cog):
    def __init__(self, bot:Bot):
        self.bot = bot
        self.log = get_log(self.__class__.__name__)
    @commands.Cog.listener()
    async def on_ready(self):
        self.log.info(f"{self.__class__.__name__}が読み込まれました！")

    @app_commands.command(name="通話募集", description="通話募集")
    @app_commands.guilds(1541248982712328287)
    @app_commands.checks.cooldown(rate=1, per=300)
    async def voice(self, interaction:discord.Interaction):
        moji = """\
UOM！UOM！UOM！UOMぅぅうううわぁああああああああああああああああああああああん！！！

あぁああああ…ああ…あっあっー！あぁああああああ！！！UOMUOMUOMぅううぁわぁああああ！！！

あぁクンカクンカ！クンカクンカ！スーハースーハー！スーハースーハー！いい匂いだなぁ…くんくん

んはぁっ！UOMたんの水色の髪をクンカクンカしたいお！クンカクンカ！あぁあ！！

間違えた！モフモフしたいお！モフモフ！モフモフ！髪髪モフモフ！カリカリモフモフ…きゅんきゅんきゅい！！

ピースフルの時首傾げてたUOMたんかわいかったよぅ！！あぁぁああ…あああ…あっあぁああああ！！ふぁぁあああんんっ！！

YSMのモデルも作られて良かったねUOMたん！あぁあああああ！かわいい！UOMたん！かわいい！あっああぁああ！

UOMちゃんのMODパックも制作されて嬉し…いやぁああああああ！！！にゃああああああああん！！ぎゃああああああああ！！

ぐあああああああああああ！！！ゲームなんて現実じゃない！！！！あ…3Dモデルもイラストもよく考えたら…

U O M ち ゃ ん は 現実 じ ゃ な い？にゃあああああああああああああん！！うぁああああああああああ！！

そんなぁああああああ！！いやぁぁぁあああああああああ！！はぁああああああん！！[null]ぁああああ！！

この！ちきしょー！やめてやる！！現実なんかやめ…て…え！？見…てる？瓶の中のUOMちゃんが僕を見てる？

瓶の中のUOMちゃんが僕を見てるぞ！UOMちゃんが僕を見てるぞ！戦闘中のUOMちゃんが僕を見てるぞ！！(多分敵対してるだけ)

メイドなUOMちゃんが僕に話しかけてるぞ！！！よかった…世の中まだまだ捨てたモンじゃないんだねっ！

いやっほぉおおおおおおお！！！僕にはUOMちゃんがいる！！やったよアポリオン！！ひとりでできるもん！！！

あ、The Eternal World of Fantasy -Tale of the End-のUOMちゃああああああああああああああん！！いやぁあああああああああああああああ！！！！

ううっうぅうう！！うちの想いよUOMへ届け！！泡沫の虚空のUOMへ届け！
"""
        role = "<@&1543070791044829235>"
        await interaction.response.send_message(content=f"{moji}\n-# {role}", allowed_mentions=discord.AllowedMentions(roles=True))
    @voice.error
    async def voice_error(self, interction:discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):
            await interction.response.send_message(content="ｽﾋﾟｷｦｲｼﾞﾒﾇﾝﾃﾞ!(訳:クールダウン中です)", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Supiki_RoleCog(bot))
