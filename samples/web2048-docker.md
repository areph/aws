# コンテナでアプリケーションを起動してみましょう🚀

Cloud9 にログインし、ターミナルで以下のコマンドを順に実行します。

- web2048 を git クローンします。
```
git clone https://github.com/gabrielecirulli/2048
cd 2048
```

- Dockerfile を作成します。
```
cat << EOF > Dockerfile
FROM nginx:latest

COPY . /usr/share/nginx/html

EXPOSE 80
EOF
```

- コンテナイメージをビルドします。
```
docker build -t web2048 .
```

- ビルドされたコンテナイメージを確認します。
```
docker images
```

- コンテナイメージからコンテナを起動します
```
docker run -d -it -p 8080:80 web2048
```

- Cloud9 で上部メニューから「Preview」-> 「Preview Running Application」を選択。2048コンテナが起動していることを確認できます。
