from cr_function import Bot

id = (input('Entrez un ID : '))

bot = Bot()
res = bot.getData("https://statsroyale.com/fr/profile/" + id)

print(res)
