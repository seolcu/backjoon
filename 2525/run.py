h, m = map(int, input().split())
current_time = h * 60 + m

duration = int(input())
after_time = current_time + duration

after_h = (after_time // 60) % 24
after_m = after_time % 60

print(after_h, after_m)
