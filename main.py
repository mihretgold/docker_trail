def fizzBuzz(n):
    answer = []
    for idx in range(1, n + 1):
        if idx   % 3 == 0 and idx % 5 == 0:
            answer.append("Fizz Buzz")
        elif idx % 3 == 0:
            answer.append("Fizz")
        elif idx % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(idx))
            
    return answer

if __name__ == '__main__':
    n = int(input())
    answer = fizzBuzz(n)
    print(answer)