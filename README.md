# leetcode
## array
### 88&119
对于一些增长型数列，每次增长会改变所有数，比如杨辉三角的每一行，可以考虑从最后往前更新
### 53
最大子序列，经典动态规划行为
### 62
注意分治思想
### 48
还有一种反转方法：357对角线对称一次，456中线对称一次
### 39
def A():中有变量a，函数B，a是B的全局变量<br>
copy.deepcopy(L)效果等同于L + []，但后者效果更好
### 64
可以从上到下，或者从左往右，按照行或者列做dp，不需要存储整个矩阵
### 75
第10行，判断如果是<,nums[high]这个数并没有被判断
### 40
上面是我的答案，下面是提交的比较快的方法：对比具体算法都是相同，但是时间快了一倍，后者结构较好<br>
很显然我的答案中主程序调用和递归中的判断重复，可以优化，但为什么快了这么多，不清楚
### 123
后序比前序方便的一点是边缘容易处理，有个比较快的答案用的的后序
### 105
用一些栈的性质修改list，比利用索引传递list子串快很多
### 74
二分查找大于、大于等于问题；取平均加一减一问题；mid减一加一问题
### 81
这个题做了很久，要先清楚具体具体步骤而不是熟悉了算法就开始做
### 56
比较容易想到的方法是，对start从小到大排序，然后从前往后扫<br>
我用的方法是对所有start和end分开排序，从新构造区间，事实证明可行，相对不好想，代码也比前者难<br>
实际上前面只需要一次排序，而排序比较费时间，所有前面更快
### 63
精妙的DP