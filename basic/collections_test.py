# Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import defaultdict, Counter
a = 'aaaabbbbbcccc'

my_counter = Counter(a)
print(my_counter)


# 创建一个带默认值的字典
my_defaultdict = defaultdict(list)

# 访问不存在的键时，自动创建默认值
my_defaultdict['key'].append(1)
print(my_defaultdict)  # 输出: defaultdict(<class 'list'>, {'key': [1]})
