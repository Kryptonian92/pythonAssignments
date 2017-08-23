import java.util.ArrayList;
import java.util.Collections;
import java.lang.Math;
import java.util.Random;

public class PuzzleJava{
  Random random = new Random();
  public ArrayList<Integer> getSum(int[] array){
    ArrayList<Integer> array2 = new
    ArrayList<>();
    Integer sum = 0;
    for (int i=0; i<array.length; i++ ) {
      sum += array[i];
      if(array[i] > 10){
        array2.add(array[i]);
      }
    }
    System.out.println(sum);
    return array2;
  }


  public ArrayList<String>japaneseFolks(ArrayList<String> array3){
    ArrayList<String> array4 = new
    ArrayList<>();
    Collections.shuffle(array3);
    for (int y=0; y<array3.size(); y++) {
        if(array3.get(y).length() > 5){
          array4.add(array3.get(y));
        }
        System.out.println(array3.get(y));
    }
    return array4;
  }


public void alphabet(char[] array5){
  char[] vowels = {'a', 'e', 'i', 'o', 'u'};
  int temp;
  char current;
  for(int u=0; u < array5.length; u++){
    temp = random.nextInt(array5.length);
    current = array5[u];
    array5[temp] = current;
    array5[u] = array5[temp];
      }
  for (int e=0; e < vowels.length; e++){
    if(array5[0] == vowels[e]){
      System.out.println("This is a vowel");
    }
  }
  System.out.println(array5[array5.length - 1]);
  System.out.println(array5[0]);
  }
  }
}
