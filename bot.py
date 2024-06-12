import discord
import re
import dotenv


def testRegex(message):
    if re.match(r"^.*\b(F|f)+(E|e)+(U|u)+(R|r)+\b.*$", message):
        return True
    return False


def check_feur_message(message):
    # Create list
    listGif = []
    listGif.append("https://tenor.com/view/feur-meme-gif-24407942")
    listGif.append("https://tenor.com/fr/view/feur-theobabac-quoi-gif-24294658")
    if listGif.__contains__(message.content):
        return True
    else:
        wordlist = message.content.split(" ")
        for i in wordlist:
            if testRegex(i.lower()):
                return True
        return False


def check_quoi_message(message):
    if re.match(r"^.*\b(Q|q)+(U|u)+(O|o)+(I|i)+\b.*$", message.content):
        return True
    return False


def check_ou_message(message):
    if re.match(r"^.*\b(O|o)+(U|u)+\b.*$", message.content):
        return True
    return False


async def check_feur(message):
    b = check_feur_message(message)
    if b:
        await message.add_reaction("\U000026A0")
        await message.channel.send("Et tu te crois drôle en plus...")
<<<<<<< HEAD
        await message.channel.send(file=discord.File("adrian.png"))
=======
        await message.channel.send(file=discord.File("40985A72E8E05E30D232752D483AC8DB04226D36631DD31D98D11177CD1EF46833BDF582AD2C5029C0838C02C65959C1FEF44552EAB6D92117AB64F0C1390098.png"))
>>>>>>> 3bd8801298a4d814ccc208a34ed45699b9065c1c
        f = open("log.txt", "a")
        f.write(
            "Feur : Message from {0.author}: {0.guild} - {0.channel}: {0.content}\n".format(
                message
            )
        )
        f.close()


async def check_quoi(message):
    q = check_quoi_message(message)
    if q:
<<<<<<< HEAD
        await message.channel.send("<@289867158438150154> - YOUR TIME !")
=======
        id = dotenv.dotenv_values(".env")["PINGID"]
        await message.channel.send("<@" + id + "> - YOUR TIME !")
>>>>>>> 3bd8801298a4d814ccc208a34ed45699b9065c1c
        f = open("log.txt", "a")
        f.write(
            "Quoi : Message from {0.author}: {0.guild} - {0.channel}: {0.content}\n".format(
                message
            )
        )
        f.close()


async def check_ou(message):
    o = check_ou_message(message)


class MyClient(discord.Client):
    status = True

    name = dotenv.dotenv_values(".env")["NAME"]

    async def on_ready(self):
        await client.change_presence(activity=discord.Game(name="vec" + self.name))
        print("Logged on as", self.user)
        print("------")

    async def check_start_stop(self, message):
        if message.content == "!stop":
            self.status = False
            await client.change_presence(activity=discord.Game(name="en standby"))
            return True
        if message.content == "!start":
            self.status = True
            await client.change_presence(activity=discord.Game(name="vec" + self.name))
            return True
        return False

    async def on_message(self, message: discord.Message):
        if await self.check_start_stop(message):
            return
        if message.author == self.user:
            return
        if not self.status:
            return

        await check_feur(message)
        await check_quoi(message)
        await check_ou(message)


client = MyClient(intents=discord.Intents.all(), command_prefix="!")

token = dotenv.dotenv_values(".env")["TOKEN"]

client.run(token)
