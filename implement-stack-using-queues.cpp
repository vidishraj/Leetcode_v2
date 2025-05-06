class MyStack {
public: 
    //the idea is to insert at the front and remove from the front too 
    //
    queue <int> q1;
    queue <int> q2;
    
    MyStack(){
    }
    
    void push(int x) {
        q1.push(x);
    }
    
    int pop() {
        int num=q1.back();
        while(q1.size()!=1){
            q2.push(q1.front());
            q1.pop();
        }
        q1.pop();
        q1=q2;
        q2=queue<int>();
        return num;
    }
    
    int top() {
        return q1.back();
    }
    
    bool empty() {
        if( q1.empty()){
            return true;
        }
        return false;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */