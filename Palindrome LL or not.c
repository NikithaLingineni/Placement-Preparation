struct ListNode* reverselist(struct ListNode* head)
{
    struct ListNode* prevnode=NULL,*nextnode,*temp=head;
    while(temp!=NULL)
    {
        nextnode=temp->next;
        temp->next=prevnode;
        prevnode=temp;
        temp=nextnode;
    }
    return prevnode;
}
bool isPalindrome(struct ListNode* head) {
    if(head==NULL || head->next==NULL)
        return true;
    struct ListNode*slow=head,*fast=head;
    while(fast->next!=NULL && fast->next->next!=NULL)
    {
        slow=slow->next;
        fast=fast->next->next;
    }
    slow->next=reverselist(slow->next);
    slow=slow->next;
    while(slow!=NULL)
    {
        if(head->val!=slow->val)
            return false;
        slow=slow->next;
        head=head->next;
    }
    return true;  
}
