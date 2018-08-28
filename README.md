# HimalayaPython

Windows:

	How to instal Python

	1. 	install python
		https://www.python.org/ftp/python/3.6.6/python-3.6.6-amd64.exe
		
		click "add environment to path"
		pip,setuptools installed by default.
				
	2. 	install pip
		after python3.4, pip installed by default, default pip version is 10.1	
		commonds : 
			pip list
		
	3.	upgrade pip 
		python -m pip install --upgrade pip
	
	4. 	install pipenv
		pip install pipenv
		certifi, pipenv, tasks, tests, virtualenv will be installed.	

	How to install flask
		
	1. configure environment add  C:\Python36\Scripts to System Environment Path
	
	2. install flask and related third party libraries
		pip install flask
			below libraries will be installed
			certifi          2018.8.13
			click            6.7
			Flask            1.0.2
			itsdangerous     0.24
			Jinja2           2.10
			MarkupSafe       1.0
			pip              18.0
			pipenv           2018.7.1
			setuptools       39.0.1
			virtualenv       16.0.0
			virtualenv-clone 0.3.0
			Werkzeug         0.14.1
			
		pip install sqlalchemy		
		pip install flask-sqlalchemy		
		pip install wtf
		pip install wtforms
		pip install cymysql
		
		finally, below modules will be installed
		aniso8601        3.0.2
		asn1crypto       0.24.0
		certifi          2018.8.24
		cffi             1.11.5
		chardet          3.0.4
		click            6.7
		cryptography     2.3.1
		cymysql          0.9.12
		Flask            1.0.2
		Flask-RESTful    0.3.6
		Flask-SQLAlchemy 2.3.2
		idna             2.7
		itsdangerous     0.24
		Jinja2           2.10
		MarkupSafe       1.0
		pip              18.0
		pycparser        2.18
		PyMySQL          0.9.2
		pytz             2018.5
		requests         2.19.1
		setuptools       40.2.0
		six              1.11.0
		SQLAlchemy       1.2.11
		urllib3          1.23
		Werkzeug         0.14.1
		wheel            0.31.1
		wtf              0.1
		WTForms          2.2.1
		
	3. create project
		mkdir pythonweb
		cd pythonweb

	4.	use pipenv to prepare the virtual environment
		cd pythonweb
		pipenv install
			system will install a virtual environment for current project.
			pipenv will isolate current project.
		install flask by pipenv
			pipenv install flask
			pipenv install sqlalchemy		
			pipenv install flask-sqlalchemy		
			pipenv install wtf
			pipenv install wtforms
			pipenv install requests
			pipenv install cymysql
			
			pipenv uninstall flask to uninstall package
			
		pipenv graph
		
		set Python Interpreter 
		references-PyDev-interpreters-Python Interpreter
		
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
	
	

Deployment:
	nginx + uwsgi
	

