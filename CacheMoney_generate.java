import java.util.Scanner;
import java.io.*;
import java.util.Random;
import java.text.DecimalFormat;

public class CacheMoney_generate {
    private static int maxUser = 1000, maxGymnast = 1000, maxTeam = 1000, maxLeague = 1000, 
        maxEmail = 1000, maxEvents = 6, maxName = 1000, maxLocation = 1000, numLeague = 25000;
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
    private static String[] users = new String[maxUser];
    private static String[] gymnasts = new String[maxGymnast];
    private static int score_id = 1;
    private static int week = 0;
    private static String[] teams;

    private static Scanner openFile(String fileName) {
        Scanner in = null;
        try {
        in = new Scanner(new FileInputStream (fileName));
        }
        catch(FileNotFoundException e) {
        System.out.println ("Could not open the file: " + fileName);
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
        System.out.println ("Could not open the file: " + fileName);
        System.exit (0);
        }
        return out;
    }
    private static void fillArrays() {
        int i;
        // fill usernames
        Scanner in = openFile("userNames.txt");
        i = 0;
        while (in.hasNext() && i < maxUser) {
          userNameArray[i++] = in.nextLine();
        }
        if (i < maxUser) maxUser = i;
        in.close();
        // fill first names
        in = openFile("firstNames.txt");
        i = 0;
        while (in.hasNext() && i < maxName) {
          nameArray[i++] = in.nextLine();
        }
        if (i < maxName) maxName = i;
        in.close();
        // fill emails
        in = openFile("emails.txt");
        i = 0;
        while (in.hasNext() && i < maxEmail) {
          emailArray[i++] = in.nextLine();
        }
        if (i < maxEmail) maxEmail = i;
        in.close();
        // fill league names
        in = openFile("leagueName.txt");
        i = 0;
        while (in.hasNext() && i < maxLeague) {
          leagueArray[i++] = in.nextLine();
        }
        if (i < maxLeague) maxLeague = i;
        in.close();
        // fill team names
        in = openFile("teamNames.txt");
        i = 0;
        while (in.hasNext() && i < maxTeam) {
          teamArray[i++] = in.nextLine();
        }
        if (i < maxTeam) maxTeam = i;
        in.close();
        // fill location names
        in = openFile("locationName.txt");
        i = 0;
        while (in.hasNext() && i < maxLocation) {
          locationArray[i++] = in.nextLine();
        }
        if (i < maxLocation) maxLocation = i;
        in.close();
        // fill events names
        in = openFile("eventNames.txt");
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
        return "'" + String.format("%06d%n", rnd.nextInt(10000)) + "'";
    }

    private static String getName(){
        String name = nameArray[rnd.nextInt(maxUser)];
        return "'" + name + "'";
    }

    private static String getLeague(){
        String league = leagueArray[rnd.nextInt(maxLeague)];
        return league;
    }

    private static String getTeam(){
        String team = teamArray[rnd.nextInt(maxTeam)];
        return team;
    }

    private static void createUsers(PrintWriter out){
        int i = 0;
        String s = "";
        String num = "";
        String name = "";
        while(i < maxUser){
            num = String.format("%08d", ++i);
            name = getUsername();
            s = "'" + num + "', " + name + ", " + getEmail() + ", " + genPassword();
            out.println("insert into users values (" + s + ");");
            users[i-1] = num;
        }
    }


    private static String getGymnast(){
        return gymnasts[rnd.nextInt(maxGymnast)];
    }

    private static String getUser(){
        return users[rnd.nextInt(maxUser)];
    }

    private static void createGymnasts(PrintWriter out){
        int i = 0;
        String s = "";
        String num = "";
        while(i < maxGymnast){
            num = String.format("%08d", ++i);
            s = "'" + num + "', " + getName() + ", " + String.valueOf(2020 + rnd.nextInt(10));
            out.println("insert into gymnast values (" + s + ");");
            gymnasts[i-1] = num;
        }
    }

    private static Boolean checkIn(String[] string, int length, String gym){
        boolean found = false;
        for (int i = 0; i < length; i++){
            if(string[i].equals(gym)){
                found=true;
            }
        }
        return found;
    }

    private static String[] createTeam(PrintWriter out, String[] gymnasts, int gl, String uid, String league_id, int ids){

        String id = String.format("%08d", ids);

        String s = id + "', '" + uid + "', '" + league_id + "', '" + getTeam() + "', "+ String.valueOf(rnd.nextInt(10)) + ", " + String.valueOf(rnd.nextInt(10));

        out.println("insert into team values ('" + s + ");");

        out.println("insert into user_league values ('" + uid + "', '" + league_id + "');");

        for (int i=0; i<6; i++){

            // System.out.println(gl);

            String curr = getGymnast();

            while (checkIn(gymnasts, gl, curr)){
                curr = getGymnast();
            }

            int year = 2000 + rnd.nextInt(30);


            gymnasts[gl++] = curr;

            out.println("insert into lineup_slot values ('" + id + "', '" + eventArray[i] + "', " + String.valueOf(i+1)
                + ", '" + curr + "');");

            out.println("insert into score values ('"+ String.format("%08d", score_id++) +"', '" + curr + "', '" + String.valueOf(year) + "-" + 
                String.valueOf(1 + rnd.nextInt(11)) + "-" + String.valueOf(1+rnd.nextInt(27)) + "', '" + eventArray[i]
                + "', " + String.valueOf(50 + rnd.nextInt(40)) + ");");

            out.println("insert into roster values ('" + id + "', '" + curr + "');");
        }

        return gymnasts;
    }
    
    private static String[] createLeague(PrintWriter out, int curr){

        int index = 0;
        int g_i = 0;
        String[] inputted = new String[10];
        String[] gymnasts = new String[maxGymnast];

        String manager = users[curr%maxUser];
        index++;
        inputted[index-1] = String.format("%08d", index+((curr-1)*10));;
        String league_id = String.format("%08d", curr); 

        out.println("insert into league values ('" + league_id + "', '" + manager + "', '" +  
            getLeague() + "', " + "6, 6);");

        gymnasts = createTeam(out, gymnasts, g_i, manager, league_id, index+((curr-1)*10));

        g_i += 5; //update this with how many gymnasts per team

        for (int i=1; i < 10; i++){
            String cu = users[(curr+i)%maxUser];
            index++;
            inputted[index-1] = String.format("%08d", index+((curr-1)*10));
            gymnasts = createTeam(out, gymnasts,  g_i, cu, league_id, index+((curr-1)*10));

            g_i += 5;
        }
        return inputted;
    }

    public static void main(String[] args) {
        System.out.println("gabe is so cute ");
        int num_leagues = 1;
        int team_num = 1;
        int gym_num = 1;
        fillArrays();
        PrintWriter out = outputFile("CacheMoney_large.sql");
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

        for (int i=0; i < numLeague; i++) {

            String[] teams = createLeague(out, i+1);
            for (int j=0; j < 5; j++){
            
                out.println("insert into matchup values ('" + teams[j] + "', '" + teams[9-j] + "', " + String.format("%08d", j) + ");");
                
            }
        } 
        out.close();
    }

}