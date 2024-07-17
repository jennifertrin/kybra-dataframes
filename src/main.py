from kybra import query, Vec, int32
from pambdas import DataFrame

@query
def get_message() -> Vec[int32]:
    df1 = DataFrame({"one": [1, 2, 3]})
    result = {}
    for index in df1.index:
        result[index] = {col: df1[col][index] for col in df1.columns}
    return result
