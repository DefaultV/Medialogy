import java.net.*;

public class program extends Thread{

  public static void main(String[] args) throws Exception{
    byte[] buf = new byte[512];
    byte[] tmp = new byte[1];
    DatagramSocket socket = new DatagramSocket();
    InetAddress ip = InetAddress.getByName("www.djxmmx.net");

    DatagramPacket send = new DatagramPacket(tmp, tmp.length, ip, 17);
    DatagramPacket get = new DatagramPacket(buf, buf.length);

    socket.send(send);
    socket.receive(get);

    System.out.format("%s", new String(get.getData()));
  }
}
