from sexpdata import *
import numpy
import csv
import math
import argparse
import random
import time
import copy

# Exercise 1
def add(a,b):
    if isNum(a) and isNum(b):
        return a + b
    if not isNum(a) and isNum(b):
        return add(parse(a),b)
    if isNum(a) and not isNum(b):
        return add(a,parse(b))
    if not isNum(a) and not isNum(b):
        return add(parse(a),parse(b))

def sub(a,b):
    if isNum(a) and isNum(b):
        return a - b
    if not isNum(a) and isNum(b):
        return sub(parse(a),b)
    if isNum(a) and not isNum(b):
        return sub(a,parse(b))
    if not isNum(a) and not isNum(b):
        return sub(parse(a),parse(b))

def mul(a,b):
    if isNum(a) and isNum(b):
        return a * b
    if not isNum(a) and isNum(b):
        return mul(parse(a),b)
    if isNum(a) and not isNum(b):
        return mul(a,parse(b))
    if not isNum(a) and not isNum(b):
        return mul(parse(a),parse(b))

def div(a,b):
    if isNum(a) and isNum(b):
        try: return a/b
        except: return 0
    if not isNum(a) and isNum(b):
        return div(parse(a),b)
    if isNum(a) and not isNum(b):
        return div(a,parse(b))
    if not isNum(a) and not isNum(b):
        return div(parse(a),parse(b))

def _pow(a,b):
    if isNum(a) and isNum(b):
        try:
            result = math.pow(a, b)
            if isinstance(result, complex):
                result = 0
            return result
        except:
            return 0
    if not isNum(a) and isNum(b):
        return _pow(parse(a),b)
    if isNum(a) and not isNum(b):
        return _pow(a,parse(b))
    if not isNum(a) and not isNum(b):
        return _pow(parse(a),parse(b))

def _sqrt(a):
    if isNum(a):
        try:
            result = math.sqrt(a)
            if isinstance(result, complex):
                result = 0
            return result
        except: return 0
    if not isNum(a):
        return _sqrt(parse(a))

def log(a):
    if isNum(a):
        try:
            return math.log(a,2)
        except: return 0
    if not isNum(a):
        try: return log(parse(a))
        except: return 0

def exp(a):
    if isNum(a):
        try:
            return math.exp(a)
        except: return 0
    if not isNum(a):
        return exp(parse(a))

def _max(a,b):
    if isNum(a) and isNum(b):
        try: result = math.max(a,b)
        except: return 0
        return result
    if not isNum(a) and isNum(b):
        return _max(parse(a),b)
    if isNum(a) and not isNum(b):
        return _max(a,parse(b))
    if not isNum(a) and not isNum(b):
        return _max(parse(a),parse(b))

def ifleq(a,b,c,d):
    if isNum(a) and isNum(b):
        if a <= b:
            return c
        else: return d
    if not isNum(a) and isNum(b):
        return ifleq(parse(a),b,c,d)
    if isNum(a) and not isNum(b):
        return ifleq(a,parse(b),c,d)
    if not isNum(a) and not isNum(b):
        return ifleq(parse(a),parse(b),c,d)

_n = 0
set = []
def data(a):
    if isNum(a):
        rem = int(mod(a,_n))
        return set[rem]
    else:
        return data(parse(a))

def mod(a,b):
    return divmod(a,b)[1]

def diff(a,b):
    if isNum(a) and isNum(b):
        return sub(data(a),data(b))
    if not isNum(a) and isNum(b):
        return diff(parse(a),b)
    if isNum(a) and not isNum(b):
        return diff(a,parse(b))
    if not isNum(a) and not isNum(b):
        return diff(parse(a),parse(b))

def avg(a,b):
    if isNum(a) and isNum(b):
        k = int(divmod(a,_n)[1])
        l = int(divmod(b,_n)[1])
        _abs = abs(k-l)
        _min = min(k,l)
        _max = max(k,l)
        if _min == _max:
            return 0
        else:
            try: return sum(set[_min: _max])/_abs
            except: return 0
    if not isNum(a) and isNum(b):
        return avg(parse(a),b)
    if isNum(a) and not isNum(b):
        return avg(a,parse(b))
    if not isNum(a) and not isNum(b):
        return avg(parse(a),parse(b))



