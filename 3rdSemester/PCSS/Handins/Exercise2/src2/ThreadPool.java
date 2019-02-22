import java.util.concurrent.*;
import java.util.concurrent.locks.ReentrantLock;

public class ThreadPool{

  public static class Counter{
    public long i = 0;
  }

  public static Counter total = new Counter();


  public static void main(String[] args) {
    ExecutorService executor = Executors.newFixedThreadPool(2);
    ReentrantLock lock = new ReentrantLock();
    executor.submit(new Runnable(){
      @Override
      public void run(){
        lock.lock();
        for (int i=0;i<10000000;i++){
          total.i++;

        }
        lock.unlock();
      }
    });

    executor.submit(new Runnable(){
      @Override
      public void run(){
        lock.lock();
        for (int i=0;i<10000000;i++){
          total.i++;
        }
        lock.unlock();
        System.out.format("%d" ,total.i);
      }
    });
  }
}


