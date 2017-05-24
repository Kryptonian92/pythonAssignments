function Node(val){
  this.val = val;
  this.next = null;
}
function SLL(){
  this.head = null;
  this.insert = function(val){
    // if this.head === null, do something
    if(!this.head){
      this.head = new Node(val) // pointing the head to a new node
       return this.head // once this.head is pointing to the new Node, return this.head
    }
    //
    var current = this.head // set current variable to this.head
    while(current.next){ //  while current node has a next
      current = current.next; // set current to the next node
    } // leave while loop, when current no longer has a next
    console.log("the current node is:", current) // currentis now the last node
    current.next = new Node(val); // set current's next pointer to a newly created node
    return this.head
  }
}
var list1 = new SLL()// create the new list
list1.insert(1) // insert a node with val of 4 into newly created list
list1.insert(2) // insert a node with val of 4 into newly created list
list1.insert(3) // insert a node with val of 4 into newly created list
list1.insert(4) // insert a node with val of 4 into newly created list


console.log(list1)
// console.log(list1.head.next)
// console.log(list1.head.val)
