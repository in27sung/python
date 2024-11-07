#리스트 연습문제

#1. 24년 11 월 개봉영화는 '청설', '아마존 활명수', '보통의 가족'이 있다.
# 영화제목을 move_list 이름의 리스트에 저장해보세요.
movie_list = ['청설', '아마존 활명수', '보통의 가족']

#2. movie_list에 "대도시의 사랑법" 를 마지막에 추가하세요.
movie_list.append('대도시의 사랑법')
print(movie_list)

#3. movie_list에서 '청설', '아마존 활명수' 사이에 '베놈: 라스트 댄스' 을 끼워넣으세요.
movie_list.insert(1, '베놈: 라스트 댄스')
print(movie_list)

#4. movie_list에서 '보통의 가족' 를 삭제하세요.
movie_list.remove('보통의 가족')
print(movie_list)


#5. movie_list에서 '베놈: 라스트 댄스', '아마존 활명수 를 삭제하세요.
# del movie_list[1:3]
del movie_list[2]
movie_list.pop(1)
print(movie_list)

#6. lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖는 langs 리스트를 만들어 출력하세요.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

#7. 다음 리스트에서 최댓값과 최솟값을 아래와 같이 출력하세요.
#   (min(), max() 함수를 사용하세요)
nums = [1, 2, 3, 4, 5, 6, 7]
print(f'최댓값: {max(nums)}, 최솟값: {min(nums)}')

#8. 다음 리스트의 합을 출력하세요.(sum() 함수 사용)
nums = [1, 2, 3, 4, 5]
print(f'리스트의 합: {sum(nums)}')

#9. 다음 리스트에 저장된 데이터의 개수를 화면에 구하세요.
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(f'cook 리스트의 갯수: {len(cook)}')

#10. 다음 리스트의 평균을 출력하세요.
nums = [1, 2, 3, 4, 5]
#실행
#예: 3.0
print(f'리스트의 평균: {sum(nums)/len(nums)}')

#11. price 변수에는 날짜와 가격 정보가 저장되어 있다.날짜 정보를 제외하고 가격 정보만 출력해보세요.
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(f'날짜 정보를 제외한 가격정보: {price[1:]}')

#12. 슬라이싱을 사용해서 홀수만 출력하세요.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'홀수 값: {nums[::2]}')

#13. 슬라이싱을 사용해서 짝수만 출력하세요.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'짝수 값: {nums[1::2]}')


#14. 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하세요.
nums = [1, 2, 3, 4, 5]
print(f'역방향으로 출력: {nums[::-1]} ')
print(f'역방향으로 출력: {nums.reverse()} ')

#15. a 리스트에는 아래의 데이터가 바인딩되어 있다.화면에 아래와 같이출력하세요.
a = ['itwill', 'busan', 'python']
#출력화면: itwill python
print(a[0], a[2])

#16. a 리스트에서 아래와 같이 화면에 출력하세요.(join 함수 사용)
a = ['itwill', 'busan', 'python']
#출력화면: itwill busan python
print(" ".join(a))

#17. join() 메서드를 사용해서 아래와 같이 화면에 출력해보자.
a = ['itwill', 'busan', 'python']
#출력화면:
# itwill
# busan
# python
print("\n".join(a))

#18. string = "itwill/busan/python" 문자열을 a 이름의 리스트로 분리 저장하세요.
string = "itwill/busan/python"
print(string.split('/'))

# 19. 리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

