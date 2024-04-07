# 题目：2023Q1A-删除重复数字后的最大数字
# 分值：200
# 作者：许老师-闭着眼睛学数理化
# 算法：单调栈
# 代码看不懂的地方，请直接在群上提问

from collections import Counter

num_lst = list(input()) # 把输入的字符串转化为字符列表，每个元素为一个数字字符
cnt = Counter(num_lst)  # 计数哈希表，记录每一个数字的出现次数
stack = list()          # 单调递减栈，更大的数字在栈底
used = set()            # 查看ch是否使用过
for num in num_lst:
    # 如果num位于used中，说明在此之前使用过了，无需入栈
    if num in used:
        cnt[num] -= 1   # cnt[ch]的计数-1
    # 如果ch不位于used中，要把ch加入栈顶
    else:
        # 在加入栈底之前，需要进行栈顶元素的检查，
        # 有可能要弹出若干栈顶元素，弹出的条件为：
        # 1.栈不为空；
        # 2.num大于栈顶元素stack[-1]
        # 3.栈顶元素的计数cnt[stack[-1]]大于1（即后面还有其他相同字符可用）
        while (len(stack) > 0 and num > stack[-1] and cnt[stack[-1]] > 1):
            cnt[stack[-1]] -= 1     # 对于栈顶弹出的元素，其计数-1
            used.remove(stack[-1])  # 同时在used集合中移除
            stack.pop()             # 栈顶元素弹出
        # 在进行完栈顶的检查之后，需要做两件事：
        # 1.把ch加入栈顶；
        # 2.把ch加入used哈希表，表示已经使用过
        stack.append(num)
        used.add(num)

# 最后需要把单调栈中的所有元素用join()方法合并成一个字符串并输出
print("".join(stack))