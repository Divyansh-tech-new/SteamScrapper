
import string
import requests
from bs4 import BeautifulSoup
L=["https://store.steampowered.com/app/1577120/The_Quarry/","https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/","https://store.steampowered.com/app/209160/Call_of_Duty_Ghosts/","https://store.steampowered.com/app/1962663/Call_of_Duty_Warzone/","https://store.steampowered.com/app/1274570/DEVOUR/","https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/"]
tag_name=""
tag_num=10
game_info=""
game_name=""
image_url=""
url_game=""
info=""
def steamDbParser(url):   
    global game_info,game_name,image_url,info
    try:
        html_text=requests.get(url).text   ##gets the html_text file from the url
        soup=BeautifulSoup(html_text,"lxml")  ##makes a soup object
        ##next few lines are important to scrap an image from web
        image_url=soup.find("img",class_="game_header_image_full")["src"]
        image=requests.get(image_url)
        url_splited=url.split("/")
        game_name=url_splited[-2]
        print(game_name)
        with open(f"{game_name}_thumbnail.ico","wb") as file:  ##The .ico file format is a type of image file used to store icons for various applications, websites, and operating systems. It is a raster image file format that contains a small icon or logo, typically used to represent a program, file, or folder.
            file.write(image.content)   ##important to use wb not only w for .ico files
        try:        
            free_or_not=soup.find('div',id="game_area_purchase").text.strip()
            free_or_not=free_or_not[0:200]
            if "Free" in free_or_not:
                return "FREE"    
        except:
            return "SORRY,some error occured, please contact me , in any servers , or dm me,free wale se end"
        try:
                    prices=soup.find('div',class_=("discount_block game_purchase_discount")).text.strip()
                    if "Download" not in prices:
                        print("Download mill gaya")
                        return prices  
        except:
            pass              
        try:
            prices=soup.find('div',class_="game_purchase_action").text.strip()
            print("nice")
            return prices
        except:
            # # return 
            # try:
            #     prices=soup.find('div',class_="").text.strip()
            #     return prices
            # except:
            return "SORRY,some error occured, please contact me , in any servers , or dm  , ha idhar"
            
    except:
        print("SORRY,some error occured, please contact me , in any servers , or dm me,exited from main bs4")                   
def game_info(url):
    
    global url_game,tag_name,tag_num,info
    url_game=url
    info=steamDbParser(url)
    print("done")
    #if info=="FREE" or "free" or "Free":
        #final_cost="FREE"
    tag_num=info.count("₹")
    print(info)
    print("tag=",tag_num)
    if tag_num==0:
        tag_name="FREE"
    elif tag_num==1:
        tag_name="NOT DISCOUNTED"
        print(tag_name)
        print(info.index("₹"))
    elif tag_num==2:
        tag_name="DISCOUNTED"
    elif tag_num>2:
        tag_name="BAD RESULT"
    else:
        tag_name="ERROR"

# def caller():
#     url=input("enter url:")
#     game_info(url)
#     global url_game
    #url_game=url
    # try:
    #     prices=soup.find('div',class_="discount_block game_purchase_discount").text
    #     return prices
    # except:
    #     game_type="free"  ##using return to end the method , so that it does not check another condition , after 1 is matched
    # try:
    #     prices=soup.find('div',class_="discount_block game_purchase_discount no_discount").text
    #     return prices
    # except:
    #     game_type="free"
            

    ##do not forget, .text to use find
    ##for div in div_list():
    # priceList=prices.split()
    # print(priceList)
    # current_price=priceList[2]
    # max_price=priceList[1][:-1]
    # discount=priceList[0][:-1]
    # print(current_price,max_price,discount)
# while True:
#     url=str(input("Enter another Steam Game url: or 'Quit' to exit: "))
#     if url[0].upper()=="Q":
#         print("THANK YOU for using my SteamDeals_bot ,if you faced any bugs , please report--")
#         break
#     game_info=steamDbParser(url)
#     print(game_info)
#     #index_of_cost=
    




import discord
from discord.ext import commands,tasks
from itertools import cycle
import threading
bot=commands.Bot(command_prefix="!",intents=discord.Intents.all())
bot_statuses=cycle(["!c or !commands or !command for command list","Add your favorite games you wanna play buy , and get to know the best deals on them "])


