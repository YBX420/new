import numpy as np
theta = [40-0.1,40,40+0.1]
m = 0.008
h_2 = [0.7-0.01,0.7,0.7+0.01]
l = [1.500-0.001,1.500,1.500+0.001]
g = 9.81
e = [0.4979-0.0142,0.4979,
        0.4979+0.0142]
d = 0.0125
r = d/2
results = []

def get_e():
    return e
def get_l():
    return l
def get_h_2():
    return h_2
def get_theta():
    return theta

def get_vr(theta,l):
    h = l*np.sin(np.deg2rad(theta))
    vr = np.sqrt(10*g*h/7)
    vx = vr*np.cos(np.deg2rad(theta))
    vy = vr*np.sin(np.deg2rad(theta))
    return vr,vx,vy

def get_t(theta,h_2,l):
    a = 0.5*g
    b = get_vr(theta,l)[2]
    c = -h_2
    t_1,t_2 = np.roots([a,b,c])
    if t_1 > 0 and t_2 > 0:
        return min(t_1,t_2)
    elif t_1 < 0 and t_2 < 0:
        raise ValueError
    else:
        return max(t_1,t_2)

def get_d2(theta,h_2,l):
    return get_t(theta,h_2,l)*get_vr(theta,l)[1]

def get_d3(theta,h_2,e,l):
    vcy = get_vr(theta,l)[2] + g*get_t(theta,h_2,l)
    vcy_ = e * vcy
    Tp = vcy_ * 2 / g
    d_3 = get_vr(theta,l)[1] * Tp
    return d_3 + get_d2(theta,h_2,l)

def get_result(theta,h_2,e,l):
    count = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for u in range(3):
                    count += 1
                    '''
                    print(count," For $theta$ = ",theta[i],
                            "; $h_2$ = ",h_2[j],
                            "; $e$ = ",e[k],
                            "; $l$ = ",l[u],
                            "; the value of $d_t$ is",end=' ')
                    '''
                    result = get_d3(theta=theta[i],
                                    h_2=h_2[j],
                                    e=e[k],
                                    l=l[u])
                    results.append(result)
                    #print(result)
    return results
def print_graph(results):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    x = [x for x in range(len(results))]
    plt.plot(x, results)
    plt.show()
get_result(theta,h_2,e,l)
print_graph(results)


def p_error(a,b,c):
    return abs(100*(a+c-b-b)/(2*b))

def calculate_error(results):
    p_error_e = []
    p_error_theta = []
    p_error_l = []
    p_error_h_2 = []
    for i in range(27):
        p_error_l.append(p_error
                        (results[i],
                        results[i+1],
                        results[i+2]))
        p_error_e.append(p_error
                        (results[i],
                        results[i+3],
                        results[i+6]))
        p_error_h_2.append(p_error
                        (results[i],
                            results[i+9],
                            results[i+18]))
        p_error_theta.append(p_error
                            (results[i],
                            results[i+27],
                            results[i+54]))
    return p_error_e, p_error_theta,p_error_l,p_error_h_2




p_error_e, p_error_theta,p_error_l,p_error_h_2 = calculate_error(results)
a_p_error_l = sum(p_error_l)/len(p_error_l)
a_p_error_e = sum(p_error_e)/len(p_error_e)
a_p_error_h_2 = sum(p_error_h_2)/len(p_error_h_2)
a_p_error_theta = sum(p_error_theta)/len(p_error_theta)

import pandas as pd
table = [a_p_error_l,
         a_p_error_e,
         a_p_error_h_2, 
         a_p_error_theta]
df = pd.DataFrame(table, 
                  columns = ['average persentage error'], 
                  index=['l','e','h_2','theta'])
print(df)