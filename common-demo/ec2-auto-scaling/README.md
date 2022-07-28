## EC2 Auto Scaling

### 目的

- URLにアクセスすると下記の情報が見れる
    - 動作しているEC2インスタンスのIDが確認できる
    - 動作しているEC2インスタンスのAZが確認できる
- リクエストの負荷が高まるとEC2 Auto ScalingによってEC2インスタンスがスケールする
- ダッシュボードで確認したり、マルチAZで動作していることがわかる

#### 追加情報

- EC2インスタンスを停止するとどうなるか
    - Auto Healingによって復旧するか
- このEC2インスタンスのパッチ当てをどうするか

### 構成

- VPC
    - Public Subnetを各AZへ作成
    - IGW作成
- ASG
- 起動テンプレート作成
- Application Load Balancing作成
- EC2のユーザーデータでPHPアプリケーションをインストール、Webサーバーを起動