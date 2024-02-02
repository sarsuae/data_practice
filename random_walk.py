import random
import matplotlib.pyplot as plt

# 模擬的社交網路
social_network = {
  'Alice': ['Bob', 'Charlie', 'David'],
  'Bob': ['Alice', 'David'],
  'Charlie': ['Alice', 'David'],
  'David': ['Alice', 'Bob', 'Charlie'],
}

# 開始的人
person = 'Alice'
# 保存隨機漫步的人
path = [person]

# 進行10步隨機漫步
for _ in range(10):
  person = random.choice(social_network[person])
  path.append(person)

print('Random walk path:')
print(' -> '.join(path))