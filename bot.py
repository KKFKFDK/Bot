import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

intents = discord.Intents.default()
intents.typing = False
intents.members = True
intents.presences = False

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command()
async def forum(ctx):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    try:
        driver.get("https://python.org")
        page_title = driver.title
        await ctx.send(f"Заголовок страницы: {page_title}")
    finally:
        driver.quit()