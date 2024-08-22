import requests
from bs4 import BeautifulSoup
L=[]
tag_name=""
tag_num=10
game_info=""
game_name=""
image=""




"""


import requests
from bs4 import BeautifulSoup
html_text=requests.get(url).text   ##.text important
soup=BeautifulSoup(html_text,"lxml")

image_url=soup.find("name of tag",class or id or other things that can respecify the tag)["name of key if you want its value"]
image=requests.get(image_url)






"""




def steamDbParser(url):   
    global game_info,game_name,image
    L.append(url)
    try:
        html_text=requests.get(url).text   ##gets the html_text file from the url
        soup=BeautifulSoup(html_text,"lxml")  ##makes a soup object
        ##next few lines are important to scrap an image from web
        image_url=soup.find("img",class_="game_header_image0_full")["src"] ##give me the value of "src" key
        image=requests.get(image_url)
        url_splited=url.split("/")
        game_name=url_splited[-2]
        print(game_name)
        with open(f"{game_name}_thumbnail.ico","wb") as file:  ##The .ico file format is a type of image file used to store icons for various applications, websites, and operating systems. It is a faster image file format that contains a small icon or logo, typically used to represent a program, file, or folder.
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
    global tag_name,tag_num
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
        #a,b=game_info[game_info.find("₹"),game_info.find("₹")+5]
    elif tag_num==2:
        tag_name="DISCOUNTED"
    elif tag_num>2:
        tag_name="BAD RESULT"
    else:
        tag_name="ERROR"

def caller():
    url=input("enter url:")
    game_info(url)
    # try:
caller()    
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
    
