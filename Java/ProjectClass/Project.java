public class Project{
  private String name;
  private String description;

  public Project(){
    this("","");
  }

  public Project(String name){
    this.name = name;
    this.description = "";
  }
  public Project(String name, String description){
    this.name = name;
    this.description = description;
  }

  public void setName(String name){
    this.name = name;
  }

  public String getName(){
    return this.name;
  }

  public void setDescription(){
    this.description = description;
  }

  public String getdescription(){
    return this.description;
  }

  public String elevatorPitch(){
    System.out.println(name + ":" + description);
    return name+":"+description;
  }
}
