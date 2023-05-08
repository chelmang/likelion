# 리스트(lists)

#mbti = ['INFP', 'ENFP', 'ISTJ', 'ESTP']

#print(mbti)
#print(mbti[0])

#mbti[0] = 'INFJ'

#print(mbti)
#print(mbti[0])


#my_list = [123, 'apple']
#print(my_list)

#colors = ['red', 'blue', 'green']

#수정
#colors[2] = 'black'
#print(colors)

#추가1
#colors.append('purple')
#print(colors)

#추가2
#colors.insert(1, 'yellow')
#print(colors)

#제거1
#del colors[0]
#print(colors)

#제거2
#color= colors.pop(0) #인덱스 없으면 맨마지막 요소 제거
#print(colors)
#print(color)

# 제거3
#colors.remove('blue')
#print(colors)

#colors = ['blue', 'red', 'grey', 'black', 'yellow', 'orange']

# 정렬 1 
#colors.sort()
#print(colors)

#colors.sort(reverse=True)
#print(colors)

#정렬2
#sorted(colors)
#print(sorted(colors))


#길이 - 요소의 갯수
#print(len(colors))

#에러
#print(colors[7])

#print(colors[-1]) #맨마지막 요소

#리스트 슬라이싱
#colors = ['blue', 'red', 'grey', 'black', 'yellow', 'orange']

#colors_2 = colors[:]

#print(colors_2)

#print(colors[1:5])
#print(colors[:4])
#print(colors[2:])

#print(colors[-5:])

scores = [88, 100, 96, 43, 65, 78]

#max_val = max(scores)
#min_val = min(scores)
sum_val = sum(scores)
avg_val = sum(scores) / len(scores)

print(avg_val)

#sum_values = 0
#for score in scores:
#    sum_value = sum_values + score
#    print(sum_values)


#scores.sort(reverse=True)

#for score in scores:
#   if score >= 80:
#       print(score)
#   else:
#       print("Fail")




