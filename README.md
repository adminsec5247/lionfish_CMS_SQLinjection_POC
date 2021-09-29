# lionfish_CMS_SQLinjection_POC
狮子鱼CMS，SQL注入批量检测工具，支持多线程
seebug:https://www.seebug.org/vuldb/ssvid-99356
工具仅供交流学习使用，因滥用产生的一切后果概不负责

使用方法

1、pip3 install requests,lxml

2、python3 lionfish_sqli_poc.py -u <Target URL>或者python3 lionfish_sqli_poc.py -f <Targets File Path> -thread <Number of threads> (tips:thread默认为10)
