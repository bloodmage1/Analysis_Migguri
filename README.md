# Migguri analysis by Django

## 1. Demonstration

![image.jpg1](https://github.com/bloodmage1/Analysis_Migguri/blob/main/img/before_login.png) |![image.jpg1](https://github.com/bloodmage1/Analysis_Migguri/blob/main/img/after_login.png) |
 --- | --- |
| This is what the webpage looks like before you type in your email. It's printing out existing images| This is the appearance of the web page after entering email and clicking Subscribe. You can see the image that you have analyzed.|
 
 
## 2. RUN

```
git clone https://github.com/bloodmage1/Analysis_Migguri
```


python blog_abtest.py


## 3. Architecture

```
Mig_analysis/
│
├── blog_abtest.py
├── app_insta.py
├── blog_control/
│   ├── session_mgmt.py
│   └── user_mgmt.py
├── blog_view/
│   └── blog.py
├── db_model/
│   ├── mongodb.py
│   └── mysql.py
├── static/
├── templates/
│   ├── blog_A.html
│   └── blog_B.html
```

  ## 4. Data

  미꾸리 데이터의 [이 곳](https://www.aihub.or.kr/)에서 확인할 수 있습니다. 그에 대한 설명 또한 [이 곳](https://www.youtube.com/watch?v=p2yjHLA9Dp8)에서 확인할 수 있습니다.