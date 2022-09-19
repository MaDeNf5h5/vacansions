from logging import PlaceHolder
from typing_extensions import Required
import discord
from discord.ext import commands
from datetime import datetime, timezone


class HelperModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            discord.ui.InputText(
                label="Ваше имя, возраст и часовой пояс",
                placeholder="Пример: Иван, 19, МСК",
                min_length=4,
                max_length=100,
                style=discord.InputTextStyle.short,
                required=True,
            ),
            discord.ui.InputText(
                label="Был ли опыт на других сервера",
                placeholder="Пример: Да был:...",
                min_length=1,
                max_length=100,
                style=discord.InputTextStyle.short,
                required=True,
            ),
            discord.ui.InputText(
                label="Как Вы относитесь к текущей администрации?",
                placeholder="Пример: Пока что хорошее впечатление, надеюсь оно не изменится",
                min_length=4,
                max_length=150,
                style=discord.InputTextStyle.long,
                required=True,
            ),
            discord.ui.InputText(
                label="Сколько времени готовы уделять нашему серверу?",
                PlaceHolder="Пример: 15-17 Часов",
                min_length=2,
                max_lenght=50,
                style=discord.InputTextStyle.long,
                Required=True,
            ),
            discord.ui.InputText(
                label="Раскажите про себя, чем вы лучше других?",
                placeholder="Пример: Я лучше других, потому что — я умею мыслить критически, я креативный, не агрессивный",
                min_length= 20,
                max_length=500,
                style=discord.InputTextStyle.long,
                required=True,
            ),
            discord.ui.InputText(
                label="Ваш опыт в модерации на других серверах",
                placeholder="Пример: Был старшим модератором на сервере Death gun'а 3 месяца",
                min_length=2,
                max_length=500,
                style=discord.InputTextStyle.long,
                required=True,
            ),
            *args,
            **kwargs,
            )

    async def callback(self, interaction):
        timereg = int(interaction.user.created_at.replace(tzinfo=timezone.utc).timestamp())
        timejoin = int(interaction.user.joined_at.replace(tzinfo=timezone.utc).timestamp())

        embed = discord.Embed(
            title="Новая анкета на помощника ",
            fields=[
                discord.EmbedField(
                    name = "Автор анкеты", 
                    value = f"{interaction.user.mention} | {interaction.user} | {interaction.user.id}", 
                    inline = False
                ),
                discord.EmbedField(
                    name = "Информация по автору анкеты", 
                    value = f'Дата регистрации аккаунта: <t:{timereg}>\nДата присоединения на сервер: <t:{timejoin}>', 
                    inline = False
                ),
                discord.EmbedField(
                    name = self.children[0].label, 
                    value = self.children[0].value, 
                    inline = False
                ),
                discord.EmbedField(
                    name = self.children[1].label, 
                    value = self.children[1].value, 
                    inline = False
                ),
                discord.EmbedField(
                    name = self.children[2].label, 
                    value = self.children[2].value, 
                    inline = False
                ),
                discord.EmbedField(
                    name = self.children[3].label, 
                    value = self.children[3].value, 
                    inline = False
                ),
                discord.EmbedField(
                    name = self.children[4].label, 
                    value = self.children[4].value, 
                    inline = False
                ),
            ],
            color = 0x2e3133,
            timestamp = datetime.now()
        )
        channel = interaction.guild.get_channel(1007118729697562715)
        await channel.send(embed = embed)
        await interaction.response.send_message('Ваша заявка успешно отправлена администрации', ephemeral = True)


class VacancyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
     
    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str('<:asm_stormy_curator:1001817272240844911>'), 
        label = 'Подать заявку', 
        style = discord.ButtonStyle.gray, 
        custom_id = "helper_modal"
    )
    async def helper(self, button, interaction):
        await interaction.response.send_modal(HelperModal(title = 'Заявка на помощника'))

class Vacancies(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions( administrator = True)
    async def vcs(self, ctx):
        embvcs = discord.Embed(
            title = 'Набор на Helper',
            description = '<@&988530239112106014> — занимается верификацией новый участников сервера, а также помогает с поддержанием порядка на сервере.\n** \n**>\n**Что от вас требуется:\n <a:f1:998650137826046003>Уделять серверу в среднем по 2-3 часа в день.\n <a:f1:998650137826046003>Адекватность и стрессоустойчивость.\n <a:f1:998650137826046003>Не менее 2-ух недель на сервере.\n <a:f1:998650137826046003> Минимум 20 уровень в `JB`\n \n**> Что мы вам можем дать?**\n <a:f1:998650137826046003>Игровая валюта <a:f1:998650137826046003>\n\nДля подачи заявки используйте кнопку ниже',
            color = 0x2e3133
            )
        await ctx.message.delete()
        await ctx.send(embed = embvcs, view = VacancyView())

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(VacancyView())


def setup(bot):
    bot.add_cog(Vacancies(bot))