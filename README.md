# GoodComputer（好电脑购物商城）             

### 1.简介
&emsp;&emsp;**本来是打算用作毕业设计的，但导师说近年来做网站的分数不是很高，加上一个人搞前端+后台+数据库，工作量确实比较大。所以打算暂时搁置了。以后有时间再慢慢雕琢。**                 
&emsp;&emsp;* 前端:html+jQuery+bootstrap+...                    
&emsp;&emsp;* 后台:python 3.6.5+django 2.0.4                
&emsp;&emsp;* 数据库:mysql                 


### 2.目标
实现网购商城的基本功能。包括：               
* 登录(包括第三方登录、验证码登录)
* 注册
* 购物车
* 我的收藏
* 用户中心（个人信息、收货地址、我的订单、我的评价、我的足迹...）
* 卖家中心（店铺管理、订单管理、商品管理、物流管理、交易管理...）
* 全局搜索(商品、店铺、品牌...)
* 评论回复
- ...

### 3.已实现
* 登录
* 注册
* 卖家中心部分功能（免费开店、发布商品、查看库存...）
* 全局搜索
* 登录状态监测
* 图片上传预览
* 商品列表展示
- ...

### 4.遇到的一些问题及解决方案        
- 登录需求监测(以中间件的方式解决)               
- 密码加解密(参考了网上的一些算法，最后用base64编解码)            
- 图片验证码(原本是直接写了一个函数生成，但扩展性很差，所以写了一个验证码类实现）          
- 前端点击刷新验证码(因浏览器缓存的原因，所以src要时时更换，而图片则放入内存中，便于刷新，验证码内容放入session进行验证)           
- 图片上传预览（看了网上的一些js插件，没有一个是随form表单提交的，于是自己学着写了一个jquery插件来解决,插件位于static/js/upImg.min.js|css/upImg.min.css）            
- 图片存储问题（将图片相对路径存储到数据库,单个图片用ImageFieled解决，但多张图片时无法满足需求，所以自定义了一个ListField解决）                 
- 图片懒加载(运用插件echo.min.js)        
- 表单验证(运用插件ValidForm.min.js)        
- 全局检索(最后用了第三方检索组件——haystack+whoosh 实现）       
...

### 5.网站部分截图
* 首页                      
![网站截图](https://github.com/jc633/PythonGithub/blob/GoodComputer/static/img/projectShortcuts/20181023220335.png)
* 注册                      
![网站截图](https://github.com/jc633/PythonGithub/blob/GoodComputer/static/img/projectShortcuts/20181023220447.png)
* 登录                      
![网站截图](https://github.com/jc633/PythonGithub/blob/GoodComputer/static/img/projectShortcuts/20181023220513.png)
* 卖家中心                
![网站截图](https://github.com/jc633/PythonGithub/blob/GoodComputer/static/img/projectShortcuts/20181023220939.png)
