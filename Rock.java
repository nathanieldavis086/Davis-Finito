import java.util.Scanner;

public class Rock
{
public static void main(String[] args)
{

//hallmark loop
int mewin = 0;
int uwin = 0;
int ties = 0;
for (int i = 0; i<10; i++)
{
  Scanner scan = new Scanner(System.in);
  System.out.println("Enter your play: Rock, Paper, Scissors");
  String personPlay = scan.nextLine().toUpperCase();
  String computerPlay = ""; //Computer's play -- "R", "P", or "S"
  int computerInt = (int)(Math.random()*((2)+1)); //Randomly generated number for computer play

  
//Get player's play -- note that this is stored as a string DONE
//Make player's play uppercase for ease of comparison DONE
//Generate computer's play (0,1,2). Use the Math.random() method DONE
//Translate computer's randomly generated play to string
//The below code uses if statements; change this to a switch statement. DONE




if (!(personPlay.startsWith("SC") || personPlay.startsWith("RO") || personPlay.startsWith("PA")))
{
    System.out.println("Error: Invalid input");
    System.out.println("Enter your play: Rock, Paper, Scissors");
    personPlay = scan.nextLine();
    personPlay = personPlay.toUpperCase();

}

else
{
    switch (computerInt)
{
    case 0:
    computerPlay = "RO";
    break;
    case 1:
    computerPlay = "PA";
    break;
    case 2:
    computerPlay = "SC";
    break;
}

System.out.println("I pick " + computerPlay);

    
    //... Fill in rest of code  DONE
    //Print computer's play  DONE
    //See who won. Use nested ifs instead of &&.  DONE
  

    if (personPlay.substring(0,2).equals(computerPlay))
    {System.out.println("It's a tie!");
    ties += 1;}
  else if (personPlay.substring(0,2).equals("RO"))
      {
        if (computerPlay.equals("SC"))
        {System.out.println("Rock crushes scissors. You win!");
        uwin += 1;}
      else if (computerPlay.equals("PA"))
        {System.out.println("Paper wraps rock. I win!");
        mewin += 1;}
      }

  else if (personPlay.substring(0,2).equals("SC"))
  {
    if (computerPlay.equals("RO"))
        {System.out.println("Rock crushes scissors. I win!");
        mewin += 1;}
      else if (computerPlay.equals("PA"))
        {System.out.println("Scissors cuts paper. You win!");
        uwin += 1;}
  }
      

  else if (personPlay.substring(0,2).equals("PA"))
  {
    if (computerPlay.equals("RO"))
        {System.out.println("Paper wraps rock. You win!");
        uwin += 1;}
      else if (computerPlay.equals("SC"))
        {System.out.println("Scissors cuts paper. I win!");
        mewin += 1;}
  }
}

}
System.out.print("You won "+uwin+" games and I won "+mewin+" games. We tied "+ties+" games.");
}
}
