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
`docker run -it -p 5000:5000 -v $(pwd)/vol:/home xxx:1.0 /bin/bash`

# port forwarding
`ssh -L 5000:localhost:5000 griduser@133.105.83.72`

