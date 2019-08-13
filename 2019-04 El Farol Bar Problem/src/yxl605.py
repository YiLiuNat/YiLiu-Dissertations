import random
import argparse
import math
# import sys,os
import numpy as np, numpy.random

def ex1(prob_str,repetitions):
    prob_split = prob_str.split(' ')
    prob = [float(i) for i in prob_split]
    length = len(prob)
    count = 0
    sample = []
    prob_sum = sum(prob)
    while(len(sample) < repetitions):
        index = count%length
        vector = prob[index]
        # print(count%length)
        # vector_prob = vector/prob_sum

        rand = random.uniform(0,1)
        if rand <= vector:
            print(index)
            sample.append(index)
        count += 1
    # while (count < repetitions):
    #     count2 = 0
    #     start = 0
    #     while(start < random.uniform(0,1)):
    #         start = start+prob[count2]
    #         index = count2
    #         count2 += 1
    #     print(index)
    #     count += 1


# ex1("0.1 0.2 0.5 0.2",100)

# def parse(strategy):
#     strategy_split = strategy.split(' ')
#     strategy_list = [float(i) for i in strategy_split]
#     return len(strategy_list)
#
# print(parse("0.812648185556 0.120843352454 0.0968210174089 0.27873187108 0.0111232197776 0.0485226897441 0.2369236801 0.0948023212397 0.0487814956782 0.0404946705079 0.0229556820093 0.0127819387805 0.00168340132378 0.0191862622733 0.115898333055 0.161757007421 0.155459735063 0.042012869176 0.14294093164 0.165366628989 0.182912892278 0.343759250622 0.0448009784613 0.139239371918 0.0791779768294 0.138316625061 0.157035462151 0.107492596337 0.0455924015866 0.135555547116 0.0959737708182 0.0568152697214 0.0281090938166 0.102111084102 0.0963023659209 0.0655402606505 0.153018561715 0.106533527703 0.170500822 0.0315378912556 0.156568070426 0.089778322411 0.178583237731 0.0146381496182 0.0917040580232 0.0677042036691 0.0187105925794 0.130200155936 0.146014950212 0.146402115256 0.0970855297112 0.142853732665 0.14468651233 0.0149678475302 0.0249143942062 0.133862255301 0.130590648681 0.127676873899 0.0419050289869 0.197394866745 0.100750829496 0.202787538608 0.0251497165466 0.919663074668 0.016541800918 0.168794590704 0.0209105701611 0.161129913507 0.172368309831 0.123629563563 0.121296796463 0.17777997791 0.017394995974 0.0201534809692 0.0647291574887 0.138026004376 0.0359076180042 0.0320806264965 0.0266359854431 0.150609159475 0.187766336283 0.18273432491 0.177594157755 0.00391662976874 0.372063525301 0.039159653304 0.0673599026337 0.186075551842 0.0257586429947 0.132507714874 0.018475857173 0.120705824965 0.111232701314 0.0972330967655 0.201491054133 0.00558437846879 0.00103832840213 0.113439829372 0.1656497077 0.112963467221 0.172851912043 0.172253491649 0.0711533844614 0.0234939109958 0.161571589687 0.283000855138 0.233315745542 0.0147719807286 0.0557416516621 0.10067209308 0.171215349138 0.142964600959 0.0380594554542 0.13411893635 0.10465428845 0.00448589863795 0.00436721548111 0.160119243337 0.0426321197697 0.124681057256 0.0528019428032 0.164743915853 0.030919410443 0.176491303256 0.169484335375 0.0737594564246 0.864500897359 0.19460783376 0.0610353356435 0.149878783896 0.025268616996 0.111758867595 0.118517847296 0.0478835314323 0.112777651263 0.161923200575 0.0163483315436 0.00721882601063 0.195265031182 0.0447824521207 0.112491240781 0.241743878321 0.0918795154863 0.00720258786058 0.192064677397 0.0104501023347 0.0969016885068 0.87479008994 0.0438442812 0.0988144697285 0.139509581405 0.194111699879 0.143348727782 0.00691180589053 0.190082101939 0.0775436456162 0.0164034170278 0.0894302695322 0.151655409891 0.0260294826396 0.0565291398337 0.0716512176955 0.110171538237 0.13685070542 0.144120135548 0.138122945279 0.0701718414614 0.0946975839951 0.117717074774 0.0342848108409 0.217387400721 0.0409549025486 0.192344524889 0.164946256173 0.000731197000461 0.091796481014 0.05638932385 0.192511865174 0.00865323778971 0.124964907305 0.0203492366718 0.102378793285 0.146128868615 0.104073174131 0.0885286883712 0.151335753149 0.0589861154045 0.121532335195 0.0817221278715 0.853987310419 0.128098335557 0.121582304773 0.0889771920958 0.0369511637774 0.133211409119 0.0551934884543 0.0877860799554 0.172086088675 0.0678096661033 0.108304271489 0.056171936514 0.210077369463 0.0256529332057 0.148999690836 0.130453222881 0.0874183891501 0.125020951734 0.0850910390019 0.0778378569134 0.0532766103023"))


