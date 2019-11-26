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
	│         ├user_Num
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
	│                ├admin.py
	│                ├apps.py
	│                ├models.py
	│                ├test.py
	│                ├urls.py
	│                └views.py
	│
	├static
	│
	├templates
	├django_project
	├imgs
	└manage.py
	
====================================

ova映像檔：

2019/11/20 https://reurl.cc/31RjNl

====================================

將下方檔案下載並依照上面路徑檔放入

facenet https://reurl.cc/nVrk7X


====================================

如果檔案執行還是有問題的，可以直接下載專案完整檔

2019/11/20 https://reurl.cc/gvrY84

====================================

模組、套件版本:

Ubuntu 18.04

Django 1.11.11

Jupyter 1.0.0

Keras 2.3.1

Tensorflow-gpu 1.14.0

Numpy 1.16.2

Python 3.6.8



----------------------------更新紀錄----------------------------

2019/11/14： <br>
1.「建立人臉資料」修改成輸入ID後會自動幫使用者在後台資料庫建立預設的個人資料<br>
2.當建立完人臉資料後會自動跑一遍訓練資料集<br>
3.透過「修改個人資料」輸入正確ID可以讓使用者更新個人資料<br>
4.如未修改個人資料直接使用「即時辨識」，當辨識到該使用者時會跑出系統預設的資料<br>

2019/11/20：<br>
1.將「建立人臉資料」的輸入ID功能取消，並改成系統自動輸入流水編號<br>
2.data裡的"user_Num.txt"為儲存流水編號用的文字檔<br>

2019/11/26：<br>
1.重新設計前端版面<br>
2.新增「刪除個人資料」功能，輸入ID就會將資料庫與資料集刪除並重新訓練一次資料集確保資料正確<br>
3.在點擊「建立個人資料」後，提示等待表單變成小網頁的BUG，預計會在下次更新時修正好<br>
