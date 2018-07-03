# python-requests_html-with-flightaware #

# 1.开发环境配置 #


- 安装Python3.x+

- 下载本教程配套的压缩包

- 安装Anaconda套装，点击这个网址 [link](https://www.anaconda.com/download/)

- 打开套装里的终端 Anaconda Prompt

- 用终端cd命令进入压缩包解压的文件目录 如cd C:\Users\51774\Desktop\python-requests_html-with-flightaware

- 进入终端后执行代码如下

________________________________________
    >>> pip install requests_html 
	>>> pip install pandas
	>>> pip install numpy
	>>> cd C:\Users\51774\Desktop\python-requests_html-with-flightaware 
	>>> jupyter notebook


# 2.爬取数据 #




- 打开Flight.ipynb文件查看代码

- Shitf+Enter运行代码




## Image:代码 ##
![](https://i.imgur.com/ewPnTD4.png)
_________________________________

## Image:制定的表格 ##

![](https://i.imgur.com/vix3MQA.png)
___________________________________
	
## Image:生成的表格 ##
![](https://i.imgur.com/29twv5J.png)
___________________________________





# 3.可视化数据 #
- 我们利用plotly可视化工具

- 需要注册账号，获得账户和密钥，点击这个网址 [link](https://plot.ly/accounts/login/?action=login#/)

- 打开cmd终端

- 在终端里调用plotly库

________________________________________
    >>> import plotly
    >>> plotly.tools.set_credentials_file(username='xxx',api_key= 'xxx')
    >>> #xxx是在plotly账户设置-API Keys里,Username,API Keys.


- 打开编译器

- 用编译器运行30.py代码

## Image:运行提示 ##

![](https://i.imgur.com/g8vetaz.png) 
____________________________________

- 运行完后会自动弹出网页

- 网页里是可视化的机场数据

## Image:机场数据 ##
![](https://i.imgur.com/T5SpoUN.png) 





# 4.常见问题 #
	1. 爬取数据后导出的是.csv的文件不是存储到数据库?
	
> 由于Plotly可视化工具支持导入.csv表格文件，所以没有选择导入到数据据做可视化
	
	2. 爬取的是什么航班数据?
> 爬取的是重庆飞往拉萨的3U8633/CSC8633航班数据

	3. 该航班数据有什么亮点?
> 5月14日，川航3U8633重庆-拉萨航班，驾驶舱右座前风挡玻璃破裂脱落，机组实施紧急下降。机组正确处置，飞机于07：46分安全备降成都双流机场，所有乘客平安落地，有序下机。

	4. 为什么选择该航班?
> 做一个项目的同时，并不仅仅为人们提供工作，而是让我们整个国家感到自豪。

> 我想把这件事情传递下去，让人们铭记，3U8633机组拯救了几百位乘客。

> 致敬！
____________________________________

- 喜欢的话给我个Star~
