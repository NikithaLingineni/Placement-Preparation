struct ListNode *detectCycle(struct ListNode *head) {
    struct ListNode * slow,*fast;
    slow=head;
    fast=head;
    if(head==NULL || head->next==NULL)
        return NULL;
    while(fast!=NULL && fast->next!=NULL)
    {
        fast=fast->next->next;
        slow=slow->next;
        if(slow==fast)
            break;
    }
    if(fast==NULL || fast->next==NULL)
        return NULL;
    slow=head;
    while(slow!=fast)
    {
        fast=fast->next;
        slow=slow->next;
    }
    return slow;
}
