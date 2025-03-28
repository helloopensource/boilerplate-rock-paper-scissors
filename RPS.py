# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

num_predictor = 27
len_rfind = [20]
limit = [10, 20, 60]
beat = {"R": "P", "P": "S", "S": "R"}
not_lose = {"R": "PPR", "P": "SSP", "S": "RRS"}  # 50-50 chance
my_his = ""
your_his = ""
both_his = ""
list_predictor = [""]*num_predictor
length = 0
temp1 = {"PP": "1", "PR": "2", "PS": "3",
         "RP": "4", "RR": "5", "RS": "6",
         "SP": "7", "SR": "8", "SS": "9"}
temp2 = {"1": "PP", "2": "PR", "3": "PS",
         "4": "RP", "5": "RR", "6": "RS",
         "7": "SP", "8": "SR", "9": "SS"}
who_win = {"PP": 0, "PR": 1, "PS": -1,
           "RP": -1, "RR": 0, "RS": 1,
           "SP": 1, "SR": -1, "SS": 0}
output = random.choice("RPS")
predictors = [""]*num_predictor
score_predictor = [0]*num_predictor


def player(prev_play, opponent_history=[]):
    global len_rfind, limit, beat, not_lose, my_his, your_his, both_his, list_predictor, length, temp1, temp2, who_win, output
    input = prev_play
    opponent_history.append(input)
    if input is None or input == "":
        return random.choice("RPS")
    else:
        # update predictors
        # """
        if len(list_predictor[0]) < 5:
            front = 0
        else:
            front = 1
        for i in range(num_predictor):
            if predictors[i] == input:
                result = "1"
            else:
                result = "0"
            list_predictor[i] = list_predictor[i][front:5] + \
                result  # only 5 rounds before
        # history matching 1-6
        my_his += output
        your_his += input
        both_his += temp1[input+output]
        length += 1
        for i in range(1):
            len_size = min(length, len_rfind[i])
            j = len_size
            # both_his
            while j >= 1 and not both_his[length-j:length] in both_his[0:length-1]:
                j -= 1
            if j >= 1:
                k = both_his.rfind(both_his[length-j:length], 0, length-1)
                predictors[0+6*i] = your_his[j+k]
                predictors[1+6*i] = beat[my_his[j+k]]
            else:
                predictors[0+6*i] = random.choice("RPS")
                predictors[1+6*i] = random.choice("RPS")
            j = len_size
            # your_his
            while j >= 1 and not your_his[length-j:length] in your_his[0:length-1]:
                j -= 1
            if j >= 1:
                k = your_his.rfind(your_his[length-j:length], 0, length-1)
                predictors[2+6*i] = your_his[j+k]
                predictors[3+6*i] = beat[my_his[j+k]]
            else:
                predictors[2+6*i] = random.choice("RPS")
                predictors[3+6*i] = random.choice("RPS")
            j = len_size
            # my_his
            while j >= 1 and not my_his[length-j:length] in my_his[0:length-1]:
                j -= 1
            if j >= 1:
                k = my_his.rfind(my_his[length-j:length], 0, length-1)
                predictors[4+6*i] = your_his[j+k]
                predictors[5+6*i] = beat[my_his[j+k]]
            else:
                predictors[4+6*i] = random.choice("RPS")
                predictors[5+6*i] = random.choice("RPS")

        for i in range(3):
            temp = ""
            search = temp1[(output+input)]  # last round
            for start in range(2, min(limit[i], length)):
                if search == both_his[length-start]:
                    temp += both_his[length-start+1]
            if (temp == ""):
                predictors[6+i] = random.choice("RPS")
            else:
                # take win/lose from opponent into account
                collectR = {"P": 0, "R": 0, "S": 0}
                for sdf in temp:
                    next_move = temp2[sdf]
                    if (who_win[next_move] == -1):
                        collectR[temp2[sdf][1]] += 3
                    elif (who_win[next_move] == 0):
                        collectR[temp2[sdf][1]] += 1
                    elif (who_win[next_move] == 1):
                        collectR[beat[temp2[sdf][0]]] += 1
                max1 = -1
                p1 = ""
                for key in collectR:
                    if (collectR[key] > max1):
                        max1 = collectR[key]
                        p1 += key
                predictors[6+i] = random.choice(p1)

        # rotate 9-27:
        for i in range(9, 27):
            predictors[i] = beat[beat[predictors[i-9]]]

        # choose a predictor
        len_his = len(list_predictor[0])
        for i in range(num_predictor):
            sum = 0
            for j in range(len_his):
                if list_predictor[i][j] == "1":
                    sum += (j+1)*(j+1)
                else:
                    sum -= (j+1)*(j+1)
            score_predictor[i] = sum
        max_score = max(score_predictor)
        # min_score = min(score_predictor)
        # c_temp = {"R":0,"P":0,"S":0}
        # for i in range (num_predictor):
        # if score_predictor[i]==max_score:
        #    c_temp[predictors[i]] +=1
        # if score_predictor[i]==min_score:
        #    c_temp[predictors[i]] -=1
        if max_score > 0:
            predict = predictors[score_predictor.index(max_score)]
        else:
            predict = random.choice(your_his)
        output = random.choice(not_lose[predict])
    return output
