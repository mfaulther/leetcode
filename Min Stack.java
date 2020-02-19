//https://leetcode.com/problems/min-stack
class MinStack {

    Stack<int[]> stack;
    int min;
    /** initialize your data structure here. */
    public MinStack() {
        stack = new Stack<>();
        min = 0;
    }
    
    public void push(int x) {
        if (stack.isEmpty())
        {
            min = x;
        }
        else
        {
            min = Math.min(min,x);
        }
        stack.push(new int[] {x, min});
    }
    
    public void pop() {
        stack.pop();
        if (!stack.isEmpty())
            min = stack.peek()[1];
    }
    
    public int top() {
        return stack.peek()[0];
    }
    
    public int getMin() {
        return stack.peek()[1];
    }
    
}
