public class ProjectTest{
  public static void main(String[] args){
    Project p = new Project();
    p.setName("Test");
    p.setDescription("Here's a description");
    p.elevatorPitch();

    Project q = new Project("Test2");
    q.elevatorPitch();

    Project r = new Project("Test2" , "This is another test");
    r.elevatorPitch();

  }
}