@tasks.loop(seconds=5)
async def change_bot_status():
    await bot.change_presence(activity=discord.Game(next(bot_statuses)))


@bot.event##only on_ready works here not anything else
async def on_ready(): ##async important ,otherwise raise TypeError('event registered must be a coroutine function')
    print("Bot is ready!")
    change_bot_status.start()

@bot.command(aliases=["command","commands","comms"])
async def c(ctx):
    await ctx.send(f"Here's your list {ctx.author.mention}")
    embeded_msg=discord.Embed(title="List of Commands",color=discord.Color.green())
    embeded_msg.set_thumbnail(url=bot.user.avatar)##bot's dp
    #embeded_msg.set_image(url=ctx.guild.icon) ##server dp
    embeded_msg.add_field(name="!deals" ,value="To get deals for today",inline=False)
    embeded_msg.add_field(name="!add",value="To call me to add a game in the list",inline=False)
    await ctx.send(embed=embeded_msg)
    await ctx.send(f"Furthur Contact  {ctx.author.mention} for any kind of error or help")

@bot.command(aliases=["deal","deals"])
async def d(ctx):
    for url in L:
        try:
            game_info(url)
            print(f"tag_num in this program={tag_num}")
            if tag_num==0:        
                embeded_msg=discord.Embed(title=game_name.replace("_"," "),description=tag_name,color=discord.Color.dark_blue())
                embeded_msg.set_image(url=image_url)
                embeded_msg.add_field(name=url_game,value="",inline=False)
                await ctx.send(embed=embeded_msg)
            elif tag_num==1:
                for i in string.ascii_lowercase+string.ascii_uppercase:
                    if i in info:
                        letter=info.index(i,info.index("₹")+2)
                try:
                    cost2=info[info.index("₹"):info.index("\t")]
                except:
                    cost2=info[info.index("₹"):info.index("\n")]

                embeded_msg=discord.Embed(title=game_name.replace("_"," "),description=tag_name,color=discord.Color.dark_blue())
                embeded_msg.add_field(name=url_game,value=f"Price:{cost2}",inline=False)
                await ctx.send(embed=embeded_msg)
                
            elif tag_num==2:
        # for i in string.ascii_lowercase+string.ascii_uppercase:
        #     if i in info:
        #         letter=info.index(i,info.index("₹")+2)
        # try:
        #     cost2=info[info.index("₹"):info.index("\t")]
        # except:
        #     cost2=info[info.index("₹"):info.index("\n")]
            
                embeded_msg=discord.Embed(title=game_name.replace("_"," "),description=tag_name,color=discord.Color.dark_blue())
                discount=info[info.index("-"):info.index("%")+1]
                try:
                    discount=info[info.index("-",info.index("%")):info.index("%",info.index("%")+2)+1]
                except:
                    pass
                real_price=info[info.index("₹"):info.index("₹",info.index("₹")+2)]
                dis_price=info[info.index("₹",info.index("₹")+2):]
                embeded_msg.set_image(url=image_url)
                embeded_msg.add_field(name=url_game,value=f"",inline=False)
                embeded_msg.add_field(name=f"Discount:{discount}!!",value="",inline=False)
                embeded_msg.add_field(name=f"Discounted Price:{dis_price}",value="",inline=False)
                embeded_msg.add_field(name=f"Earlier Price Was:{real_price}",value="",inline=False)
                await ctx.send(embed=embeded_msg)
                
            else:
                await ctx.send(f"Contact  {ctx.author.mention} , some error occured")
        except:
            await ctx.send(f"Contact  {ctx.author.mention} , some error occured")    
    await ctx.send(f"Furthur Contact  {ctx.author.mention} for any kind of error or help \n The bot shows some mistakes in scrapping the correct prices of some games with dlc packs or demo version etc. ... pls tolerate")    
@bot.command(name="add")
async def add_game(ctx):
    await ctx.send(f"Contact  {ctx.author.mention}, to add a specific game" )

with open("token.txt","r+") as file:
    token=file.read()
    bot.run(token)



    