def ex2(strategy,state,crowded,repetitions):
    strategy_split = strategy.split(' ')
    strategy_list = [float(i) for i in strategy_split]
    h = strategy_list[0]
    left = strategy_list[1:]
    left_len = len(left)
    sub_len = int(left_len / h)

    matrix = []
    count_m = 0
    while(count_m < h):
        start_point = count_m * sub_len
        end_point = start_point + sub_len
        sub_list = left[start_point:end_point]
        matrix.append(sub_list)
        count_m += 1

    subMat = matrix[state]
    stateMat = subMat[0]
    a = subMat[1:int(h+1)]
    b = subMat[int(h+1):]
    sample = []
    count = 0
    while(count < repetitions):
        if(crowded == 1):
            rand = random.uniform(0,1)
            countRand = 0
            start = 0
            while(start < rand):
                start = start+a[countRand]
                index = countRand
                countRand += 1
            rand2 = random.uniform(0,1)

            newRow = matrix[index]
            decision_p = newRow[0]
            decision = 0
            if(rand2 < decision_p):
            # if(rand2 < a[index]):
                decision = 1
            print("%s\t%s"%(decision,index))

        if(crowded == 0):
            rand = random.uniform(0,1)
            countRand = 0
            start = 0
            while(start < rand):
                start = start+b[countRand]
                index = countRand
                countRand += 1
            rand2 = random.uniform(0,1)

            newRow = matrix[index]
            decision_p = newRow[0]
            decision = 0
            if (rand2 < decision_p):
                decision = 1
            print("%s\t%s"%(decision,index))

        count += 1
        # return decision

def _ex2(strategy, state, crowded, repetitions):
    strategy_split = strategy.split(' ')
    strategy_list = [float(i) for i in strategy_split]
    h = strategy_list[0]
    left = strategy_list[1:]
    left_len = len(left)
    sub_len = int(left_len / h)

    matrix = []
    count_m = 0
    while (count_m < h):
        start_point = count_m * sub_len
        end_point = start_point + sub_len
        sub_list = left[start_point:end_point]
        matrix.append(sub_list)
        count_m += 1

    subMat = matrix[state]
    stateMat = subMat[0]
    a = subMat[1:int(h + 1)]
    b = subMat[int(h + 1):]
    sample = []
    count = 0
    while (count < repetitions):
        if (crowded == 1):
            rand = random.uniform(0, 1)
            countRand = 0
            start = 0
            while (start < rand):
                start = start + a[countRand]
                index = countRand
                countRand += 1
            rand2 = random.uniform(0, 1)

            newRow = matrix[index]
            decision_p = newRow[0]
            decision = 0
            if (rand2 < decision_p):
                # if(rand2 < a[index]):
                decision = 1

        if (crowded == 0):
            rand = random.uniform(0, 1)
            countRand = 0
            start = 0
            while (start < rand):
                start = start + b[countRand]
                index = countRand
                countRand += 1
            rand2 = random.uniform(0, 1)

            newRow = matrix[index]
            decision_p = newRow[0]
            decision = 0
            if (rand2 < decision_p):
                decision = 1

        count += 1
        return decision,index
    #     while(len(sample) < repetitions):
    #         index = count%len(a)
    #         vector = a[index]
    #         rand = random.uniform(0,1)
    #         if rand <= vector:
    #             decision_rand = random.uniform(0,1)
    #             decision = 0
    #             if(decision_rand <= vector):
    #                 decision = 1
    #             # print(decision,"\t",index)
    #             print(decision)
    #             sample.append(index)
    #         count += 1
    # if(crowded == 0):
    #     while (len(sample) < repetitions):
    #         index = count % len(b)
    #         vector = b[index]
    #         rand = random.uniform(0, 1)
    #         if rand <= vector:
    #             decision_rand = random.uniform(0,1)
    #             decision = 0
    #             if(decision_rand <= vector):
    #                 decision = 1
    #             # print(decision,'\t',index)
    #             print(decision)
    #             sample.append(index)
    #         count += 1

    # return matrix





