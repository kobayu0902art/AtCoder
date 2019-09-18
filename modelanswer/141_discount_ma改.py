import heapq

n, m = map(int, input().split())
a = list(map(lambda x: int(x)*(-1), input().split()))
heapq.heapify(a)  # aを優先度付きキューに

for _ in range(m):
    tmp_min = heapq.heappop(a)
    heapq.heappush(a, (-1)*(-tmp_min//2))  # 計算誤差の関係で-1を2回かけてます
print(-sum(a))