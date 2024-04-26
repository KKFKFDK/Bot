from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


intents = discord.Intents.default()

intents.typing = False
intents.members = True

intents.presences = False

intents.members = True

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@bot.command()
async def forum(ctx):
    #конфиг
    options = Options()
    options.add_argument('--headless') 
    options.add_argument('--no-sandbox') 
    options.add_argument('--disable-dev-shm-usage')
   
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get("https://python.org")
    page_title = driver.title
    
    await ctx.send(f"Заголовок страницы: {page_title}")
    
    driver.close()