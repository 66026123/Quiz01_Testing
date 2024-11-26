public class quiz01 {
    private static int count;

    public static int countLetter_A(String word){

        for (int i = 0; i< word.length(); i++) {
            if (word.charAt(i)=='a'||word.charAt(i)=='A'){
                count++;
            }
        }
        return count;
    }
}