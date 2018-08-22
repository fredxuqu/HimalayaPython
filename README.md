# HimalayaPython

How to install flask

Windows:

	1. install python
		https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe
		
	2. configure environment add  C:\Python36\Scripts to System Environment Path
	
	3. upgrade pip
		python -m pip install --upgrade pip
	
	4. create project
		mkdir pythonweb
		cd pythonweb
		python -m venv venv
		
	5.	activate the project venv\scripts\activate
		
	6.	pip install Flask
	
	
	7.  pip install pipenv
		使用pipenv创建虚拟环境
		进入项目之后，输入  pipenv install
		pip list
		pipenv shell
		piplist
		exit
		pipevn graph

Linux:
	
	1.	sudo apt-get install software-properties-common
		sudo add-apt-repository ppa:jonathonf/python-3.6 
		sudo apt-get update 
		sudo apt-get install python3.6
		
		sudo apt-get install libbz2-dev libgdbm-dev liblzma-dev libreadline-dev libsqlite3-dev libssl-dev tcl-dev tk-dev dpkg-dev
	
	2.	download python from 
		https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz
		
	3.	tar -xvzf Python-3.6.6.tgz
		cd Python-3.6.6
		./configure
		make
		make altinstall
		
	4.	pip3.4 list
	
	
Linux 编译安装
	1. download from
		https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz
	
	2. sudo tar -xvf Python-3.6.6.tgz
	
	3. prepare dependancy
		sudo apt-get install libbz2-dev libgdbm-dev liblzma-dev libreadline-dev libsqlite3-dev libssl-dev tcl-dev tk-dev dpkg-dev
	
	4.	cd Python-3.6.6
		sudo ./config
		make
		make install
		
	5.	install pip3
		sudo apt-get update
		sudo apt-get upgrade
		sudo apt-get install python-pip
		sudo apt-get install python3-pip
		pip3 --version
	
	6.	install flask
		sudo pip3 install flask
	
	7. 	install virtualenv
		sudo pip3 install virtualenv
	
	



