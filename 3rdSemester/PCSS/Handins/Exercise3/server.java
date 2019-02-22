import java.net.*;
import java.io.*;

public class server{

  public static void main(String[] args){
    server serv = new server();
    serv.HandleClient();
  }

  server(){

  }

  void HandleClient(){
    new Thread(() -> {
      try{
        ServerSocket servsoc = new ServerSocket(8080);
        while(true){
          Socket soc = servsoc.accept();
          System.out.format("InetAccept: %s\n", soc.getInetAddress().toString());

          DataInputStream i_client = new DataInputStream(soc.getInputStream());
          DataOutputStream o_client = new DataOutputStream(soc.getOutputStream());
        new Thread(new ThreadClient(soc, i_client, o_client)).start(); 
        }
      }
      catch(Exception e){System.out.format("%s", e.getMessage());}
    }).start();
  }
}

class ThreadClient implements Runnable{
  private Socket soc;

  DataInputStream i_client;
  DataOutputStream o_client;

  public ThreadClient(Socket soc, DataInputStream i, DataOutputStream o){
    this.soc = soc;
    this.i_client = i;
    this.o_client = o;
  }

  @Override
  public void run(){
    while(true){
      try{
        float[] vals = new float[3];
        for (int i = 0; i <= 2; i++){
          float get = i_client.readFloat();
          vals[i] = get;
        }
        o_client.writeUTF(ComputeAll(vals));
      }
      catch(Exception e){}
    }
  }

  String ComputeAll(float[] vals){
    float l_amount = vals[0];
    float l_rate = (vals[1]/12)/100;
    float l_years = vals[2];
    
    //Monthly
    double month = l_amount*((l_rate*Math.pow(1+l_rate, l_years*12))/((Math.pow(1+l_rate, l_years*12))-1));
    //Total
    double total = l_amount*((l_rate*(1+l_rate))/((1+l_rate)-1));
    String ret = String.format("Month: %f\nTotal: %f\n", month, total);
    return ret;
  }
}
