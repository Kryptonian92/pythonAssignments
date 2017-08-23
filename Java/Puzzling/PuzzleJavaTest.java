import java.util.*;
import java.util.Collections;
import java.lang.Math;

class PuzzleJavaTest{
  public static void main(String[] args) {
    PuzzleJava iD = new PuzzleJava();
    int [] sumarray = {3,5,1,2,7,9,8,13,25,32};
    System.out.println(iD.getSum(sumarray));

    ArrayList<String> japaneseFolks = new ArrayList<>();

    japaneseFolks.add("Nancy");
    japaneseFolks.add("Jinichi");
    japaneseFolks.add("Fujibayashi");
    japaneseFolks.add("Momochi");
    japaneseFolks.add("Ishikawa");
    japaneseFolks.add("Tim");

    System.out.println(iD.japaneseFolks(japaneseFolks));

    char[] alphabet_array = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
    iD.alphabet(alphabet_array);
  }
}
