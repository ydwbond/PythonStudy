"""
inner function is good for
* Provide encapsulation
* Building Helpers to avoid do stuff not necessary
"""



def connect_db():
    def get_db_connection():
        print('privately get DB, can not be called outside')
    get_db_connection()

connect_db()

#get_db_connection() can not be called here


def fibonacci(input:int):
    if not isinstance(input,int):
        raise Exception('Input should be integer')
    if input <= 0:
        raise Exception('has been be bigger than 0')

    def _inner_fibonacci(input):
        if input == 1:
            output = [0]
        elif input == 2:
            output = [0,1]
        else:
            pre_output = _inner_fibonacci(input-1)
            pre_output.append(pre_output[input-2] + pre_output[input-3])
            output = pre_output
        return output
    return _inner_fibonacci(input)
print(fibonacci(6))