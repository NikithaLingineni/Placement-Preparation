int length(struct ListNode* currentnode){
    int len=0;
    while(currentnode!=NULL)
    {
        currentnode=currentnode->next;
        len++;
    }
    return len;
}
struct ListNode* reverseKGroup(struct ListNode* head, int k){
    if(length(head)<k)
        return head;
	int count=0;
	struct ListNode*temp,*prevnode=NULL,*currentnode=head,*nextnode=NULL;
	  while(currentnode!=NULL &&count<k)
	  {
		nextnode=currentnode->next;
		currentnode->next=prevnode;
		prevnode=currentnode;
		currentnode=nextnode;
          count++;
	  }
    if(nextnode!=NULL)
    {
        head->next=reverseKGroup(nextnode,k);
    }
    head=prevnode;
	return head;
}
