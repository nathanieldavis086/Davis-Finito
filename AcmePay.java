import java.util.*;
public class AcmePay {
    public static void main(String[] args) throws Exception 
    {
            int choice = 1;
            Scanner input = new Scanner(System.in); {
            System.out.println("Please enter shift - 1 , 2 , or 3");
            int shift = input.nextInt();
//ask for participation in retirement plan if the second or third shift are selected
            if (shift == 2 || shift == 3)
            {
                System.out.println("Are you electing to participate in the retirement plan? Please enter 1 for yes or 2 for no:");
                choice = input.nextInt();
            }
            else
            {
                System.out.println("You are not eligible for the retirement plan");
            }

     //ask for hours worked
            System.out.println("Please enter the number of hours worked:");
            int hours = input.nextInt();
     
     

            double rate = payRate(shift);
            double gross = grossPay(rate, hours);
            
            System.out.println("Hours worked is " + hours);
            System.out.println("Hourly pay rate is " + rate);
            if (shift == 1)
            {
                System.out.println("You served the "+shift+"st shift");
            }
            else if (shift == 2)
            {
                
                System.out.println("You served the "+shift+"nd shift");
            }
            else
            {
                System.out.println("You served the "+shift+"rd shift");
            }
            hoursBreakdown(rate, hours);
            retirementPay(shift, choice, gross);
            }
    }


    public static double payRate(int shift)
    {
        
            if (shift == 1)
            {
                double rate = 17.0;
                return rate;
            }
            else if (shift == 2)
            {
                double rate = 18.5;
                return rate;
            }
            else
            {
                double rate = 22.0;
                return rate;
            }
    
    }

    public static void hoursBreakdown(double rate, double hours)
    {
        if (hours>40)
        {
                double otPay = (hours-40)*(rate*1.5);
                System.out.println("You earned " +otPay+" in overtime pay and "+((rate*40))+" in regular pay");
        }
    }

    public static double grossPay(double rate, double hours)
    {
        if (hours>40)
        {
                double otPay = (hours-40)*(rate*1.5);
                double everElse = rate*40;
                double gross = otPay+everElse;
                System.out.println("You earned " +otPay+" in overtime pay and "+everElse+" in regular pay");
                System.out.println("You earned a total of "+gross+" dollars");
                return gross;
        }
        else
        {
            double gross = hours*rate;
            System.out.println("You did not earn overtime pay, and your gross pay was "+gross);
            return gross;
        }
    }
    

    public static void retirementPay(int shift, int choice, double gross)
    {
        
        if ((shift == 2 || shift == 3) && choice == 1)
        {
            double retire = 0;
            retire += (gross*0.03);
            double netPay = gross-retire;
            System.out.println("Retirement Deduction is " + retire);
            System.out.println("Net Pay is ...................." + netPay);
        }
        else
        {
            System.out.println("Retirement Deduction is 0");
            System.out.println("Net Pay is ...................." + gross);
        }
        
    }
}

//I'm not sure what to put in the hoursBreakdown method, and I can't figure out what's with the return pay and return rate commands.

//Display: (1) the hours
//worked, (2) the shift, (3) the hourly pay rate, (4) the regular pay, (5) overtime pay, (6) the total of regular and
//overtime pay, and (7) the retirement deduction, if any, and (8) the net pay.

//case 1 <40 1st shift check
//case 2 <40 2nd/3rd shift no ret
//not regarding choice parameter in retirementPay