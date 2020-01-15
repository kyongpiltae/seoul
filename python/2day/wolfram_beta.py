
"""
Lab2-1. Wolfram-Beta
only int range degree & factor

Not Object Oriented,
just functions (not class)
"""
import traceback
import re

def matching_factor(data):
    match = re.match('[-|0-9]+',data)

    
    if match:
        return match.group()
    else:
        match = re.match('^x',data)
        if match:
            return '1'
        else:
            return '0'
def matching_degree(data):
    match = re.search('x\^[0-9]+',data)
    if match:
        return match.group()[2:]
    else:
        match = re.search('x',data)
        if match:
            return '1'
        else:
            return '0'

def print_term(degree, factor):
    """
    :param degree: int, 항의 차수 
    :param factor: int, 항의 계수
    :return: str
    """
    #print_term(2, 0)
    
    if (degree >= 2):
        if factor == 1:
            factor =""
        if factor == -1:
            factor ="-"

        return str(factor)+'x'+'^'+str(degree)       
    if (degree == 1):
        if factor == 1:
            factor =""
        if factor == -1:
            factor ="-"

        return str(factor)+'x'
       
    return str(factor)
    

def print_equation(terms):
    """
    :param terms: dict {key=degree, value=factor}
    :return: str
    """
    tl = list()
    for key,values in terms.items():
        #if(values == 0):
        #    continue
        
        tl.append(print_term(key,values))
    result = " + ".join(tl)
    print(result) 

    return result
    #return '1 + 5x^2'    # when terms == {0: 1, 2: 5}



def parse_term(term_str):
    """
    :param term_str: str
    :return: 2-tuple (degree: int, factor: int)
    """
    print(term_str)
    factor =matching_factor(term_str)
    degree =matching_degree(term_str)
    if(factor =='-'):
        factor = '-1'
    
    #print("factor = ",factor)
    #print("degree = ",degree)

    return int(degree),int(factor)



    
    # return 2, 5    # when term_str == '5x^2'


def parse_equation(equation):
    """
    :param equation: str
    :return: dict {key=degree, value=factor}
    """
    resultDic = dict()
    l1 = equation.split(" + ")
    for item in l1:
        key,value =parse_term(item)
        resultDic[key]=value

    return resultDic
    #return {1: -7, 2: 3}    # when equation == '-7x + 3x^2'


def d_dx_as_terms(terms):
    """
    :param terms: dict {key=degree, value=factor}
    :return: dict {key=degree, value=factor}
             terms와 동일한 형식, 값은 terms의 미분 결과
    """
    print(terms)
    resultDic = dict()
    for key,value in terms.items():
        print(key,value)
        if(key >= 1):
            resultDic[key-1 ] = value*key
        else:
            continue
    if(len(resultDic)==0):
        resultDic[0] = 0
    print("result is ", resultDic)
    return resultDic
    #return {0: 3, 2: 6}    # when terms == {1: 3, 3: 2}


def d_dx(equation):
    """
    :param equation: str
    :return: str (differential result)
    """
    print("equation ", equation)
    resultDic = parse_equation(equation)
    print(resultDic)
    output = d_dx_as_terms(resultDic)
    print(output)
    result = print_equation(output)
    print(result)
    return result
    #return '2 + 6x'    # when equation == '2x + 3x^2'


def integral_as_terms(terms, constant):
    """
    :param terms: dict (key=degree, value=factor)
    :param constant: int
    :return: dict {key=degree, value=factor}
             terms와 동일한 형식, 값은 terms의 적분 결과
    """
    print(terms," ", constant)
    resultDic = dict()
    for key,value in terms.items():
        resultDic[key+1] = value//(key+1)
        
    print("result is ", resultDic)
    return resultDic


    #return {0: 6, 1: -2, 2: 5}    # when terms == {0: -2, 1: 10} and constant == 6


def integral(equation, constant):
    """
    :param equation: str
    :param constant: str
    :param constant: str (integral result)
    """
    print("equation ", equation)
    resultDic = parse_equation(equation)
    print(resultDic)
    output = integral_as_terms(resultDic,constant)
    print(output)
    
    result = print_equation(output)
    print(result)
    return  result +" + " + str(constant)

    #return '5 + 3x + 5x^5'    # when equation == '3 + 25x^4' and constant == 5


def compute_as_terms(terms, x):
    """
    :param terms: dict (key=degree, value=factor)
    :param x: int
    :return: int
    """
    result = 0
    for degree,value in terms.items():
        result += value* ( x ** degree)
    print(result)

    return result    # when terms == {0: 5, 1: -3, 2: 1} and x = 3


def compute(equation, x):
    """
    :param equation: str
    :param x: str
    :return: str <- not int type
    """
    resultDic = parse_equation(equation)
    intval = compute_as_terms(resultDic,int(x))

    return str(intval)    # when equation == '5 + -3x + x^2' and x == 3


def solve_query(line):
    """
    :param line: str
    :return: str
    """
    try:
        # 이 안에 코드를 작성해주세요!
        # solve_query() 함수에서 실행 도중 불가피한 오류가 발생하더라도,
        # 다음 쿼리를 받아들일 수 있게 도와줍니다.

        tlist = line.split(',')
        result =""

        if(tlist[0] =='D'):
            result=d_dx(tlist[1])
            pass

        if(tlist[0] =='I'):
            result=integral(tlist[1],tlist[2])
            pass

        if(tlist[0] =='C'):
            print(tlist[1],tlist[2])
            result=compute(tlist[1],tlist[2])
            pass

        print(result)


        


        return result    # if line == 'D,x^2'
    except:
        traceback.print_exc()
        return ''


def solve(input_path, output_path):
    """
    :param input_path: str
    :param output_path: str
    :return: None (파일 입출력으로 문제 해결)
    """
    fh = open(input_path)
    fhw =open(output_path,'w')
    for line in fh:
        result=solve_query(line)
        fhw.write(result)
        fhw.write('\n')

    fh.close()
    fhw.close()
 

    return


if __name__ == '__main__':
    ipath = 'input_sample.txt'
    opath = 'output_sample.txt'

    solve(ipath, opath)
    
    assert print_term(2, 0) == "0x^2"
    assert print_term(1, -1) == "-x"
    assert print_term(1, 1) == "x"
    assert print_term(0, 5) == "5"
    assert print_term(2, 1) == "x^2"
    assert d_dx_as_terms({1: 3, 3: 2}) == {0: 3, 2: 6}
    
    assert print_equation({2:0, 1:-1, 0:5}) == "0x^2 + -x + 5"
    assert print_equation({1:-1, 0:5}) == "-x + 5"

    assert parse_term("0x^2") == (2, 0)
    assert parse_term("-x") == (1, -1)
    assert parse_term("5") == (0, 5)
    assert parse_equation("0x^2 + -x + 5") == {2:0, 1:-1, 0:5}
    assert d_dx("x^2 + -x + 5") == "2x + -1"
    
    assert d_dx("7x^22") == "154x^21"
    assert d_dx("3x^3 + 162 + -x^18 + -2x") == "9x^2 + -18x^17 + -2"

  


    assert integral("2x + -1", 5) == "x^2 + -x + 5"
    assert integral("0", -761) == "-761 + 0x"


    assert compute("2x + -1", 5) == "9"


    assert solve_query("D,x^2 + -x + 5") == "2x + -1"
    assert solve_query("D,-256") == "0"
    assert solve_query("I,2x + -1,5") == "x^2 + -x + 5"
    assert solve_query("C,2x + -1,5") == '9'
    