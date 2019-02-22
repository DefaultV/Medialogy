public class RaceCondition {

  public static class Counter{
    public long i = 0;
  }

  public static Counter total = new Counter();

  public static void main(String[] args) {

    Thread t1 = new Thread(){
      @Override
      public void run() {
        synchronized(total){
          for (int i=0;i<10000000;i++){
            total.i++;
          }
        }
      }
    };

    Thread t2 = new Thread(){
      @Override
      public void run() {
        synchronized(total){
          for (int i=0;i<10000000;i++){
            total.i++;
          }

        }
      }
    };

    t1.start();
    t2.start();

    try {
      t1.join();
      t2.join();
    } catch (InterruptedException e) {}

    System.out.println(total.i);
  }
}

