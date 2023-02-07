# aws
AWS sample

**Warning**
このリポジトリは公式資料ではありません。私個人でまとめているものですので、参照する場合は参考程度でご利用ください
## Developing on AWS

トレーニング中に当リポジトリをcloneし Lab 環境でサンプルコードを動かしてみましょう

```shell
git clone https://github.com/areph/aws.git
```

## Mod3 Cloud9 でサンプルコードを実行
### Python で実施する場合

Pythonを実行する際にはboto3をライブラリとしてインストールしておきます

```shell
python3 -m pip install --user boto3
```

GUIで実行する場合

- [Run]->[Python]
- sample/python/helloaws.py

CUIで実行する場合

```shell
python ~/environment/aws/samples/python/helloaws.py
```

### Java で実施する場合

Gradleを使って実行します

```shell
cd ~/environment/aws/samples/java
./gradlew run
```