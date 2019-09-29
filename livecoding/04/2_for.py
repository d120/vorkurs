public class mehrSchleifen{
  public static void main(String[] args){
    for(int zaeler = 0; zaeler < 100; zaeler++){
      System.out.print(zaeler + " ");
    }

    //nach dem ersten ausfüren:
    for(int ausen = 0; ausen < 100; ausen++){
      System.out.println();
      for(int zaeler = 0; zaeler < 100; zaeler++){
        System.out.print(zaeler + " ");
      }
      //int notOK = 1;
    }
    //System.out.println(notOK);

    System.out.println();
    System.out.println();

    String input = "";
    do{
      System.out.println("ende?");
      input = Input.readString();
    }while(!input.equals("ende"));
  }
}
 

for i in range(100):
    print(i)
    
for x in range(10):
    zeile = ""
    for y in range(10):
        zeile += str(x * y) + " "
    print(zeile)