def parse(content):
    if isNum(content):
        return content
    if content[0] == Symbol('add'):
        try:return parse(content[1])+parse(content[2])
        except:return 0
    if content[0] == Symbol('sub'):
        try: return parse(content[1])-parse(content[2])
        except: return 0
    if content[0] == Symbol('mul'):
        try: return parse(content[1]) * parse(content[2])
        except: return 0
    if content[0] == Symbol('div'):
        if parse(content[2]) == 0: return 0
        else:
            try: return parse(content[1])/parse(content[2])
            except: return 0
    if content[0] == Symbol('pow'):
        if parse(content[1]) and parse(content[2]) == 0: return 1 # and / or
        else:
            try:
                if isinstance(math.pow(parse(content[1]),parse(content[2])),complex):
                    return 0
                else: return math.pow(parse(content[1]),parse(content[2]))
            except: return 0
    if content[0] == Symbol('sqrt'):
        try:
            result = math.sqrt(parse(content[1]))
            if isinstance(result,complex): return 0
            else: return result
        except: return 0
    if content[0] == Symbol('log'):
        try: return math.log(parse(content[1]),2)
        except: return 0
    if content[0] == Symbol('exp'):
        try:
            return math.exp(parse(content[1]))
        except: return 0
    if content[0] == Symbol('max'):
        return max(parse(content[1]),parse(content[2]))
    if content[0] == Symbol('ifleq'):
        if parse(content[1]) <= parse(content[2]):
            return parse(content[3])
        else: return parse(content[4])
    if content[0] == Symbol('data'):
        return set[int(abs(math.floor(parse(content[1])))%_n)]
    if content[0] == Symbol('diff'):
        try:
            return set[int(abs(math.floor(parse(content[1])))%_n)] - set[int(abs(math.floor(parse(content[2])))%_n)]
        except: return 0
    if content[0] == Symbol('avg'):
        k = int(abs(math.floor(parse(content[1]))) % _n)
        l = int(abs(math.floor(parse(content[2]))) % _n)#
        if k == l: return 0
        else:
            try: return sum(set[min(k,l):max(k,l)])/math.fabs(k-l)
            except: return 0





def isNum(a):
    if isinstance(a,float) or isinstance(a,int):
        return True
    else: return False

def niso_lab3(question,dimension,input_vector,expression):
    global set
    global _n
    if question == 1:
        traverse_vector = [float(i) for i in input_vector.split()]
        # if dimension != len(traverse_vector):
        #     return 0

        set = traverse_vector
        # print(set)
        _n = dimension
        return parse_loads(expression)

def parse_loads(a):
    return parse(loads(a))


# Exercise 2
def fopen(directory,vector_dimention):
    f_hor = open(directory, 'r')
    f_vir = open(directory, 'r')
    try:
        hor = [i[0:vector_dimention] for i in csv.reader(f_hor, delimiter='\t')]
        vir = [i[vector_dimention] for i in csv.reader(f_vir, delimiter='\t')]
        f_hor.close()
        f_vir.close()
        return hor,vir
    except IOError as err:
        return 0,0
        # print('Error: ', err)


def fitness(expression,n_dimention,m_dataSize,data_directory):

    hor,vir = fopen(data_directory,n_dimention)
    _sum = []
    for i in range(0,m_dataSize):
        _x = ' '.join(hor[i])
        _x_new = [float(j) for j in _x.split()]

        global set
        global _n
        set = _x_new
        _n = n_dimention
        parsed_exp = parse_loads(expression)

        try:
            _square = math.pow(float(vir[i])-float(parsed_exp),2)
            _sum = _sum + [_square]
        except OverflowError as err:
            _square = numpy.inf
            _sum = _sum + [_square]
            # print("Error: ",err)
    try:
        return sum(_sum)/len(_sum)
    except:
        return numpy.inf


