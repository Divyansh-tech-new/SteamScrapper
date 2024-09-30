import discord
from discord.ext import commands,tasks
from itertools import cycle
from bs4 import BeautifulSoup
import requests
import string
import random
import threading
bot=commands.Bot(command_prefix="!",intents=discord.Intents.all()) ##see meaning in video of this line
##see why this function is between the 2 bot commands , its important
bot_statuses=cycle(["!comms for commands list","!c or !commands or !command for command list","please do not try !j5 black , there's something wrong with it"])
@tasks.loop(seconds=5)
async def change_bot_status():
    await bot.change_presence(activity=discord.Game(next(bot_statuses)))
@bot.event##only on_ready works here not anything else
async def on_ready(): ##async important ,otherwise raise TypeError('event registered must be a coroutine function')
    print("Bot is ready!")
    change_bot_status.start()

@bot.command(name="hi")
async def hello(ctx):  ##ctx takes commands from the users , notice that the function name is the command to be given by the user
    await ctx.send(f"Hello there {ctx.author.mention}!")

@bot.command(aliases=["gm","GM","Morning"])
async def goodmorning(ctx):  ##ctx takes commands from the users , notice that the function name is the command to be given by the user
    await ctx.send(f"Good Moring {ctx.author.mention}!")



@bot.command(name="t")
async def tags(ctx):
    await ctx.send(f"Here's your list {ctx.author.mention}")
    await ctx.send(f"Example- Use !j(1) or !j1 for jokes on alcohol")
    
    for j in range(0,100,20):
        embeded_msg=discord.Embed(title="List of Tags",color=discord.Color.blurple())
        for i in enum_all_tags_not_text[j:j+20]:       
            embeded_msg.add_field(name="",value=f"{i[0]}. {i[-1].text}",inline=True)
        await ctx.send(embed=embeded_msg)    
    await ctx.send(f"Furthur Contact  {ctx.author.mention} for any kind of error or help")





@bot.command(aliases=["command","commands","comms"])
async def c(ctx):
    await ctx.send(f"Here's your list {ctx.author.mention}")
    embeded_msg=discord.Embed(title="List of Commands",color=discord.Color.green())
    embeded_msg.set_thumbnail(url=bot.user.avatar)##bot's dp
    #embeded_msg.set_image(url=ctx.guild.icon) ##server dp
    embeded_msg.add_field(name="!hi" ,value="To greet me",inline=False)
    embeded_msg.add_field(name="!gm or !GM or !Morning",value="To wish me Good Morning",inline=False)
    embeded_msg.add_field(name="!jokes or !j ",value="To get a random joke",inline=False)##try inline=True or False, False better for me
    embeded_msg.add_field(name="!j(TagNumber) ",value="To get a random joke with some specific tags , enter !tags or !t for list of tags, the bot will itself fail if u ask jokes on sensitive topics",inline=False)
    embeded_msg.add_field(name="!call @mention ",value="To call someone",inline=False)
    embeded_msg.add_field(name="!about @mention    or    !userinfo @mention ",value="To get info about the tagged user",inline=False)
    await ctx.send(embed=embeded_msg)
    await ctx.send(f"Furthur Contact  {ctx.author.mention} for any kind of error or help")
    
    
html_text=requests.get("https://onelinefun.com/").text
soup=BeautifulSoup(html_text,"lxml")
joke=list(soup.find_all("div",class_="o"))
all_tags_not_text=soup.find_all("li")
all_tags_not_text=all_tags_not_text[1:]
enum_all_tags_not_text=list(enumerate(all_tags_not_text,start=1))
# for i in range(2,467):
#     print(i)
def html_scrapper(i):
    global joke
    html_text=requests.get(f"https://onelinefun.com/{i}/").text
    soup=BeautifulSoup(html_text,"lxml")
    joke.extend(list(soup.find_all("div",class_="o")))
    print(type(joke))
    print(len(joke))
@bot.command(aliases=["j","J"])
async def jokes(ctx):
    global joke
    #current_joke=random.choice(joke)
    try:
        current_joke=random.choice(joke)
        joke.pop(joke.index(current_joke))
        current_joke=current_joke.text
        print(current_joke)
        pos=current_joke.find("One liner tags:")
        joke_text=current_joke[0:pos]
        joke_rating=current_joke[current_joke.find("%")-6:current_joke.find("%")+1]
        joke_tags=current_joke[pos:current_joke.find("%")-6]
        await ctx.send(f"Here's your Joke {ctx.author.mention}")
        user_id = "781493577292447744"
        user = discord.utils.get(ctx.guild.members, id=int(user_id))##to get user object , from user id ., like bot.user or ctx.author
        avatar = user.avatar
        embeded_msg=discord.Embed(description=f"Rating-{joke_rating}",color=discord.Color.green())
        embeded_msg.add_field(name="\n",value="",inline=False)
        embeded_msg.add_field(name=joke_text,value="\n",inline=False)
        embeded_msg.add_field(name="\n",value=joke_tags,inline=False)
        embeded_msg.set_footer(text="The bot and its developer takes no responsiblity on the jokes posted by the bot itself.They are just scrapped from a website from web")
        await ctx.send(embed=embeded_msg)
        await ctx.send(f"Contact  {user.mention} for any kind of error or help")
        print("Number of jokes remaining in the server:",len(joke))

    except:
        await ctx.send(f"Seems like we ran out of jokes for today, contact  {ctx.author.mention} for refueling...")
    #https://onelinefun.com/4/ 
    # print(joke_original_list)
    # for joke in joke_original_list:
    #     if joke not in joke_List:
    #         joke_List.append(joke)
    #         if joke[0].isdigit():
    #             break
    