# print(ex2("2 0.1 0.0 1.0 1.0 0.0 1.0 0.9 0.1 0.9 0.1",1,1,5))
# print(ex2("10 0.812648185556 0.120843352454 0.0968210174089 0.27873187108 0.0111232197776 0.0485226897441 0.2369236801 0.0948023212397 0.0487814956782 0.0404946705079 0.0229556820093 0.0127819387805 0.00168340132378 0.0191862622733 0.115898333055 0.161757007421 0.155459735063 0.042012869176 0.14294093164 0.165366628989 0.182912892278 0.343759250622 0.0448009784613 0.139239371918 0.0791779768294 0.138316625061 0.157035462151 0.107492596337 0.0455924015866 0.135555547116 0.0959737708182 0.0568152697214 0.0281090938166 0.102111084102 0.0963023659209 0.0655402606505 0.153018561715 0.106533527703 0.170500822 0.0315378912556 0.156568070426 0.089778322411 0.178583237731 0.0146381496182 0.0917040580232 0.0677042036691 0.0187105925794 0.130200155936 0.146014950212 0.146402115256 0.0970855297112 0.142853732665 0.14468651233 0.0149678475302 0.0249143942062 0.133862255301 0.130590648681 0.127676873899 0.0419050289869 0.197394866745 0.100750829496 0.202787538608 0.0251497165466 0.919663074668 0.016541800918 0.168794590704 0.0209105701611 0.161129913507 0.172368309831 0.123629563563 0.121296796463 0.17777997791 0.017394995974 0.0201534809692 0.0647291574887 0.138026004376 0.0359076180042 0.0320806264965 0.0266359854431 0.150609159475 0.187766336283 0.18273432491 0.177594157755 0.00391662976874 0.372063525301 0.039159653304 0.0673599026337 0.186075551842 0.0257586429947 0.132507714874 0.018475857173 0.120705824965 0.111232701314 0.0972330967655 0.201491054133 0.00558437846879 0.00103832840213 0.113439829372 0.1656497077 0.112963467221 0.172851912043 0.172253491649 0.0711533844614 0.0234939109958 0.161571589687 0.283000855138 0.233315745542 0.0147719807286 0.0557416516621 0.10067209308 0.171215349138 0.142964600959 0.0380594554542 0.13411893635 0.10465428845 0.00448589863795 0.00436721548111 0.160119243337 0.0426321197697 0.124681057256 0.0528019428032 0.164743915853 0.030919410443 0.176491303256 0.169484335375 0.0737594564246 0.864500897359 0.19460783376 0.0610353356435 0.149878783896 0.025268616996 0.111758867595 0.118517847296 0.0478835314323 0.112777651263 0.161923200575 0.0163483315436 0.00721882601063 0.195265031182 0.0447824521207 0.112491240781 0.241743878321 0.0918795154863 0.00720258786058 0.192064677397 0.0104501023347 0.0969016885068 0.87479008994 0.0438442812 0.0988144697285 0.139509581405 0.194111699879 0.143348727782 0.00691180589053 0.190082101939 0.0775436456162 0.0164034170278 0.0894302695322 0.151655409891 0.0260294826396 0.0565291398337 0.0716512176955 0.110171538237 0.13685070542 0.144120135548 0.138122945279 0.0701718414614 0.0946975839951 0.117717074774 0.0342848108409 0.217387400721 0.0409549025486 0.192344524889 0.164946256173 0.000731197000461 0.091796481014 0.05638932385 0.192511865174 0.00865323778971 0.124964907305 0.0203492366718 0.102378793285 0.146128868615 0.104073174131 0.0885286883712 0.151335753149 0.0589861154045 0.121532335195 0.0817221278715 0.853987310419 0.128098335557 0.121582304773 0.0889771920958 0.0369511637774 0.133211409119 0.0551934884543 0.0877860799554 0.172086088675 0.0678096661033 0.108304271489 0.056171936514 0.210077369463 0.0256529332057 0.148999690836 0.130453222881 0.0874183891501 0.125020951734 0.0850910390019 0.0778378569134 0.0532766103023",1,0,1000))
# print(ex2("10 0.812648185556 0.120843352454 0.0968210174089 0.27873187108 0.0111232197776 0.0485226897441 0.2369236801 0.0948023212397 0.0487814956782 0.0404946705079 0.0229556820093 0.0127819387805 0.00168340132378 0.0191862622733 0.115898333055 0.161757007421 0.155459735063 0.042012869176 0.14294093164 0.165366628989 0.182912892278 0.343759250622 0.0448009784613 0.139239371918 0.0791779768294 0.138316625061 0.157035462151 0.107492596337 0.0455924015866 0.135555547116 0.0959737708182 0.0568152697214 0.0281090938166 0.102111084102 0.0963023659209 0.0655402606505 0.153018561715 0.106533527703 0.170500822 0.0315378912556 0.156568070426 0.089778322411 0.178583237731 0.0146381496182 0.0917040580232 0.0677042036691 0.0187105925794 0.130200155936 0.146014950212 0.146402115256 0.0970855297112 0.142853732665 0.14468651233 0.0149678475302 0.0249143942062 0.133862255301 0.130590648681 0.127676873899 0.0419050289869 0.197394866745 0.100750829496 0.202787538608 0.0251497165466 0.919663074668 0.016541800918 0.168794590704 0.0209105701611 0.161129913507 0.172368309831 0.123629563563 0.121296796463 0.17777997791 0.017394995974 0.0201534809692 0.0647291574887 0.138026004376 0.0359076180042 0.0320806264965 0.0266359854431 0.150609159475 0.187766336283 0.18273432491 0.177594157755 0.00391662976874 0.372063525301 0.039159653304 0.0673599026337 0.186075551842 0.0257586429947 0.132507714874 0.018475857173 0.120705824965 0.111232701314 0.0972330967655 0.201491054133 0.00558437846879 0.00103832840213 0.113439829372 0.1656497077 0.112963467221 0.172851912043 0.172253491649 0.0711533844614 0.0234939109958 0.161571589687 0.283000855138 0.233315745542 0.0147719807286 0.0557416516621 0.10067209308 0.171215349138 0.142964600959 0.0380594554542 0.13411893635 0.10465428845 0.00448589863795 0.00436721548111 0.160119243337 0.0426321197697 0.124681057256 0.0528019428032 0.164743915853 0.030919410443 0.176491303256 0.169484335375 0.0737594564246 0.864500897359 0.19460783376 0.0610353356435 0.149878783896 0.025268616996 0.111758867595 0.118517847296 0.0478835314323 0.112777651263 0.161923200575 0.0163483315436 0.00721882601063 0.195265031182 0.0447824521207 0.112491240781 0.241743878321 0.0918795154863 0.00720258786058 0.192064677397 0.0104501023347 0.0969016885068 0.87479008994 0.0438442812 0.0988144697285 0.139509581405 0.194111699879 0.143348727782 0.00691180589053 0.190082101939 0.0775436456162 0.0164034170278 0.0894302695322 0.151655409891 0.0260294826396 0.0565291398337 0.0716512176955 0.110171538237 0.13685070542 0.144120135548 0.138122945279 0.0701718414614 0.0946975839951 0.117717074774 0.0342848108409 0.217387400721 0.0409549025486 0.192344524889 0.164946256173 0.000731197000461 0.091796481014 0.05638932385 0.192511865174 0.00865323778971 0.124964907305 0.0203492366718 0.102378793285 0.146128868615 0.104073174131 0.0885286883712 0.151335753149 0.0589861154045 0.121532335195 0.0817221278715 0.853987310419 0.128098335557 0.121582304773 0.0889771920958 0.0369511637774 0.133211409119 0.0551934884543 0.0877860799554 0.172086088675 0.0678096661033 0.108304271489 0.056171936514 0.210077369463 0.0256529332057 0.148999690836 0.130453222881 0.0874183891501 0.125020951734 0.0850910390019 0.0778378569134 0.0532766103023",1,0,1000))


