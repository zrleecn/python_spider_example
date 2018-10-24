# python_spider_example

## 案例
- 豆瓣影视爬虫
- 51job爬虫
- 人人网模拟登陆爬虫

## 关键字

- 设置随机user-agent
- 随机ip代理
- 保存到mongodb数据库


## 中间件

```

# 随机的user_agent
class RandomUserAgentMiddlewere(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENTS)
        print(user_agent)
        # 设置头信息
        request.headers.setdefault("User-Agent", user_agent)



class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        print(proxy)
        if proxy['user_passwd'] is None:
            # 没有验证的免费代理ip
            request.meta['proxy'] = proxy['ip_port']
        else:
            base64_pwd = base64.b64encode(proxy['user_passwd'])
            request.headers['Proxy-Authorization'] = 'Basic ' + base64_pwd
            request.meta['proxy'] = proxy['ip_port']


```

设置user_agent
```
-request.headers.setdefault("User-Agent", {"User_Agent": "xxxx"})
```

设置代理
```
 request.meta['proxy'] = "https://xxxx.xxx.x.x:xxx"
```
