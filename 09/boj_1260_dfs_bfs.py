def dfs(v,N): #v는 시작점, N은 정점의 개수
    visited_dfs[v] = 1
    print(v, end='')


N, M, V = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]  # 연결상태체크

visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)

for i in range(M):
    n1, n2 = map(int, input().split())
    arr[n1][n2] = arr[n2][n1] = 1  # 정점끼리 연결해준다.
