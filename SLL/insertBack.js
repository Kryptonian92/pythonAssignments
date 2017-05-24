function Node(val){
  this.val = val;
  this.next = null;
}
function SLL(){
  this.head = null;
  this.insert = function(val){
    if(!this.head){
      this.head= new Node(val)
      return this.head
    }
    var current = this.head;
    while (current.next){
      current = current.next
    }
    current.next = new Node(val)
    return this.head
  }
}

list1.insert(1)
list1.insert(2)
list1.insert(3)
list1.insert(4)
