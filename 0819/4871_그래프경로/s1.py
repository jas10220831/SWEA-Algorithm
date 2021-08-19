import sys
sys.stdin = open('sample_input.txt')

# 경로 행렬만들기
T = int(input())
dot, line = map(int, input().split())
road = [[0] * (dot+1) for _ in range(dot+1)]
for _ in range(line):
    dot1, dot2 = map(int, input().split())
    road[dot1][dot2] += 1
start, goal = map(int, input().split())

def find_road(road, dot, start, goal):
    dot_check = [0] * dot
