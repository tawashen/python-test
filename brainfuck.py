def decide_memory_size():
    answer = int(input ("メモリのサイズを決めてくれ"))
    return [0] * (answer + 1)

memory = decide_memory_size()

def c_right(vec): #->memory
    if vec[-1] >= len(vec):
        return vec
    else:
        vec[-1] += 1
        return vec
def c_left(vec):
    if vec[-1] == 0:
        return vec
    else:
        vec[-1] -= 1
        return memory
def c_plus(vec):
    vec[vec[-1]] += 1
    return vec
def c_minus(vec):
    if vec[vec[-1]] <= 0:
        return vec
    else:
        vec[vec[-1]] -= 1
        return vec
def c_comma(vec):
    answer_comma = input("Ascii文字を入力せよ")
    vec[vec[-1]] = ord(answer_comma)
    return vec
def c_period(vec):
    print(chr(vec[vec[-1]]))
    return vec
def c_from(vec):
    command_list = []
    def from_innner(command_list):
        answer = input("ループするコマンドを入力せよ")
        if answer == ">":
            command_list.append(c_right)
        



def brain_read(memory):
    answer = input("command?")
    if answer == ">":
        brain_read(c_right(memory))
    elif answer == "<":
        brain_read(c_left(memory))
    elif answer == "+":
        brain_read(c_plus(memory))
    elif answer =="-":
        brain_read(c_minus(memory))
    elif answer ==",":
        brain_read(c_comma(memory))
    elif answer ==".":
        brain_read(c_period(memory))        
    elif answer == "p":
        print(memory)
    else:
        brain_read(memory)


brain_read(memory)
#print(memory)


