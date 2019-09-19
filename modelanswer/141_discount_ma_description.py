import heapq

n, m = map(int, input().split())
a = list(map(lambda x: int(x)*(-1), input().split()))
heapq.heapify(a)  

for _ in range(m):
    print(heapq.nlargest(len(a),a))
    tmp_min = heapq.heappop(a)
    print("tmp_min",tmp_min)
    print("(-1)*(-tmp_min//2)",(-1)*(-tmp_min//2))
    print("(-tmp_min//2)",(-tmp_min//2))
    print("tmp_min//2",tmp_min//2)
    heapq.heappush(a, (-1)*(-tmp_min//2))

print(-sum(a))