- 3 找到无重复的最长子串:中间没有重复出现的字符
  - 利用集合set对其出现字符进行统计

- 4 在两个正序的数组中找到合并后的中位数
  - 分别对两个数组采用二分法，以降低时间复杂度

- 11 找到以index为底，值为高的最大面积
  - 从左右两个指针开始，注意先向内移动值小的指针

- 142 找到链表哪里连接成环，此链表不会在中间有环
  - 利用快慢指针法，一个先走2步，一个走1步至相遇点x,x处固定一指针，再选取另一指针从起点处，二者分别以1步开始走直至相遇，此时相遇点即为环连接处，具体说明（证明见网站题解）见题解。

- 146 
  - 关键在于OrderDict的应用，以及 popitem,由于字典是没有顺序的，应该是只考虑时间顺序的

- 287 找到数组中的重合数
  - 将数组中的数相像成指针，这里同样采用快慢指针的方法，快的走两步，慢的走一步，快的只要是闭合的就一定会追上慢的

- 560_974 这边寻找的数组皆为连续子数组，和为K或为K的倍数
  - 选取一个字典初始化{0:1},这是为了防止第一个就符合条件，presum-k在hashmap中，说明中间子数组和为K; 如果得到的余数之间出现过那说明新加入的连续子数组为K的倍数