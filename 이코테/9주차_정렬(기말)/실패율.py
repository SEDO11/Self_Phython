def solution(N, stages):
    answer = []
    stage = []
    for i in range(1, N+1):
        answer.append((i, stages.count(i) / len(stages)))
        try:
            for _ in stages:
                stages.remove(i)
        except:
            pass
    answer = sorted(answer, key=lambda stage:stage[1], reverse=True)
    
    for ans in answer:
        stage.append(ans[0])
    
    return stage