import random
import math

populations = []
rand = []
opt = 0

#first individuals
first = []
for i in range(8):
    first.append(random.randint(0,255))

#create_ans
def create_ans():
    ans = []
    for i in range(8):
        ans.append([0,0.0,0.0,0.0])
    return ans

#binary_to_decimal
def binary_to_decimal(populations):
    carry = []
    for i in range(8):
        x = ""
        for j in range(8):
            x += str(populations[i][j])
        carry.append(int(int(x, 2)))
    return carry

#find f(x),Sum of f(x),f_norm,cumulative
def reproduction(first):
    ans = create_ans()
    populations = []
    opt = 0
    total_f = 0.0
    fx = 0.0
    for i in range(8):
        indi = int(first[i])
        t = round(math.sin((math.pi*indi)/256),10)
        total_f += t
        ans[i][0] = indi
        ans[i][1] = t
        binary = format(indi,'08b')
        binn = []
        for j in range(8):
            binn.append(int(str(binary[j])))
        populations.append(binn)
        if fx < ans[i][1]:
            opt = ans[i][0]
            fx = ans[i][1]
    f_norm = 0.0
    for i in range(8):
        fnorm = round(ans[i][1]/total_f,10)
        f_norm += fnorm
        ans[i][2] = fnorm
        ans[i][3] = round(f_norm,10)
        
    return ans,opt,populations
    
#print_show_table
def print_show_table(ans):
    for i in range(8):
        print(ans[i][0],ans[i][1],ans[i][2],ans[i][3])
        
#print_show_table
def print_show_pop(pop):
    for i in range(8):
        print(pop[i][0],pop[i][1],pop[i][2],pop[i][3],pop[i][4],pop[i][5],pop[i][6],pop[i][7])

#ramdom new value
def random_new():
    rand = []
    for i in range(8):
        cross = round(random.uniform(0.0,1.0), 5)
        rand.append(cross)
    return rand

def new_pop(rand,ans):
    c = []
    carry = ans
    for i in range(8):
        for j in range(8):
            if rand[i] < carry[j][3]:
                c.append(carry[j][0])
                break;
    return c

#best
def is_better(old,new):
    best = []
    for i in range(8):
        old_1 = round(math.sin((math.pi*old[i])/256),10)
        new_1 = round(math.sin((math.pi*new[i])/256),10)
        if old_1 >= new_1:
            best.append(int(old[i]))
        else:
            best.append(int(new[i]))
    return best
        
def cross_over(populations):
    print("\nChoose Cross over")
    first = random.randint(0,7)
    second = random.randint(0,7)
    slice1 = random.randint(0,7)
    slice2 = random.randint(0,7)
    
    while first == second:
        second = random.randint(0,7)
    while slice1 == slice2:
        slice2 = random.randint(0,7)
    if first < second:
        print("set "+str(first+1)+" and set "+str(second+1))
    else:
        print("set "+str(second+1)+" and set "+str(first+1))
    if slice1 < slice2:
        print("address "+str(slice1+1)+" to "+str(slice2+1))
    else:
        print("address "+str(slice2+1)+" to "+str(slice1+1))

    if slice2 > slice1:
        for j in range(slice1,slice2-1):
            temp = populations[first][j]
            populations[first][j] = populations[second][j]
            populations[second][j] = temp
    else:
        for j in range(slice2,slice1-1):
            temp = populations[first][j]
            populations[first][j] = populations[second][j]
            populations[second][j] = temp
    return populations

def mutation(populations):
    for i in range(8):
        for j in range(8):
            m_rate = round(random.uniform(0.0,1.0), 5)
            if m_rate < 0.9 :
                if populations[i][j] == 1:
                    populations[i][j] = 0
                else:
                    populations[i][j] = 1
    return populations
      
for i in range(30):
    if opt == 128:
        break;
    else:
        print("\n#"+str(i))
        ans,opt,populations = reproduction(first)
        print(first)
        print_show_table(ans)
        print("\nPopulations")
        print_show_pop(populations)
        rand = random_new()
        print("\nRandom")
        print(rand)
        first = new_pop(rand,ans)
        print("\nX after roulette wheel")
        print(first)
        ans,opt,populations = reproduction(first)
        print("\nTable")
        print_show_table(ans)
        print("\nPopulations after random")
        print_show_pop(populations)
        cross_over(populations)
        print("\nPopulations after cross over")
        print_show_pop(populations)
        compare = mutation(populations)
        compare_x = binary_to_decimal(compare)
        print("\nCompare with old X")
        print("New :",compare_x)
        print("Old: ",first)
        print("\nPopulations after mutation")
        print_show_pop(compare)
        best = is_better(first,compare_x)
        print("\nBEST new individuals")
        print(best)
        first = best
        ans,opt,populations = reproduction(first)
        print("\nOptimal")
        print(opt)
    
    
    
