package sample;

// 依存関係を設定
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;

import java.util.UUID;

public class S3 {
    public static void main(String[] args) {
        new S3().createBucket();
    }

    public void createBucket() {
        String region = "ap-northeast-1";
        String bucketName = "dev-bucket-" + UUID.randomUUID();
        System.out.println("作成するバケット名：" + bucketName);

        // S3クライアント作成
        AmazonS3 s3 = AmazonS3ClientBuilder.standard().withRegion(region).build();

        try {
            // バケットを作成
            s3.createBucket(bucketName);
        } catch (Exception e) {
            System.out.println("バケット作成時に例外が発生しました");
            e.printStackTrace();
        } finally {
            // 明示的に接続をクローズする
            s3.shutdown();
        }
    }
}
