def solution(id_list, report, k):
    answer = []
    # id_list = 유저 목록 (유니크함)
    # report = 신고 내역 ("신고자 신고당한자")
    # k = 정지 기준
    
    # 내가 생각한 알고리즘?
    # 누가 몇 번 신고당했는지 알아야 함
    # --> { user_id: set() }
    # user별로 신고당한 횟수가 k번 이상인 경우 정지
    # --> len(set())
    report_info = {}
    for user in id_list:
        report_info[user] = set()
    
    # 메일을 몇 통 받아야하는지 알아야 함
    # --> { user_id: 0 }
    mail_info = {}
    for user in id_list:
        mail_info[user] = 0

    # 신고내역을 하나씩 확인하면서 
    # 신고당한사람: 신고한 사람들 목록을 채워준다.
    for report_detail in report:
        신고한, 신고당한 = report_detail.split() # 신고한사람, 신고당한사람
        report_info[신고당한].add(신고한)
    
    # report_info를 보고 유저별로 몇명이 신고했는지 k와 비교 (신고당한사람: set('frodo', 'neo'))
    for key in report_info:
        # 정지 당했으면 >= k, 신고한 유저들 메일 +1
        if len(report_info[key]) >= k:
            for user in report_info[key]:
                mail_info[user] += 1
            
    
    # mail_info를 가지고 id_list 순서대로 값을 가져온다.
    for user in id_list:
        answer.append(mail_info[user])
    
    # answer = [메일을 받는 횟수]
    return answer