# Exercise 3
def init(max_depth):
    if random.uniform(0,1)<0.1 or max_depth==0:
        return random.randint(0,10)
    else:
        symbol = random.choice(['add','sub','mul','div','pow','sqrt','log','exp','max','ifleq','data','diff','avg'])
        doubleCallBack = init(max_depth-1),init(max_depth-1)
        singleCallBack = init(max_depth-1)
        if symbol == 'add': return [Symbol('add'),singleCallBack,singleCallBack]
        if symbol == 'sub': return [Symbol('sub'),singleCallBack,singleCallBack]
        if symbol == 'mul': return [Symbol('mul'),singleCallBack,singleCallBack]
        if symbol == 'div': return [Symbol('div'),singleCallBack,singleCallBack]
        if symbol == 'pow': return [Symbol('div'),singleCallBack,singleCallBack]
        if symbol == 'sqrt': return [Symbol('sqrt'),singleCallBack]
        if symbol == 'log': return [Symbol('log'),singleCallBack]
        if symbol == 'exp': return [Symbol('exp'),singleCallBack]
        if symbol == 'max': return [Symbol('max'),singleCallBack,singleCallBack]
        if symbol == 'ifleq': return [Symbol('ifleq'),singleCallBack,singleCallBack,singleCallBack,singleCallBack]
        if symbol == 'data': return [Symbol('data'),singleCallBack]
        if symbol == 'diff': return [Symbol('diff'),singleCallBack,singleCallBack]
        if symbol == 'avg': return [Symbol('avg'),singleCallBack,singleCallBack]

def population(size,max_depth,n_dimention,m_dataSize,data_directory):
    popSet = []
    fitSet = []
    for i in range(0,size):
        indivi = init(max_depth)
        # print(dumps(indivi))
        # print(indivi)
        fitness_indivi = fitness(dumps(indivi),n_dimention,m_dataSize,data_directory)
        # avoid repetition
        # while (fitness_indivi in fitSet) or (not isinstance(indivi,list)):
        #     indivi = init(max_depth)
        #     fitness_indivi = fitness(dumps(indivi), n_dimention, m_dataSize, data_directory)
        popSet = popSet + [indivi]
        fitSet = fitSet + [fitness_indivi]

    return popSet,fitSet

# def get_dir(expr):
#     if not isinstance(expr, list):
#         return [[]]
#     if len(expr) == 2:
#         p = []
#         for i in get_dir(expr[1]):
#             p.append([1]+i)
#         return [[]] + p # [[]]+[[1]+i for i in get_branch(expr[1])]
#     if len(expr) == 3:
#         p1 = []
#         for i in get_dir(expr[1]):
#             p1.append([1]+i)
#         p2 = []
#         for i in get_dir(expr[2]):
#             p2.append([2]+i)
#         return [[]] + p1 + p2
#     if len(expr) == 5:
#         p1 = []
#         for i in get_dir(expr[1]):
#             p1.append([1]+i)
#         p2 = []
#         for i in get_dir(expr[2]):
#             p2.append([2]+i)
#         p3 = []
#         for i in get_dir(expr[3]):
#             p3.append([3]+i)
#         p4 = []
#         for i in get_dir(expr[4]):
#             p4.append([4]+i)
#         return [[]] + p1 + p2 + p3 + p4

def get_dir(expr):
    if not isinstance(expr, list):
        return [[]]
    if len(expr) == 2:
        p = []
        for i in get_dir(expr[1]):
            p.append([1]+i)
        return [[]] + p
    if len(expr) == 3:
        p1 = []
        for i in get_dir(expr[1]):
            p1.append([1]+i)
        p2 = []
        for i in get_dir(expr[2]):
            p2.append([2]+i)
        return [[]] + p1 + p2
    if len(expr) == 5:
        p1 = []
        for i in get_dir(expr[1]):
            p1.append([1]+i)
        p2 = []
        for i in get_dir(expr[2]):
            p2.append([2]+i)
        p3 = []
        for i in get_dir(expr[3]):
            p3.append([3]+i)
        p4 = []
        for i in get_dir(expr[4]):
            p4.append([4]+i)
        return [[]] + p1 + p2 + p3 + p4

def get_branch(dir,expr):
    if dir != []:
        return get_branch(dir[1:],expr[dir[0]])
    else:
        return expr

