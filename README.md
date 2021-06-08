# 简单英语学习助手
这是我

# 运行环境
python3.8+django 3.17+mysql 5.7

前端页面依赖于bootstrap@3.3.7和jquery@3.1.1（直接通过src获取）

# 运行方法

1. 安装`python3.8`
2. 执行`pip install -r requirements.txt`(建议pip之前修改pip源为国内镜像)
3. 在`setting.py`中的`DATABASES`修改数据库相关配置
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',# 数据库种类（这里为mysql）
        'NAME': 'english',# 数据库名称
        'USER': 'xxx',# 用户名
        'PASSWORD': 'xxx',# 密码
        'HOST': 'localhost',# 数据库地址
        'PORT': '3306',# 数据库连接端口
    }
}
```
4. 在数据库中先新建数据库名称为`english`（或者你想设置的），执行`english.sql`，将数据等导入到数据库中
5. 分别执行`python manage.py makemigrations`和`python manage.py migrate`来生成django的Models。
6. 再执行`python manage.py createsuperuser`根据命令行提示设置相关管理员帐户。
7. 最后执行`python manage.py runserver`即可在`http://localhost:8000`打开网站了。（其他运行方法自行到django官网查阅）

# 系统界面

## 首页

![](https://www.hualigs.cn/image/60bf40fc143d8.jpg)

## 单词列表

![](https://www.hualigs.cn/image/60bf40fb6a119.jpg)

## 单词详情
包括含有图片信息的和不含图片信息的两种，在此以展示含有图片信息的为主。
### 进入单词详情
**含有图片信息**
![](https://www.hualigs.cn/image/60bf40fb7c103.jpg)
**不含图片信息**
![](https://www.hualigs.cn/image/60bf4ba33e745.jpg)

### 单词例句
![](https://www.hualigs.cn/image/60bf4bdca4d49.jpg)

### 单词图片
![](https://www.hualigs.cn/image/60bf4c021bb73.jpg)

## 单词搜索
采用`Word.objects.filter（word__icontains==）`来进行单词搜索。
### 开始搜索
![](https://www.hualigs.cn/image/60bf4c4ab0eb6.jpg)
### 查询到结果
![](https://www.hualigs.cn/image/60bf4ccd39506.jpg)
### 未查询到结果
![](https://www.hualigs.cn/image/60bf4ce429b7e.jpg)

## 段落翻译
采用百度翻译开放平台的的通用翻译API实现，请到https://fanyi-api.baidu.com/doc/21 
查看API的调用方法，并申请appid和key，将`english\views.py`的
appid和key修改成你自己的（我的不能保证能用）。
### 英语->中文
![](https://www.hualigs.cn/image/60bf4cffcf4fb.jpg)
### 中文->英语
![](https://www.hualigs.cn/image/60bf4e5615fcf.jpg)

## 单词测试
单词测试为个人创新性的设计，可以从数据库中随机获取选定等级的10个单词，给出中文含义和词性，在输入框输入
正确的英文单词，如果输入不正确的话就会以红色提示框提示，输入正确的话就会以绿色提示框提示。同时也可以随时
查看正确答案来检验自己。

### 进入界面
![](https://www.hualigs.cn/image/60bf4f509c2dd.jpg)
### 生成随机单词的界面
![](https://www.hualigs.cn/image/60bf5014c93c3.jpg)
### 错误的输入情况
![](https://www.hualigs.cn/image/60bf506e4fe59.jpg)
### 正确的输入情况
![](https://www.hualigs.cn/image/60bf59f38fbb0.jpg)
### 显示正确答案
[![2s9BsH.png](https://z3.ax1x.com/2021/06/08/2s9BsH.png)](https://imgtu.com/i/2s9BsH)

## 后台管理
后台管理采用django自带的admin模块来进行，采用开源的SimpleUI框架对原有django后台进行美化。
### 登录界面
[![2s97oq.md.png](https://z3.ax1x.com/2021/06/08/2s97oq.md.png)](https://imgtu.com/i/2s97oq)
### 进入后台登录界面
[![2s9oes.md.png](https://z3.ax1x.com/2021/06/08/2s9oes.md.png)](https://imgtu.com/i/2s9oes)
### 后台维护单词内容界面
[![2s95Lj.md.png](https://z3.ax1x.com/2021/06/08/2s95Lj.md.png)](https://imgtu.com/i/2s95Lj)
### 对某一单词进行修改
**修改前单词情况（前端和后端）**
[![2s94yQ.md.png](https://z3.ax1x.com/2021/06/08/2s94yQ.md.png)](https://imgtu.com/i/2s94yQ)
[![2s9hQg.md.png](https://z3.ax1x.com/2021/06/08/2s9hQg.md.png)](https://imgtu.com/i/2s9hQg)
**进行修改后保存**
[![2s9bF0.md.png](https://z3.ax1x.com/2021/06/08/2s9bF0.md.png)](https://imgtu.com/i/2s9bF0)
**修改成功（后端和前端）**
[![2s9Twn.md.png](https://z3.ax1x.com/2021/06/08/2s9Twn.md.png)](https://imgtu.com/i/2s9Twn)
[![2s9qYV.md.png](https://z3.ax1x.com/2021/06/08/2s9qYV.md.png)](https://imgtu.com/i/2s9qYV)
### 管理用户添加和权限修改设置
[![2s9XSU.md.png](https://z3.ax1x.com/2021/06/08/2s9XSU.md.png)](https://imgtu.com/i/2s9XSU)
[![2s9jlF.md.png](https://z3.ax1x.com/2021/06/08/2s9jlF.md.png)](https://imgtu.com/i/2s9jlF)
[![2s9LWT.md.png](https://z3.ax1x.com/2021/06/08/2s9LWT.md.png)](https://imgtu.com/i/2s9LWT)