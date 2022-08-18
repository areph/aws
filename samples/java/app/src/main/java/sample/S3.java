package sample;

// 依存関係を設定
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.CreateBucketRequest;
import com.amazonaws.services.s3.model.HeadBucketRequest;
import com.amazonaws.waiters.Waiter;
import com.amazonaws.waiters.WaiterParameters;

import java.util.UUID;

public class S3 {
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

    public void createBucketWithExists() {
        String region = "ap-northeast-1";
        String bucketName = "dev-bucket-" + UUID.randomUUID();
        System.out.println("作成するバケット名：" + bucketName);

        // S3クライアント作成
        AmazonS3 s3 = AmazonS3ClientBuilder.standard().withRegion(region).build();

        try {
            if (!s3.doesBucketExistV2(bucketName)) {
                // 存在しなければバケットを作成
                s3.createBucket(bucketName);
            }
        } catch (Exception e) {
            System.out.println("バケット作成時に例外が発生しました");
            e.printStackTrace();
        } finally {
            // 明示的に接続をクローズする
            s3.shutdown();
        }
    }
}
