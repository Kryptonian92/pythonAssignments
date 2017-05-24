function Node(val){
	this.val = val;
	this.next = null;
}
function SLL(){
	this.head = null;
	this.numbers = function(){
		count = 0;
		sum = 0;
		
		if (!this.head){
			return null
		}
		current = this.head;
		
		max = current.val;
		min = current.val;
		while(current){
			sum+=current.val
			if(current.val>max){
				max=current.val
				}
			if(current.val<min){
				min = current.val
			}
			current = current.next
			count++
		}
		avg = sum/count 
	}
	return dictionary{
		'max': max
		'min': min
		'avg': avg
	}
}
