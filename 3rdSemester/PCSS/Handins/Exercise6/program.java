import java.util.*;

public class program {
  public static void main(String args[]){
    // First part of exercise
    LinkedList<String> list = new LinkedList<String>();
    list.add("blue");
    list.add("green");
    list.add("yellow");
    list.add("white");
    list.addFirst("red");
    printList(list);  
    String tmp = list.removeLast();
    list.addFirst(tmp);
    printList(list);
    
    // Second part of exercise - Generic Queue

    GenericQueue<String> gq = new GenericQueue<String>();
    gq.enqueue("Tom");
    gq.enqueue("George");
    gq.enqueue("Peter");
    System.out.format("\n\n%s\n", gq.toString());
  }
  
  //For printing the list
  static void printList(LinkedList<String> list){
    System.out.format("\n");
    for (int i = 0; i < list.size(); i++){
      System.out.format("\n%d: %s", i, list.get(i));
    }
    System.out.format("\n");
    for (int i = list.size()-1; i >= 0; i--){
      System.out.format("\n%d: %s", i, list.get(i));
    }
  }
}

// Second part of exercise
class GenericQueue<T> extends LinkedList {
  private LinkedList<T> list = new LinkedList<T>();

  public void enqueue(T item){
    list.addLast(item);
  }

  public T dequeue(){
    return list.removeFirst();
  }

  public int getSize(){
    return list.size();
  }

  public String toString(){
    String str = "[";
    for (int i = 0; i < list.size(); i++){
      if (i+1 == list.size())
        str += String.format("%s", list.get(i));
      else
        str += String.format("%s, ", list.get(i));
    }
    str += "]";
    return str;
  }
}