def initPop(popSize,h):
    count_p = 0
    popMatrix = []
    while(count_p < popSize):
        count_h = 0
        individualWithoutH = []
        individual = []
        while(count_h < h):
            a = np.random.dirichlet(np.ones(h),size=1)
            a = a.tolist()
            b = np.random.dirichlet(np.ones(h),size=1)
            b = b.tolist()

            state_value = [random.uniform(0,1)]
            _state = state_value+a+b

            # state = eval('[%s]'%repr(_state).replace('[','').replace(']',''))
            # state_str = " ".join([str(i) for i in state])
            individualWithoutH.append(_state) # indivi with multi-states

            count_h += 1
        individual.append(h)
        individual.append(individualWithoutH)
        individualWithoutBra = eval('[%s]'%repr(individual).replace('[','').replace(']',''))#delete bracket
        indivi_str = " ".join([str(i) for i in individualWithoutBra])

        popMatrix.append(indivi_str)
        # print(popMatrix)
        count_p += 1
    return popMatrix

# print(initPop(2,2))

def mutation(individual,rate):
    h_split = individual.split(' ')
    ind = [float(i) for i in h_split]
    h = int(ind[0])
    mutationNum = math.ceil(rate*h*2)
    count = 0
    ind = individual
    while(count < mutationNum):
        ind_split = ind.split(' ')
        ind = [float(i) for i in ind_split]
        h = int(ind[0])
        withoutH = ind[1:]
        eachLength = h*2+1

        rand_h = random.randint(0,h-1) #select which part to mutate
        startOfPart = rand_h*eachLength
        endOfPart = startOfPart + eachLength
        mutatePart = withoutH[startOfPart:endOfPart]

        randAB = random.uniform(0,1)
        if randAB <= 0.5:
            mutatePart[1:h + 1] = np.random.dirichlet(np.ones(h),size=1).tolist() #a = mutatePart[1:h+1]
        else:
            mutatePart[h + 1:] = np.random.dirichlet(np.ones(h),size=1).tolist() #b = mutatePart[h+1:]

        mutatePart[0] = random.uniform(0, 1)
        withoutH[startOfPart:endOfPart] = mutatePart
        ind[1:] = withoutH
        ind_bra = eval('[%s]'%repr(ind).replace('[','').replace(']',''))
        ind_str = " ".join([str(i) for i in ind_bra])
        ind = ind_str
        count += 1
    return ind_str

