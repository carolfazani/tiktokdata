class QueryValidation:
    def __init__(self, query: str, loadmore: int):
        if isinstance(query, str) and isinstance(loadmore, int):
            self.query = query
            self.loadmore = loadmore

        else:
            print('Entradas inválidas')
            exit()




