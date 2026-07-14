scores = [12,34,23,532,5553,23,6,4223,13315,64424,42442,124]
max_score = 0
print(max(scores))

# for loop with list

for score in scores:
  if max_score < score:
    max_score = score

print(max_score)
sum=0
# for loop with range
for num in range(1,101):
  sum+=num
print(sum)