# print(mutation(initPop(2,2)[0],10))
# print(mutation("2 0.1 0.0 1.0 1.0 0.0 1.0 0.9 0.1 0.9 0.1",0.1))
# print(mutation("3 0.30593444298031935 0.7380166146213242 0.04866988365533367 0.2133135017233423 0.9388630177526694 0.03504653859387766 0.02609044365345269 0.8463976820990444 0.30955326568892205 0.5008052176766762 0.18964151663440174 0.33852722727481377 0.48151857533871145 0.17995419738647472 0.09797159958675172 0.1584350094262061 0.8390482906925539 0.002516699881240066 0.6866164405576679 0.06789095857919344 0.24549260086313857",0.1))
# print(initPop(1,3))

def crossover(ind1,ind2):
    h1_split = ind1.split(' ')
    ind1 = [float(i) for i in h1_split]
    h2_split = ind2.split(' ')
    ind2 = [float(i) for i in h2_split]
    h = int(ind1[0])

    eachLength = h*2+1
    rand_cross1 = random.randint(0,h-1)
    startPoint1 = rand_cross1*eachLength
    endPoint1 = startPoint1+eachLength

    rand_cross2 = random.randint(0, h - 1)
    startPoint2 = rand_cross2 * eachLength
    endPoint2 = startPoint2 + eachLength

    ind1[1+startPoint1:1+endPoint1] = ind2[1+startPoint2:1+endPoint2]
    ind_str = " ".join([str(i) for i in ind1])

    return ind_str

def countRepeat(element,list):
    count = 0
    repeat = 0
    while(count < len(list)):
        if(list[count] == element):
            repeat += 1
        count += 1
    return repeat

def payHome(decision_list,payoff_list):
    count = 0
    while(count < len(decision_list)):
        if decision_list[count] == 0:
            payoff_list[count] += 1
        count += 1
    return payoff_list

def payBar(decision_list,payoff_list):
    count = 0
    while(count < len(decision_list)):
        if decision_list[count] == 1:
            payoff_list[count] += 1
        count += 1
    return payoff_list

def ranking(population,payoff):
    for j in range(len(payoff)):
        for i in range(0,len(payoff)-1):
            if payoff[i] < payoff[i+1]:
                # swap payoff
                temp1 = payoff[i]
                payoff[i] = payoff[i+1]
                payoff[i+1] = temp1

                # swap population
                temp2 = population[i]
                population[i] = population[i+1]
                population[i+1] = temp2
    return population

