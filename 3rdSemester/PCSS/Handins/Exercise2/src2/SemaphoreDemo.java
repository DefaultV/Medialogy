import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;


public class SemaphoreDemo {
	public static void main(String[] args) {
	ExecutorService executor = Executors.newFixedThreadPool(10);

	Semaphore semaphore = new Semaphore(10);

	Runnable longRunningTask = () -> {
	    boolean permit = false;
	    try {
	    	
	        permit = semaphore.tryAcquire(1, TimeUnit.SECONDS);
	        if(permit) {
	        System.out.println("Semaphore acquired");
	        Thread.sleep(5000);
	        }
	        else
		        System.out.println("Could not acquire semaphore");
	    } catch (InterruptedException e) {
	        System.out.println("Interrupted");
	    } finally {
	         semaphore.release();
	    }
	};
	for (int i=0; i <10; i++)
		executor.submit(longRunningTask);

	executor.shutdown();
	}
}