test_tree1 =[[Symbol('ifleq'), 5, 5, 5, 5], [Symbol('div'), [Symbol('ifleq'), [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]], [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]], [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]], [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]]], [Symbol('ifleq'), [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]], [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]], [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]], [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]]]], [Symbol('mul'), 2, 2], [Symbol('avg'), 2, 2], [Symbol('add'), [Symbol('data'), [Symbol('data'), [Symbol('add'), [Symbol('max'), 2, 2], [Symbol('max'), 2, 2]]]], [Symbol('data'), [Symbol('data'), [Symbol('add'), [Symbol('max'), 2, 2], [Symbol('max'), 2, 2]]]]]]
test_tree2 =[Symbol('mul'), [Symbol('sqrt'), [Symbol('ifleq'), [Symbol('diff'), 3, 3], [Symbol('diff'), 3, 3], [Symbol('diff'), 3, 3], [Symbol('diff'), 3, 3]]], [Symbol('sqrt'), [Symbol('ifleq'), [Symbol('diff'), 3, 3], [Symbol('diff'), 3, 3], [Symbol('diff'), 3, 3], [Symbol('diff'), 3, 3]]]]
# print(get_dir([[Symbol('ifleq'), 5, 5, 5, 5], [Symbol('div'), [Symbol('ifleq'), [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]], [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]], [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]], [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]]], [Symbol('ifleq'), [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]], [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]], [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]], [Symbol('max'), [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]], [Symbol('div'), [Symbol('sqrt'), 2], [Symbol('sqrt'), 2]]]]], [Symbol('mul'), 2, 2], [Symbol('avg'), 2, 2], [Symbol('add'), [Symbol('data'), [Symbol('data'), [Symbol('add'), [Symbol('max'), 2, 2], [Symbol('max'), 2, 2]]]], [Symbol('data'), [Symbol('data'), [Symbol('add'), [Symbol('max'), 2, 2], [Symbol('max'), 2, 2]]]]]]))

def depthCal(expr):
    if dir == []:
        return 0
    if isinstance(expr, list):
        depths = []
        for i in expr:
            depths.append(depthCal(i))
        return 1 + max(depths)
    else:
        return 0


def crossover(parent1,parent2):
    r1 = random.choice(get_dir(parent1))
    part1 = get_branch(r1,parent1)
    loop_count_1 = 0
    while depthCal(part1) < 2:
        r1 = random.choice(get_dir(parent1))
        part1 = get_branch(r1, parent1)
        loop_count_1 += 1
        if loop_count_1 == 10:
            break

    r2 = random.choice(get_dir(parent2))
    part2 = get_branch(r2,parent2)
    loop_count_2 = 0
    while depthCal(part2) < 2:
        r2 = random.choice(get_dir(parent2))
        part2 = get_branch(r2,parent2)
        loop_count_2 += 1
        if loop_count_2 == 10:
            break

    if r1 == []:
        parent1 = part2
    else:
        copy_parent1 = parent1
        temp = r1[-1]
        for i in r1:
            if i == temp:
                copy_parent1[i] = part2
                break
            else:
                copy_parent1 = copy_parent1[i]

    if r2 == []:
        parent2 = part1
    else:
        copy_parent2 = parent2
        temp = r2[-1]
        for i in r2:
            if i == temp:
                copy_parent2[i] = part1
                break
            else:
                copy_parent2 = copy_parent2[i]

    return parent1

def mutation(expr):
    if random.uniform(0,1) < 0.75:
        r_dir = random.choice(get_dir(expr))
        r_branch = get_branch(r_dir,expr)
        new_branch = init(2)
        if r_dir == []:
            expr = r_branch
        else:
            copy_expr = expr
            temp = r_dir[-1]
            for i in r_dir:
                if i == temp:
                    copy_expr[i] = new_branch
                    break
                else:
                    copy_expr = copy_expr[i]
    return expr


    # return depthCal(part1),depthCal(part2)

# print(get_branch(random.choice(get_dir(test_tree)),test_tree))
# print(crossover(test_tree1,test_tree2))
# print(mutation([Symbol('sqrt'), [Symbol('add'), [Symbol('mul'), 0, 0], [Symbol('mul'), 0, 0]]]))

def ranking(population,fitness):
    for j in range(len(fitness)):
        for i in range(0,len(fitness)-1):
            if math.isinf(fitness[i]) or math.isnan(fitness[i]):
                # Swap fitness
                temp1 = fitness[i]
                fitness[i] = fitness[i+1]
                fitness[i+1] = temp1
                # Swap population
                temp2 = population[i]
                population[i] = population[i+1]
                population[i+1] = temp2
            if fitness[i] > fitness[i+1]:
                # Swap fitness
                temp3 = fitness[i]
                fitness[i] = fitness[i+1]
                fitness[i+1] = temp3
                # Swap population
                temp4 = population[i]
                population[i] = population[i+1]
                population[i+1] = temp4
    return population,fitness


