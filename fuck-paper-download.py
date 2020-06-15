#coding = utf-8
import re
import requests
import webbrowser
import tkinter as tk
import tkinter.messagebox
"""
author : Srpihot
github : https://github.com/Srpihot
update_time : 2020-06-15
version : Fuck-Paper-download v1.1
"""
def get_link(url_get):
        paper_link=url_get.get()
        try:
                if 'wanfangdata.com.cn' in paper_link:
                        #遇到万方进行参数处理
                        temp_re = re.compile('(^|&)id=([^&]*)',re.S)
                        temp = re.findall(temp_re,paper_link)
                        paper_link = 'http://d.wanfangdata.com.cn/Periodical/'+temp[0][1]

                headers={
                        'Host': 'ifish.fun',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1'
                }
                base_url='https://ifish.fun/paper/search?key='
                url=base_url+paper_link
                html=requests.get(url=url,headers=headers).text

                pattern=re.compile('下载地址：(.*?)<u(.*?)>(.*?)</u>',re.S)
                results=re.findall(pattern,html)
                download_link = results[0][2]
                webbrowser.open(download_link,new=1)
        except:
                tkinter.messagebox.showerror(title='错误', message='请检查网址是否正确！') 


def main():
        windows = tk.Tk()
        windows.title('Paper-Download V1.1 By-Srpihot*')
        windows.geometry('500x150')
        windows.iconbitmap(r'./lib/icon.ico')
        icon = tk.PhotoImage(file=r'./lib/icon.png')
        icon_p = tk.Canvas(windows,width=80,height=80)
        icon_p.create_image(40,40,image=icon)
        icon_p.place(x=40,y=7)
        name = tk.Label(windows,text='Paper Download',font=('微软雅黑',30),width=15,height=1)
        name.place(x=110,y=9)
        use_how = tk.Label(windows,text='使用方法:输入具体网址点击下载即食用',font=('微软雅黑',8),width=30,height=1)
        use_how.place(x=0,y=120)
        notice = tk.Label(windows,text='仅供学习参考,若所造成的法律责任与本人无关.',font=('微软雅黑',8),fg='red',width=35,height=1)
        notice.place(x=240,y=120)
        url_get = tk.Entry(windows, show = None , font=('Arial',14),width=30)
        url_get.place(x=20,y=90)
        but=tk.Button(windows,text="下载",command=lambda : get_link(url_get),width=10)
        but.place(x=390,y=89)
        windows.mainloop()

if __name__ == "__main__":
    main()
