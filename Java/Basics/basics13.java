import java.util.*;

class basics13{
  //1-255
  // public void twoFiftyFive(){
  //   for(int i=0; i<256; i++){
  //     System.out.println(i);
  //   }
  // }

  //odd 255
  public void twoFiftyFive(){
    for(int i=0; i<256; i++){
      if(i %2 ==1){
      System.out.println(i);
    }
  }
}
  //min max average
  public void mma(int[] arr){
    int sum = 0;
    int avg;
    int max = arr[0];
    int min = arr[0];
    for(int i=0; i< arr.length; i++){
      sum = arr[i] + sum;
      if(arr[i] > max){
        max = arr[i];
      }
      if(arr[i] < min){
        min = arr[i];
      }
    }
    avg = sum/arr.length;
    // ing [] mmaStuff = new int[2];
    int [] mmaStuff = {min, max, avg};
    System.out.println(Arrays.toString(mmaStuff));
  }
  // greater than y
  // public void gty(int[] arr, int y){
  //   int count = 0;
  //   for(int x = 0; x < arr.length; x++){
  //     if(arr[x] < y){
  //       count ++;
  //     }
  //   }
  //   System.out.println(count);
  // }
  // sum 255
  // public void sum255(){
  //   int sum = 0;
  //   fir(int i = 0; i < 256; i++){
  //     sum += i;
  //   }
  //   System.out.println(sum);
  // }
  // square array values
  // public void sqVals(int[] arr){
  //
  //   for(int i = 0; i < arr.length; i++){
  //     arr[i] = arr[i] * arr[i];
  //   }
  //   System.out.println(Arrays.toString(arr));
  // }
  //iterate array
  //shift 1
  public void shiftOne(int [] arr){
    for(int i=0; i<arr.length; i++){
      try{
        arr[i] = arr[i + 1];

      } catch(ArrayIndexOutOfBoundsException
      e) {
        arr[i]=0;
      }
    }
    System.out.println(Arrays.toString(arr));
  }
  //swap negs with 0
  //
}
