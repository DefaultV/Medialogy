import java.util.*;
import java.net.*;
import java.io.*;

public class programstats extends Thread{

  public static void main(String[] args) throws Exception{
    List<String> l_str = new ArrayList<String>();
    byte[] buf = new byte[512];
    byte[] tmp = new byte[1];
    DatagramSocket socket = new DatagramSocket();
    InetAddress ip = InetAddress.getByName("www.djxmmx.net");
    long s_t = System.currentTimeMillis();
    while(true){
      (new Thread(() -> {
        try{
          DatagramPacket send = new DatagramPacket(tmp, tmp.length, ip, 17);
          DatagramPacket get = new DatagramPacket(buf, buf.length);

          socket.send(send);
          socket.receive(get);

          l_str.add(new String(get.getData()));
          long end = System.currentTimeMillis() - s_t;
          SortAndShow(l_str, end);

        } catch (Exception e){}
      })).start();
    }
  }

  static void SortAndShow(List<String> list, long elap){
    Collections.sort(list);
    Set<String> hashsetList = new HashSet<String>(list);
    int fsize = hashsetList.size(); int ssize = list.size();
    float calc = ((float)fsize/(float)ssize) * 100;
    System.out.format("len: %d, occ: %d; percentage %.2f%% -> %d milliseconds\n", list.size(), hashsetList.size(), calc, elap);
    /*if (ssize >= 740){
      try{
      WriteToFile(hashsetList);
      System.exit(0);
      } catch(Exception e){}
      }*/
  }

  static void WriteToFile(Set<String> hashset) throws Exception{
    FileOutputStream fos = new FileOutputStream("Data", true);
    for (String s : hashset){
      fos.write((s+"\n").getBytes());
    }
  }
}
