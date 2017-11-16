import os
import time
import requests
from bs4 import BeautifulSoup
import bs4


num = 0
f = open('E:/下载文件/3.txt','w')
os.system('del*.jpg')
request = requests.get('http://www.qiushibaike.com').content
soup = BeautifulSoup(request,'html.parser')
main_field = soup.find('div',id = 'content-left')
print(main_field)
#找到我们想要的一信息的位置。

# for joke_block in main_field.children:
# #将每我们得到的信息按照每行读出来
#     # print(type(joke_block))
#     if type(joke_block) == bs4.element.Tag and joke_block.name == 'div':
#     #用type来判断我们（joke_block)的类型属于那一块，运用我们想要的一块
#         print(joke_block)
#         print(joke_block.find('h2').get_text(strip=True))
#         num = num + 1
#         author = joke_block.find('h2').get_text(strip=True)
#         # #读出每个页面的作者的名字
#         #joke_content = joke_block.find('div',class_='content').get_text(strip = True)
#         joke_content = joke_block.find('span').get_text(strip=True)
#         #该处读出我们的想要的文章（这里是笑话）
#         f.write('------------\n')
#         f.write('{0}'.format(num) + author)#将我们爬下的作者的名字爬下来
#         f.write('\n')
#         f.write(joke_content)#将我们爬下的文章爬下来
#         f.write('\n')
#         pic_tag = joke_block.find('div',class_='thumb')
#         #将我们爬下存放文件夹的地点爬下来也爬出来
#         if pic_tag != None:
#             pic_link = pic_tag.find('img').get('src')
#             #该步骤就是在找到刚刚爬下的文件夹的中的图片
#             pic_request = requests.get('http:'+pic_link)
#             with open('E:/下载文件/{0}.jpg'.format(num),'wb') as file:
#             #存放的地点
#                 file.write(pic_request.content)
#     f.close()
#
#
