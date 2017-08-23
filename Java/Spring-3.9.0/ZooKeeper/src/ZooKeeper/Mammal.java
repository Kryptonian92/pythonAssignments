package ZooKeeper;

public class Mammal {
	private int energy = 100;
	private int denergy = 300;
	
	public Mammal() {}
	
	public void setEnergy(int energy) {this.energy = energy;}
	public int getEnergy() {return energy;}
	
	public void setDenergy(int denergy) {this.denergy = denergy;}
	public int getDenergy() {return denergy;}
	
	public int displayEnergy() {
		System.out.println(energy);
		return energy;
	}
		

	public int displayDenergy() {
		System.out.println(denergy);
		return denergy;
	}
}
