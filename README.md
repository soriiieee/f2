# tutorial
■環境構築
https://qiita.com/phorizon20/items/57277fab1fd7aa994502
■flask tutorials(Youtube)
https://www.youtube.com/watch?v=xIgPMguqyws&list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX&index=2

# dockerに関しての説明
`docker build . -t xxxx:1.0 ` #build
`docker run -it xxxx:1.0 /bin/bash` "login container

# docker mount
`mkdir vol` #ローカルにマウントされるリンクフォルダを作成
`docker run -it -p 5000:5000 -v $(pwd)/vol:/home flask:1.0 /bin/bash`

# port forwarding
`ssh -L 5000:localhost:5000 griduser@133.105.83.72`


#container の内部で、ライブラリーが読み込めないとき(cartopy)
# cartopy pre install library
# https://stackoverflow.com/questions/53697814/using-pip-install-to-install-cartopy-but-missing-proj-version-at-least-4-9-0

!apt-get install libproj-dev proj-data proj-bin  
!apt-get install libgeos-dev  
!pip install cython  
!pip install cartopy  

