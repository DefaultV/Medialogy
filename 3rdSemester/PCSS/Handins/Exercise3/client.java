import java.net.*;
import java.io.*;
import java.util.Scanner;

public class client{
  Scanner kb = new Scanner(System.in);
  DataOutputStream toServer = null;
  DataInputStream fromServer = null;

  public static void main(String[] args){
    client cli = new client();
    cli.Connect();
  }

  void Connect(){
    new Thread(() ->{
      try{
        Socket soc = new Socket("localhost", 8080);

        fromServer = new DataInputStream(soc.getInputStream());
        toServer = new DataOutputStream(soc.getOutputStream());

        while(true){ //Get 3 values needed for the calculation
          System.out.format("First enter the loan amount, then the interest rate, and finally the period in years.\n");
          for (int i = 0; i <= 2; i++){
            float ToSerb = kb.nextFloat();
            toServer.writeFloat(ToSerb);
          }

          System.out.format("Monthly and total:\n%s\n", fromServer.readUTF());
          System.out.println("Do you want to continue?\n");
          String resp = kb.nextLine();
          resp = kb.nextLine();
          if ("yes".equals(resp)){
            System.out.format("\nRestarting\n");
          }
          else{
            toServer.close();
            fromServer.close();
            soc.close();
            break;
          }
        }
      }
      catch(Exception e){}
    }).start();
  }
}
