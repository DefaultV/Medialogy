
public class MyTask implements Runnable{
  String threadName;
  Thread t;

  public static void main(String[] args){
    Thread thread = new Thread(new MyTask("Task1"));
    Thread thread2 = new Thread(new MyTask("Task2"));
    
    thread.start();
    thread2.start();
  }

  MyTask(String threadname){
    this.threadName = threadname;
  }

  void start(){
    if (this.t == null){
      t = new Thread();
      t.start();
    }
  }

  @Override
  public void run(){
    try{
      for (int i = 0;i <= 9;i++){
        //Thread.sleep(1000);
        System.out.format("Hello World %d\n", i);
      }
    }
    catch(Exception e){
    }
  }
}
