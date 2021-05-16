import java.util.Scanner;
import java.io.*;
import java.util.Random;
import java.text.DecimalFormat;
public class gymGen {
    // private static int maxUser = 100, maxGymnast = 1000, maxTeam = 20000, maxLeague = 

    private static Scanner openFile(String fileName) {
        Scanner in = null;
        try {
        in = new Scanner(new FileInputStream (fileName));
        }
        catch(FileNotFoundException e) {
        System.out.println ("Could not open the file");
        System.exit (0);
        }
        return in;
    }
    private static PrintWriter outputFile(String fileName) {
        PrintWriter out = null;
        try {
        out = new PrintWriter (new FileOutputStream (fileName));
        }
        catch (FileNotFoundException e) {
        System.out.println ("Could not open the file");
        System.exit (0);
        }
        return out;
    }
    private static void fillArrays() {
    int i;
    // fill first names
    Scanner in = openFile("buildingNames");
    i = 0;
    while (in.hasNext() && i < maxBuilding) {
      buildingArray[i++] = in.nextLine();
    }
    if (i < maxBuilding) maxBuilding = i;
    in.close();
    // fill last names
    Scanner in = openFile("buildingNames");
    i = 0;
    while (in.hasNext() && i < maxBuilding) {
      buildingArray[i++] = in.nextLine();
    }
    if (i < maxBuilding) maxBuilding = i;
    in.close();
    // fill emails
    Scanner in = openFile("buildingNames");
    i = 0;
    while (in.hasNext() && i < maxBuilding) {
      buildingArray[i++] = in.nextLine();
    }
    if (i < maxBuilding) maxBuilding = i;
    in.close();
    // fill team/league names
    in = openFile("personNames");
    i = 0;
    while (in.hasNext() && i < maxName) {
      nameArray[i++] = in.nextLine();
    }
    if (i < maxName) maxName = i;
    in.close();
    // fill events names
    Scanner in = openFile("buildingNames");
    i = 0;
    while (in.hasNext() && i < maxBuilding) {
      buildingArray[i++] = in.nextLine();
    }
    if (i < maxBuilding) maxBuilding = i;
    in.close();
  }

    public static void main(String[] args) {
        int num_leagues = 1;
        int team_num = 1;
        int gym_num = 1;
        fillArrays();
        PrintWriter out = outputFile("largeRelationsInsertFile.sql");
        for 
    }

}