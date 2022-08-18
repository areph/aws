## Cognito CLI Sample

### 環境変数を設定

```shell
USER_POOL_ID=''
APP_CLIENT_ID=''
USER_NAME=''
PASSWORD=''
```

### sign-up

```shell
aws cognito-idp sign-up \
--client-id ${APP_CLIENT_ID} \
--username ${USER_NAME} \
--password ${PASSWORD}
```

### ステータスを確認済みにする

```shell
aws cognito-idp admin-confirm-sign-up \
--user-pool-id ${USER_POOL_ID} \
--username ${USER_NAME}
```

### 認証してJWTを取得する

※アプリクライアントの認証方法で `USER_PASSWORD_AUTH` を追加する必要があります

```shell
aws cognito-idp initiate-auth \
--auth-flow "USER_PASSWORD_AUTH" \
--client-id ${APP_CLIENT_ID} \
--auth-parameters '{"USERNAME": "${USER_NAME}", "PASSWORD": "${PASSWORD}"}'
```

`IdToken` がJWT（トークン）です

https://jwt.io/ でトークンをデコードしてみましょう