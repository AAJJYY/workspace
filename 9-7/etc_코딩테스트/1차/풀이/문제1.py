def solution(lottos, win_nums):
    answer = []
    
    # lottos : 민우가 선택한 번호들
    # win_nums : 당첨 번호
    
    # 내가 생각한 알고리즘 ???
    # 로또번호를 하나하나씩 당첨 번호와 비교한다.
    # 비교할 때 로또번호가 0이면, 별도로 처리한다.
    # 몇 개 맞췄는지 알고있어야 한다 (변수로 저장한다.)
    win_count = 0
    # 로또번호가 지워진 경우도 몇 개인지 알고 있어야한다. (변수로 저장한다.)
    sub_count = 0
    
    for lotto in lottos:
        if lotto == 0:
            sub_count += 1
        else:
            if lotto in win_nums:
                win_count += 1
            # for win_num in win_nums:
            #     if lotto == win_num:
            #         win_count += 1

    # 맞춘 갯수와 지워진 갯수를 가지고 최대, 최소 몇 개 맞출수 있는지 확인한다.
    best_count = win_count + sub_count
    worst_count = win_count
    # 최대 맞춘 갯수와, 최소 맞춘 갯수로 순위를 확인한다.
    best_rank = min(7 - best_count, 6)
    worst_rank = min(7 - worst_count, 6)
    # if best_count == 6:
    #     best_rank = 1
    # elif best_count == 5:
    #     best_rank = 2
    # elif best_count == 4:
    #     best_rank = 3
    # elif best_count == 3:
    #     best_rank = 4
    # elif best_count == 2:
    #     best_rank = 5
    # else:
    #     best_rank = 6
        
    # if worst_count == 6:
    #     worst_rank = 1
    # elif worst_count == 5:
    #     worst_rank = 2
    # elif worst_count == 4:
    #     worst_rank = 3
    # elif worst_count == 3:
    #     worst_rank = 4
    # elif worst_count == 2:
    #     worst_rank = 5
    # else:
    #     worst_rank = 6
    
    # answer = [최고 순위, 최저 순위]
    answer = [best_rank, worst_rank]
    return answer