public class Program implements Runnable{
  private Thread t;
  String threadName;
  Program(String Threadname) {
    this.threadName = Threadname;
  }



  public static void main(String[] args) {
    Thread t1 = new Thread(new Program("T0"));

    t1.start();
    Thread.yield();

    for (int i = 0; i < 5; i++) {
      try {
        Thread.sleep(1);
      }
      catch(InterruptedException e) {}
      System.out.format("%s is in control\n", Thread.currentThread().getName());
    }
  }

  public void start() {
    System.out.format("Starting %s\n", threadName );
    if (t == null) {
      t = new Thread (this, threadName);
      t.start ();
    }

  }

  @Override
  public void run() {
    for(int i = 0; i < 5; i++) {
      System.out.format("%s is in control\n", threadName);
    }
  }
}
