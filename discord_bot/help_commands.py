import discord
from discord.ext import commands


class HelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

        self.help = {
            "p": " β―οΈ  reproducir canciones",
            "pause": " π  pausar una cancion",
            "stop": " π  frenar definitivamente una cancion",
            "resume": " β―οΈ  reanudar una cancion pausada",
            "skip": " β­οΈ  saltear una cacion",
            "help": " pedir ayuda con los comandos",
            # "loop": " βΎοΈ  repetir la cancion infinitamente",
            # "endloop": " π  frenar la repeticion",
            # "config": " π»  entrar en la configuracion del bot",
            "playlist": " β―οΈ  reproducir una playlist de spotify",
            # "seek numero -s/-m": " π  saltar a un segundo/minuto deseado",
            "lyrics": " π  obtener la letra de la cancion que se esta reproducioendo",
        }

    # sends general help
    async def send_bot_help(self, mapping):
        embed = discord.Embed(
            title="Atencion!",
            description="```css\nComandos\n```",
            color=discord.Colour.random(),
        )

        for cmd in mapping:
            for command in mapping[cmd]:
                embed.add_field(
                    name=f"-{command.name}: ",
                    value=f"{self.help[command.name]}",
                    inline=False,
                )
            # description = (
            #     f"{' '.join([f'-{command.name}:{self.help[command.name]}{new}' for command in mapping[cmd]])}",
            # )

        await self.get_destination().send(embed=embed)

    # sends help about an especific command
    async def send_command_help(self, command):
        pass
