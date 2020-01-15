
"""
Lab2-2. Wolfram-Beta OO
support cos, sin, exp
float type degree & factor

Object Oriented
using classes
    WolframBeta
    Terms (has terms_dict)
"""
import traceback
import math
import re

def matching_sign_degree(data):
    match = re.search('cos',data)
    if(match):
        return 'cos'
    match = re.search('sin',data)
    if(match):
        return 'sin'
    match = re.search('cos',data)
    if(match):
        return 'exp'
    
    return None



def matching_sign_factor(data):
    
    match = re.match('[0-9|\.|-]cos',data)
    match = re.match('[0-9|\.|-]sin',data)
    match = re.match('[0-9|\.|-]cos',data)
    if(match):
        return data[:-3]
    
    return None


def matching_factor(data):
    match = re.match('[-|0-9|\.]+',data)
    
    if match:
        return match.group()
    else:
        match = re.match('^x',data)
        if match:
            return '1'
        else:
            match = re.match('^x',data)
            return '0'

def matching_degree(data):
    match = re.search('x\^[0-9|\.|-]+',data)
    if match:
        return match.group()[2:]
    else:
        match = re.search('x',data)
        if match:
            return '1'
        else:
            matching_sign_degree
            return '0'

class Terms:
    def __init__(self, equation=None):
        """
        :param equation: str, 문자열로 표현된 함수
                        None 인 경우 terms_dict 를 생성만 함
        """
        # make Terms.terms : dict {key = degree, val = factor}
        # store the equation if not None
        self.terms_dict = dict()
        self.equation = equation
        pass

    def __str__(self):
        """
        :return: str equation
        """
        # this function support interface
        # str(Terms) -> string (equation)
        return self.print_equation()

    def __eq__(self, other):
        """
        :param other: Terms
        :return: True when equal, ow False
        """
        # don't modify this function
        if type(other) != Terms:
            return False

        t1 = self.terms_dict
        t2 = other.terms_dict
        eps = 1e-6

        keys = set(t1.keys()).union(t2.keys())
        for k in keys:
            if not math.isclose(t1.get(k, 0), t2.get(k, 0),
                                rel_tol=eps, abs_tol=eps):
                return False
        return True

    @staticmethod
    def print_term(degree, factor):
        """
        :param degree: float, 항의 계수
        :param factor: float, 항의 차수
        :return: str
        """
        # use wolfram_beta's print_term
          #print_term(2, 0)
    
        if (degree != 1):
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



    def print_equation(self):
        """
        :param self: self.terms_dict: dict {key=degree, value=factor}
        :return: str equation
        """
        # use wolfram_beta's print_equation
        terms=self.terms_dict
        tl = list()
        for key,values in terms.items():
            #if(values == 0):
            #    continue
            
            tl.append(self.print_term(key,values))
        result = " + ".join(tl)
        print(result) 

        return result
        #return str()

    @staticmethod
    def parse_term(term_str):
        """
        :param term_str: str (a single term <- a part of equation)
        :return: 2-tuple (degree: float/str, factor: float)
        """
        # use wolfram_beta's parse_term
        # now, degree is float
        #             or (cos(x), sin(x), exp(x)
        #      factor is float
        print(term_str)
        factor =matching_factor(term_str)
        degree =matching_degree(term_str)
        if(factor =='-'):
            factor = '-1'
        
        return float(degree),float(factor)
        #return (0.0, 0.0)

    def parse_equation(self, equation):
        """
        :param equation: str
        :return: None (modify self.terms_dict)
        """
        # update self.terms_dict
        # terms in equation is separated by ' + '
        # use dict.get(key, default)

        resultDic = dict()
        l1 = equation.split(" + ")
        for item in l1:
            key,value =self.parse_term(item)
            resultDic[key]=value + resultDic.get(key, 0)

        self.terms_dict = resultDic

    def d_dx_as_terms(self):
        """
        :return: Terms : that result of differential
        """
        # make Terms that result of differential

        dterms = Terms()
        
        resultDic = dict()
        for key,value in self.terms_dict.items():
            print(key,value)
            if(key !=0 ):
                resultDic[key-1 ] = value*key
            else:
                continue
        if(len(resultDic)==0):
            resultDic[0] = 0
        print("result is ", resultDic)
        
        self.terms_dict = resultDic
        dterms.terms_dict = resultDic
        # process each term (degree, factor) in terms
        # use dict.get(key, default)

        return dterms

    def integral_as_terms(self, constant):
        """
        :param constant: float
        :return: Terms : that result of integral
        """
        # make Terms that result of integral
        iterms = Terms()

        # process each term (degree, factor) in terms
        # use dict.get(key, default)

        # don't forget the constant
        resultDic = dict()
        for key,value in self.terms_dict.items():
            print("key value  ",key,value)
            resultDic[key+1] = value/(key+1)
        print("result is ", resultDic)
        iterms.terms_dict = resultDic
        self.terms_dict = resultDic
        print(iterms.terms_dict)


        return iterms

    def compute_as_terms(self, x):
        """
        :param x: float
        :return: float
        """
        result = 0.0
        print("terms " , self.terms_dict)
        for degree,value in self.terms_dict.items():
            result += value* ( x ** degree)
        print(result)
        # compute the result using Terms
        return result


