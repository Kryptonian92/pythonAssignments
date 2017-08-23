package ZooKeeper;

public class Gorilla extends Mammal {
	
	public void toss() {
		System.out.println("Throwing a Banana");
		this.setEnergy(this.getEnergy()-5);
	}
	public void eatBananas() {
		System.out.println("Eating Bananas");
		this.setEnergy(this.getEnergy()+10);
	}
	public void climb() {
		System.out.println("Climbing a tree");
		this.setEnergy(this.getEnergy()-10);
	}

}
