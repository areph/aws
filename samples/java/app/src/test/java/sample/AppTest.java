/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package sample;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AppTest {
    @Test void appHasAGreeting() {
        App classUnderTest = new App();
        assertNotNull(classUnderTest.getS3BucketNames(), "app should have a S3 bucket list");
    }
}
