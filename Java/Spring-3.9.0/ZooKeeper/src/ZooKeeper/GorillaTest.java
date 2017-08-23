package ZooKeeper;

public class GorillaTest {
	public static void main(String[] args) {
		Gorilla h = new Gorilla();
		h.toss();
		h.toss();
		h.toss();
		
		h.eatBananas();
		h.eatBananas();
		
		h.climb();
		
		h.displayEnergy();
		
		Dragon wings = new Dragon();
		wings.attackTown();
		wings.attackTown();
		wings.attackTown();

		wings.eatHumans();
		wings.eatHumans();

		wings.fly();

		wings.displayDenergy();
	}

}
