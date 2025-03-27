from collections import deque

# 双端队列常见用法：从右边入队，左边出队O(1)
q = deque()
q.append(2)
# q.appendleft(1)  # 不推荐 O(n)
x = q.popleft()  # 从左出队，有返回值

print(q)

""" 栈 """
# 获取栈顶 stack[-1]
stk = []
stk.append(1)  # 入栈
x = stk.pop  # 出战

print(stk)
