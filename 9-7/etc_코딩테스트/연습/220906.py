def solution(survey, choices):
    answer = ''
    'RT'
    'CF'
    'JM'
    'AN'
    MBTI_dict = {
        'RT': 0,
        'CF': 0,
        'JM': 0,
        'AN': 0
    }
    
    # 반복문
    for i in range(len(survey)):
        mbti = survey[i]
        if mbti in MBTI_dict:
            # 양수일 경우, 앞에 나오는 유형이 +
            # 음수일 경우, 뒤에 나오는 유형이 +
            score = 4 - choices[i]
            # 계산된 점수를 데이터에 최신화
            MBTI_dict[mbti] += score
        # 반대의 경우,
        elif mbti[::-1] in MBTI_dict:
            score = choices[i] - 4
            MBTI_dict[mbti[::-1]] += score
    
    # 계산된 결과를 가지고,
    for key in MBTI_dict:
        # 0보다 크거나 같으면, 앞을 선택
        if MBTI_dict[key] >= 0:
            answer+=key[0]
        # 아닐 경우, 뒤를 선택
        else:
            answer+=key[1]
                
    return answer
    

# 백현님 풀이
def solution(survey, choices):
    index_dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        if choices[i] >= 4:
            index_dict[survey[i][1]] += choices[i] - 4
        elif choices[i] <= 3:
            index_dict[survey[i][0]] += 4 - choices[i]

    if index_dict['R'] > index_dict['T']:
        index1 = 'R'
    elif index_dict['R'] < index_dict['T']:
        index1 = 'T'
    else:
        index1 = 'R'

    if index_dict['C'] > index_dict['F']:
        index2 = 'C'
    elif index_dict['C'] < index_dict['F']:
        index2 = 'F'
    else:
        index2 = 'C'

    if index_dict['J'] > index_dict['M']:
        index3 = 'J'
    elif index_dict['J'] < index_dict['M']:
        index3 = 'M'
    else:
        index3 = 'J'

    if index_dict['A'] > index_dict['N']:
        index4 = 'A'
    elif index_dict['A'] < index_dict['N']:
        index4 = 'N'
    else:
        index4 = 'A'

    answer = index1 + index2 + index3 + index4

    return answer


# 재웅님 풀이
def solution(survey, choices):
    answer = ''
    # 점수 계산 딕트
    tr_dict = {
        'R' : 0,
        'C' : 0,
        'J' : 0,
        'A' : 0
    }
    # 각 질문이 성격의 질문인지 확인
    for n in range(len(survey)) :
        # 정렬하여 확인
        temp_list = sorted([survey[n][1], survey[n][0]])
        # 성격유형 , 역순인지 확인용 첫번쨰 문자
        trait = [temp_list[0], survey[n][0]]
    # 위치값에 따라 점수 변동 반영
        if trait[0] == trait[1]:
            p_m = 1
        else :
            p_m = -1
    # 총점 계산
        cal = tr_dict[trait[0]] + p_m * (4 - choices[n])
        tr_dict[trait[0]] = cal
    # 해당 질문 없으면 오름차순으로 값 리턴
    if tr_dict['R'] >= 0 :
        answer += 'R'
    else : answer += 'T'
   
    if tr_dict['C'] >= 0 :
        answer += 'C'
    else : answer += 'F'
   
    if tr_dict['J'] >= 0 :
        answer += 'J'
    else : answer += 'M'
   
    if tr_dict['A'] >= 0 :
        answer += 'A'
    else : answer += 'N'
   
    return answer