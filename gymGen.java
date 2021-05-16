import java.util.Scanner;
import java.io.*;
import java.util.Random;
import java.text.DecimalFormat;
public class gymGen {
    private static int maxUser = 1000, maxGymnast = 1000, maxTeam = 1000, maxLeague = 1000, 
        maxEmail = 1000, maxEvents = 6, maxName = 1000, maxLocation = 1000;
    private static int maxYear = 2030, minYear = 2020;
    private static int maxID = 99999999;
    private static Random rnd = new Random();
    private static String[] userNameArray = new String[maxUser];
    private static String[] nameArray = new String[maxName];
    private static String[] emailArray = new String[maxEmail];
    private static String[] leagueArray = new String[maxLeague];
    private static String[] teamArray = new String[maxTeam];
    private static String[] locationArray = new String[maxLocation];
    private static String[] eventArray = new String[maxEvents];

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
        // fill usernames
        Scanner in = openFile("userNames");
        i = 0;
        while (in.hasNext() && i < maxUser) {
          userNameArray[i++] = in.nextLine();
        }
        if (i < maxUser) maxUser = i;
        in.close();
        // fill first names
        in = openFile("firstNames");
        i = 0;
        while (in.hasNext() && i < maxName) {
          nameArray[i++] = in.nextLine();
        }
        if (i < maxName) maxName = i;
        in.close();
        // fill emails
        in = openFile("emails");
        i = 0;
        while (in.hasNext() && i < maxEmail) {
          emailArray[i++] = in.nextLine();
        }
        if (i < maxEmail) maxEmail = i;
        in.close();
        // fill league names
        in = openFile("leagueName");
        i = 0;
        while (in.hasNext() && i < maxLeague) {
          leagueArray[i++] = in.nextLine();
        }
        if (i < maxLeague) maxLeague = i;
        in.close();
        // fill team names
        in = openFile("teamNames");
        i = 0;
        while (in.hasNext() && i < maxTeam) {
          teamArray[i++] = in.nextLine();
        }
        if (i < maxTeam) maxTeam = i;
        in.close();
        // fill location names
        in = openFile("locationName");
        i = 0;
        while (in.hasNext() && i < maxLocation) {
          locationArray[i++] = in.nextLine();
        }
        if (i < maxLocation) maxLocation = i;
        in.close();
        // fill events names
        in = openFile("eventNames");
        i = 0;
        while (in.hasNext() && i < maxEvents) {
          eventArray[i++] = in.nextLine();
        }
        if (i < maxEvents) maxEvents = i;
        in.close();
    }

    private static String getUsername(){
        String name = userNameArray[rnd.nextInt(maxUser)];
        return "'" + name + "'";
    }

    private static String getEmail(){
        String email = emailArray[rnd.nextInt(maxEmail)];
        return "'" + email + "'";
    }

    private static String genPassword(){
        return "'" + System.out.format("%06d%n", rnd.nextInt(10000)) + "'";
    }

    private static String getName(){
        String name = nameArray[rnd.nextInt(maxUser)];
        return "'" + name + "'";
    }

    private static void createUsers(PrintWriter out){
        int i = 0;
        String s = "";
        while(i < 10){
            s = "'" + System.out.format("%08d%n", i++) + "', " + getUsername() + ", " + getEmail() + ", " + genPassword();
            out.println("insert into users value (" + s + ");");
        }
    }

    private static void createGymnasts(PrintWriter out){
        int i = 0;
        String s = "";
        while(i < 10){
            s = "'" + System.out.format("%08d%n", i++) + "', " + getName() + ", " + (String) 2020 + rnd.nextInt(10);
            out.println("insert into gymnasts value (" + s + ");");
        }
    }

    private static String[] createTeam(PrintWriter out, String[] gymnasts, int curr){
        for (int i=0; i<5; i++){

        }
    }

    // private static void createLeague(PrintWriter out){
    //     String[] gymnasts = String[1000];
    //     for (int i=0; i < 6; i++){
    //         createTeam(out, gymnasts,  5*i);
    //     }
    // }



    public static void main(String[] args) {
        int num_leagues = 1;
        int team_num = 1;
        int gym_num = 1;
        fillArrays();
        PrintWriter out = outputFile("largeRelationsInsertFile.sql");
        out.println("delete from users;");
        out.println("delete from league;");
        out.println("delete from team;");
        out.println("delete from gymnast;");
        out.println("delete from lineup_slot;");
        out.println("delete from score;");
        out.println("delete from user_league;");
        out.println("delete from roster;");
        out.println("delete from matchup;");


        createUsers(out);

        createGymnasts(out);

        // for (i=0; i < 10; i++) {
        //     createLeague(out);
        // } 
    }

}