'''
양의 정수 n이 매개변수로 주어집니다. 
n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.
'''

def solution(n):
    result = [[0]*n for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    x,y,direction = 0,0,0
    for count in range(1,n*n+1):
        result[x][y] = count
        
        nx, ny = x+dx[direction], y+dy[direction]
        
        if 0<=nx<n and 0<=ny<n and result[nx][ny]==0:
            x,y = nx,ny
        else:
            direction =(direction+1)%4
            x += dx[direction]
            y += dy[direction]
    return result

  '''
  def solution(n):
    answer = [[None for j in range(n)] for i in range(n)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    x, y, m = 0, 0, 0
    for i in range(1, n**2 + 1):
        answer[y][x] = i
        if y + move[m][0] >= n or x + move[m][1] >= n or answer[y + move[m][0]][x + move[m][1]]:
            m = (m + 1) % len(move)
        y, x = y + move[m][0], x + move[m][1]
    return answer
'''
