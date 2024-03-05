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

from functools import reduce

def c_from(vec):
    command_list = []
    def from_inner(command_list):
        answer = input("ループするコマンドを入力せよ")
        if answer == "]":
            origin_command_list = command_list
            pointer = vec[-1]
            def to_point_zero(vec, command_list):
                new_vec = reduce(lambda world, x:x(world), command_list, vec)
                if new_vec[pointer] == 0:
                    return new_vec
                else:
                    to_point_zero(new_vec, origin_command_list)
            to_point_zero(vec, origin_command_list)
        else:
            command_list.append(command_table[answer])
            from_inner(command_list)
            
    from_inner(command_list)
    return vec
#From_innerでVecが返って来て、ここでVecを返せるということは
#破壊的に実引数が変化してるってことか？
            

command_table = {">": c_right, "<": c_left, "+": c_plus, "-": c_minus,
                ",": c_comma, ".": c_period}


def brain_read(memory):
    answer = input("command?")
    if answer == "p":
        print(memory)
    elif answer == "[":
        brain_read(c_from(memory))
    elif len(answer) >= 2 and answer[0] == "+":
        brain_read(c_plus_multi(memory))
    elif len(answer) >= 2 and answer[0] == "-":
        brain_read(c_minus_multi(memory))
    else:
        brain_read(command_table[answer](memory))
        

brain_read(memory)
#print(memory)