#ctx.author: The user who invoked the command
#ctx.guild: The guild (server) where the command was invoked
#ctx.channel: The channel where the command was invoked
#ctx.message: The original message that triggered the command







tagged_jokes_aliases=[]
for i in range(1,101):
    tagged_jokes_aliases.append(f"j({i})")
    tagged_jokes_aliases.append(f"j{i}")
type(tagged_jokes_aliases)
#print(enum_all_tags_not_text)
@bot.command(aliases=tagged_jokes_aliases)
async def tagged_jokes(ctx):
    global joke
    #current_joke=random.choice(joke)
    #try:
    while True:
        try:
            current_joke=random.choice(joke)
            current_joke_text=current_joke.text
            pos=current_joke_text.find("One liner tags:")
            joke_text=current_joke_text[0:pos]
            joke_rating=current_joke_text[current_joke_text.find("%")-6:current_joke_text.find("%")+1]
            joke_tags=current_joke_text[pos:current_joke_text.find("%")-6]
            joke_tags_stripped=joke_tags[joke_tags.find(":")+1:].replace(","," ")
            ##gives the original msg that invoked that command
            id=""
            tag=""
            for i in str(ctx.invoked_with):
                if i.isdigit():
                    id+=i         
            if int(id)==5:
                break
            for i in enum_all_tags_not_text:
                cond=(int(i[0])==int(id))
                if cond:
                    tag=i[-1].text
                    print("breaked")
                    break
            if tag not in joke_tags_stripped:
                continue
            joke.pop(joke.index(current_joke))
            await ctx.send(f"Here's your Joke {ctx.author.mention} on {tag}")
            user_id = "781493577292447744"
            user = discord.utils.get(ctx.guild.members, id=int(user_id))##to get user object , from user id ., like bot.user or ctx.author
            print("joke text=",joke_text)
            print("joke tags=",joke_tags)
            avatar = user.avatar
            embeded_msg=discord.Embed(description=f"Rating-{joke_rating}",color=discord.Color.green())
            embeded_msg.add_field(name="\n",value="",inline=False)
            embeded_msg.add_field(name=joke_text,value="\n",inline=False)
            embeded_msg.add_field(name="\n",value=joke_tags,inline=False)
            embeded_msg.set_footer(text="The bot and its developer takes no responsiblity on the jokes posted by the bot itself.They are just scrapped from a website from web")
            await ctx.send(embed=embeded_msg)
            await ctx.send(f"Contact  {user.mention} for any kind of error or help")
            print("Number of jokes in the server are-",len(joke))
            break

        except Exception as e:
            print("EXCEPTION IS-",e)
            await ctx.send(f"Seems like we ran out of jokes for today, contact  {ctx.author.mention} for refueling...")






















@bot.command()
async def em(ctx):
    embeded_msg=discord.Embed(title="Title of embeded",description="description of embeded",color=discord.Color.green())
    embeded_msg.set_thumbnail(url=ctx.author.avatar)##person's dp
    embeded_msg.set_image(url=ctx.guild.icon) ##server dp
    embeded_msg.add_field(name="name of field",value="value of field",inline=False)
    embeded_msg.set_footer(text="Footer Text",icon_url="https://developers.google.com/speed/webp/gallery2")
    embeded_msg.set_author(name='', url='https://www.example.com', icon_url=ctx.author.avatar)
    
    await ctx.send(embed=embeded_msg)

@bot.command(aliases=['userinfo',"about"])## once aliases , name given , original fun name does not work
async def ab(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title="User Info", description=f"Information about {member}", color=0x00ff00)
    embed.set_thumbnail(url=member.avatar.url)
    embed.add_field(name="Username", value=member.name, inline=True)
    embed.add_field(name="Discriminator", value=member.discriminator, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Status", value=member.status, inline=True)
    embed.add_field(name="Top Role", value=member.top_role.mention, inline=True)
    embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    embed.add_field(name="Account Created", value=member.created_at.strftime("%Y-%m-%d %H:%M:%S"), inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def bye(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(f"bye {member.mention}")




@bot.command()
async def call(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(f"how are you {member.mention}")






for i in range (2,30):
    print(i)
    t=threading.Thread(target=html_scrapper,args=[i])
    t.start()
bot.run("MTI2MjM3MzgzMzk2NTMwNjA0OQ.GeK8iK.hyWS1S4oMcxerGn1Eg7XrBCMtdzj_sG_l4PM9k") ##bot token here , do not share it with anyone
##put run command at last as , otherwise the bot will only have actions till the point it runs
