class FizzBuzz{
  public String FizzBuzz(int number){
    //logic
    String fizz = "Fizz";
    String buzz = "Buzz";
    String both = "FizzBuzz";
    if(number %3==0 && number %5==0){
      return both;
    }else if(number %5==0){
      return buzz;
    }else if(number %3==0){
      return fizz;
    }else{
      return "" + number;
    }
  }
}