def ga(size,n_dimention,m_dataSize,data_directory,time_budget):
    timeStart = time.time()
    popSet,fitSet = population(size,4,n_dimention,m_dataSize,data_directory)
    generation = 200000
    for i in range(0,generation):
        if (time.time()-timeStart) > time_budget:
            break
        else:
            parent1 = popSet[random.randint(0, len(popSet) - 1)]
            parent2 = popSet[random.randint(0, len(popSet) - 1)]
            while parent1 == parent2:
                parent2 = popSet[random.randint(0, len(popSet) - 1)]
            if (time.time() - timeStart) > time_budget:
                break
            deep_parent1 = copy.deepcopy(parent1)
            deep_parent2 = copy.deepcopy(parent2)
            crossovered = crossover(deep_parent1,deep_parent2)
            if (time.time() - timeStart) > time_budget:
                break
            after_mutation = mutation(crossovered)
            if (time.time() - timeStart) > time_budget:
                break
            fitnessCal = fitness(dumps(after_mutation),n_dimention,m_dataSize,data_directory)

            if (time.time() - timeStart) > time_budget:
                break
            popSet.append(after_mutation)
            fitSet.append(fitnessCal)
        new_population,new_fitness = ranking(popSet,fitSet)
        popSet = new_population[0:size]
        fitSet = new_fitness[0:size]

        # print(fitSet[0:10],'\t')
    # print(fitSet[0:10],'\t')
    return fitSet[0] #dumps(test_tree1) popSet[0]

def test(loop):
    total = []
    for i in range(0,loop):
        result = ga(50, 5, 100, "data.txt", 10) #(popSize,dimention,datasize,data,time_budget)
        total = total + [result]
        print(total)

# print(test(20))
# print(tree_depth(init(10)))
# print(init(4))
# print(fitness("(add (mul 2 3) (div (add 12 3) 3))",1,100,'data1.txt'))
# print(population(5,5,1,100,"data1.txt"))
# print(ga(100,5,100,"data3.txt",60))
#  print(crossover(population(5,5,1,100,"data1.txt")[0],population(5,5,1,100,"data1.txt"))[1])



# Docker
docker = argparse.ArgumentParser()

docker.add_argument("-question", help="question num 1,2 or 3", type=int)
docker.add_argument("-n", help="input vector size", type=int)
docker.add_argument("-m", help="input data size", type=int)
docker.add_argument("-x", help="input a vector", type=str)
docker.add_argument("-expr", help="input expression", type=str)
docker.add_argument("-data", help="input file name", type=str)
docker.add_argument("-lambdainput", help="input population size", type=int)
docker.add_argument("-time_budget", help="input time budget", type=float)

parsed = docker.parse_args()

if parsed.question == 1:
    get_vector=parsed.x
    get_result_1 = niso_lab3(1,parsed.n,get_vector,parsed.expr)
    print(get_result_1)

if parsed.question == 2:
    get_result_2 = fitness(parsed.expr, parsed.n, parsed.m, parsed.data)
    print(get_result_2)
if parsed.question == 3:
    get_result_3 = ga(parsed.lambdainput,parsed.n,parsed.m,parsed.data,parsed.time_budget)
    print(get_result_3)


#print(mod(7,3))
#print(ifleq(2,1,3,4))
#print(niso_lab3("-question 1",2,3,4))
#print(loads('(add (add (1 2) add (1 2)))'))
#print(loads("(add (1) (2))"))
# print(parse_loads("(add 1 (add 1 2))"))
# print(parse_loads("(ifleq (add 1 2) 2 6 5)"))
# print(parse_loads("(add (mul 2 3) (mul 2 3))"))
# print(fopen('data1.txt',1))
# print(fitness("(add (mul 2 3) (div (add 12 3) 3))",1,100,'data1.txt'))
#print(parse_loads("(avg 1 2)"))
# print(niso_lab3(1, 4, '1.0 2.0 3.0 5.0', '(add (mul 2 3) (mul 2 3))'))

