"""https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
        
    integer_tuple = tuple(integer_list)
    
    output = hash(integer_tuple)
    
    print(output)
        