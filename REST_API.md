# REST







## REST API



1.Postman

Postman is a software which you can use to test REST APIs. Postman has an easy to use graphical user interface. It also has many helpful features to help you with testing your REST API.  Postman is a very simple and intuitive API testing tool or application. Every component in POSTMAN is very important as it has its own significance.



1.1 Installation

Method 1:

```
* System : Ubuntu 16.04

$ sudo snap install postman
```





1.2 Quick start

run `app.py`, open Postman application, choose new request. 



### Flask APP

run `python ./script/app.py`, then surf 'IP adress:8080',  we can get the following web page.

![Flask_simple_demo](/home/jiaojiao/jiaojiao/project/dubhe/git/github/tutorials/img/Flask_simple_demo.png)



### Remote Server

1.1setup local

```
sudo iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
```

使用通配符IP地址：0.0.0.0. That is `app.run(host='0.0.0.0')`

deploy code in remote server

1.2 access server through

run `python app.py` under required environment in session 

modify `host=0.0.0.0`, `port=5000`

access in your local machine in `127.0.0.1:5000` or IP adress of remote server.



## Reference

* https://linuxhint.com/testing_rest_api_postman/
* https://www.softwaretestinghelp.com/how-to-use-postman/

