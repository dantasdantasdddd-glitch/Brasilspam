import os
import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

class MeuBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=".", intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print("Comandos de barra sincronizados!")

bot = MeuBot()

@bot.event
async def on_ready():
    print(f"Bot {bot.user} está online e pronto!")

# 1. Comando /spam (Manda 5 mensagens fixas)
@bot.tree.command(name="spam", description="Envia exatamente 5 mensagens padrão de spam com intervalo.")
async def spam(interaction: discord.Interaction):
    # Responde a interação de forma privada para não dar erro de timeout
    await interaction.response.send_message("Enviando as 5 mensagens...", ephemeral=True)
    
    # Loop que envia exatamente 5 vezes no canal
    for i in range(5):
        await interaction.channel.send("brasil hub melhor brasil hub melhor brasil hub melhor")
        await asyncio.sleep(0.7) # Pausa segura para o Discord não bloquear

# 2. Comando /spamcustom (Manda 5 mensagens customizadas)
@bot.tree.command(name="spamcustom", description="Envia uma mensagem personalizada exatamente 5 vezes.")
@discord.app_commands.describe(mensagem="A mensagem que o bot vai repetir")
async def spamcustom(interaction: discord.Interaction, mensagem: str):
    await interaction.response.send_message("Enviando sua mensagem customizada...", ephemeral=True)
    
    # Loop que envia exatamente 5 vezes a mensagem escolhida no canal
    for i in range(5):
        await interaction.channel.send(mensagem)
        await asyncio.sleep(0.7)

bot.run(os.getenv('DISCORD_TOKEN'))
