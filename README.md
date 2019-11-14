<h1>大學專題:人臉辨識</h1>


================路徑檔================

  	┬data┬cv2  
	│         ├dataset
	│         ├facenet
	│         ├haar
	│         ├mtcnn
	│         ├recognizer
	│         ├serializer
	│         ├uploadedimages
	│         ├detect_face
	│         ├facenet
	│         └visualization_utils
	│
	├faceRecog┬__init__.py
	│                     ├cascade.py
	│                     ├dataset_fetch.py
	│                     ├setting.py
	│                     ├urls.py
	│                     ├views.py
	│                     └wsgi.py
	│	
	├records┬migrations
	│	         ├admin.py
	│	         ├apps.py
	│	         ├models.py
	│	         ├test.py
	│	         ├urls.py
	│	         └views.py
	│
	├static
	│
	├templates
	├django_project
	├imgs
	└manage.py
	
====================================

將下列檔案下載並依照上面路徑檔分別放入

MTCNN https://reurl.cc/L14YN7

haar https://reurl.cc/ObGdVr

facenet https://reurl.cc/nVrk7X

cv2 https://reurl.cc/727ORQ

====================================

模組、套件版本:

Ubuntu 18.04

Django 1.11.11

Jupyter 1.0.0

Keras 2.3.1

Tensorflow-gpu 1.14.0

Numpy 1.16.2





----------------------------更新紀錄----------------------------

2019/10/14： 1.「建立人臉資料」修改成輸入ID後會自動幫使用者在後台資料庫建立預設的個人資料
                             2.當建立完人臉資料後會自動跑一遍訓練資料集
			     3.透過「修改個人資料」輸入正確ID可以讓使用者更新個人資料
			     4.如未修改個人資料直接使用「即時辨識」，當辨識到該使用者時會跑出系統預設的資料
			     5.修改