def ex3(popSize,h,weeks,max_t):
    crowdedRate = 0.6
    mutationRate = 0.2
    population = initPop(popSize,h)
    generationCount = 0
    while(generationCount < max_t):
        crowded = 0
        popCount = 0
        state = 0
        decision_list = []
        state_list = []
        avg_list = []
        # Initial Week
        while(popCount < popSize):
            # disablePrint()
            # print(popCount)
            decision,new_state = _ex2(population[popCount],state,crowded,1)
            decision_list.append(decision)
            state_list.append(new_state)
            popCount+=1

        # Week Loop
        payoff_list = [0 for i in range(popSize)]
        weekCount = 0
        while(weekCount < weeks):

            new_decision_list = []
            new_state_list = []
            popCount = 0
            while(popCount < popSize):
                decision,new_state = _ex2(population[popCount],state_list[popCount],crowded,1)
                new_decision_list.append(decision)
                new_state_list.append(new_state)
                popCount += 1
            decision_list = new_decision_list
            state_list = new_state_list

            # is it crowded?
            peopleGoBar = countRepeat(1,decision_list)
            if (peopleGoBar > crowdedRate*len(decision_list)):
                crowded = 1
                # Pay bonus for people stayed home
                new_payoff_list = payHome(decision_list,payoff_list)
                payoff_list = new_payoff_list
            else:
                crowded = 0
                # Pay bonus for people went bar
                new_payoff_list = payBar(decision_list,payoff_list)
                payoff_list = new_payoff_list

            printDecisionList = " ".join([str(i) for i in decision_list])
            print("%s\t%s\t%s\t%s\t%s"%(weekCount,generationCount,crowded,peopleGoBar,printDecisionList))
            # print((weekCount + 1)+'\t'+ (generationCount + 1) +'\t'+ crowded+'\t'+ peopleGoBar+'\t'+ decision_list)
            avg_list.append(peopleGoBar)
            weekCount += 1
        rankPopSet = ranking(population,payoff_list)
        cutNum = int((1-crowdedRate)*popSize)
        cutPopSet = rankPopSet[0:popSize-cutNum]

        addOffspring = 0
        while(addOffspring < cutNum):
            parent1 = population[random.randint(0,(popSize-cutNum))]
            parent2 = population[random.randint(0,(popSize-cutNum))]
            while(parent1 == parent2):
                parent2 = population[random.randint(0,(popSize-cutNum))]
            crossovered = crossover(parent1,parent2)
            mutated = mutation(crossovered,mutationRate)
            cutPopSet.append(mutated)
            addOffspring += 1
         # =
        # print(len(cutPopSet),cutNum)
        population = cutPopSet
        generationCount += 1
    # return sum(avg_list)/(weeks+1)

# print(ex3(100,5,10,100))
# def avgCal(i):
#     count = 0
#     avg_list = []
#     while(count < i):
#         avg = ex3(100,5,30,100)
#         avg_list.append(avg)
#         print(avg_list)
#         count += 1
#     list_i = 0
#     while(list_i < len(avg_list)):
#         print(avg_list[list_i])
#         list_i += 1
#     # return avg_list
# print(avgCal(20))





# print(payHome([1,0,0,1],[1,1,1,1]))
# def disablePrint():
#     sys.stdout = open(os.devnull,'w')
#
# def enablePrint():
#     sys.stdout = sys.__stdout__

# Docker
# if __name__ == '__main__':
docker = argparse.ArgumentParser(description='start', add_help=False)

docker.add_argument("-question", help="question num", type=int)
docker.add_argument("-prob", help="probability", type=str)
docker.add_argument("-repetitions", help="", type=int)
docker.add_argument("-strategy",help="strategy",type=str)
docker.add_argument("-crowded",help="crowded",type=int)
docker.add_argument("-state",help="state",type=int)
docker.add_argument("-lambdapush",help="pop size",type=int)
docker.add_argument("-hpush",help="num of stg",type=int)
docker.add_argument("-weeks",help="num of week per gen",type=int)
docker.add_argument("-max_t",help="num of gen",type=int)

parsed = docker.parse_args()

if parsed.question == 1:
    ex1(parsed.prob,parsed.repetitions)
    # print(get_result_1)
if parsed.question == 2:
    ex2(parsed.strategy,parsed.state,parsed.crowded,parsed.repetitions)
if parsed.question == 3:
    ex3(parsed.lambdapush,parsed.hpush,parsed.weeks,parsed.max_t)