class WolframBeta:
    def __init__(self, input_path, output_path):
        """
        :param input_path: path of input query file
        :param output_path: path of output file storing result
                            generated by wolfram beta
        """
        self.input_path = input_path
        self.output_path = output_path

        # if you need more initializing process,
        # just write your code !

        pass

    @staticmethod
    def d_dx(equation):
        """
        :param equation: str
        :return: equation str (differential result)
        """
        # using Terms's class function
        term = Terms(equation)


        print("equation ", equation)
        term.parse_equation(equation)
        term.d_dx_as_terms()
        result =term.print_equation()
        #print(result)
        return result
        #return str()  # equation

    @staticmethod
    def integral(equation, constant):
        """
        :param equation: str
        :param constant: str
        :return: str equation (integral result)
        """
        # using Terms's class function
        term = Terms(equation)
        term.parse_equation(equation)
        term.integral_as_terms(constant)
     
        result = term.print_equation()

        print(result)
        return  str(constant) +" + " + result  # equation

    @staticmethod
    def compute(equation, x):
        """
        :param equation: str
        :param x: str
        :return: str <- not int type
        """
        # using Terms's class function
        term = Terms(equation)
        term.parse_equation(equation)
        result = 0
        result = term.compute_as_terms(float(x))
        
        return str(result)  # result

    def solve_query(self, line):
        """
        :param line: str (query)
        :return: str (result)
        """
        try:
            # 이 안에 코드를 작성해주세요!
            # solve_query() 함수에서 실행 도중 불가피한 오류가 발생하더라도,
            # 다음 쿼리를 받아들일 수 있게 도와줍니다.

            tlist = line.rstrip().split(',')
            result =""

            if(tlist[0] =='D'):
                result=self.d_dx(tlist[1])
                pass
            if(tlist[0] =='D2'):
                '''
                Input: D2,x^3
                Expected: 6x
                '''
                result=self.d_dx(tlist[1])
                pass

            if(tlist[0] =='I'):
                result=self.integral(tlist[1],tlist[2])
                pass

            if(tlist[0] =='I3'):
                '''
                Input: I2,6x,0
                Expected: 0 + 0 + x^3
                '''

            if(tlist[0] =='C'):
                print(tlist[1],tlist[2])
                result=self.compute(tlist[1],tlist[2])
                pass

            print(result)


            return result  # if line == 'D,x^2'
        except:
            traceback.print_exc()
            return ''

    def solve(self):
        """
        :return: None (파일 입출력으로 문제 해결)
        """
        fh = open(self.input_path)
        fhw =open(self.output_path,'w')
        for line in fh:
            result=self.solve_query(line)
            fhw.write(result)
            fhw.write('\n')

        fh.close()
        fhw.close()    
        return


if __name__ == '__main__':
    ipath = 'input_sample.txt'
    opath = 'output_sample1.txt'
    
    wolfram_beta = WolframBeta(ipath, opath)
    wolfram_beta.solve()
    '''
    terms = Terms()
    assert terms.print_term(2, 0) == "0x^2"
    assert terms.print_term(1, -1) == "-x"
    assert terms.print_term(1, 1) == "x"
    assert terms.print_term(0, 5) == "5"
    assert terms.print_term(2, 1) == "x^2"


    terms.parse_equation("5 + -2x^4 + -7x^5 + -6x^2 + -4x^3")
    print(terms.terms_dict)
    print(terms.print_equation())
    '''
    '''
    assert terms.d_dx_as_terms({1: 3, 3: 2}) == {0: 3, 2: 6}
    assert print_equation({2:0, 1:-1, 0:5}) == "0x^2 + -x + 5"
    assert print_equation({1:-1, 0:5}) == "-x + 5"
    

    assert terms.parse_term("0x^2") == (2, 0)
    assert terms.parse_term("-x") == (1, -1)
    assert terms.parse_term("5") == (0, 5)
    assert terms.parse_equation("0x^2 + -x + 5") == {2:0, 1:-1, 0:5}
    
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
    '''