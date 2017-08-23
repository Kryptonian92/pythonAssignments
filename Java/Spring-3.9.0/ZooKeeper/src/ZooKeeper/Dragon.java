package ZooKeeper;

public class Dragon extends Mammal{
	
	public void fly() {
		System.out.println("Swoosh!");
		this.setDenergy(this.getDenergy()-50);
	}
	public void eatHumans() {
		System.out.println("Yumm Delicious!");
		this.setDenergy(this.getDenergy()+25);
	}
	public void attackTown() {
		System.out.println("HE'S BURNING EVERYTHING!!");
		this.setDenergy(this.getDenergy()-100);
	}
}
