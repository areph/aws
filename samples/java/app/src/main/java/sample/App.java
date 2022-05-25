package sample;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;

import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.Bucket;

public class App {
    SimpleDateFormat df = new SimpleDateFormat("yyyy MM dd");

    public static void main(String[] args) {
        new App().getS3BucketNames().forEach(System.out::println);
    }

    /**
     * Get S3 Bucket names.
     * ex)
     * yyyy mm dd, bucketname
     * @return List<String> bucketname
     */
    public List<String> getS3BucketNames() {
        final AmazonS3 s3 = AmazonS3ClientBuilder.standard().withRegion(Regions.DEFAULT_REGION).build();
        List<Bucket> buckets = s3.listBuckets();
        return buckets.stream().map(i -> String.format("%s, %s", df.format(i.getCreationDate()), i.getName())).collect(Collectors.toList());
    }
}
