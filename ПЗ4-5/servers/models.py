class SuspiciousQuery:
    def __init__(self, query: str, duration: float = 0.0):
        self.query = query
        self.duration = duration

    def get_info(self) -> str:
        raise NotImplementedError()


class SlowQuery(SuspiciousQuery):

    def get_info(self) -> str:
        return f"SLOW: '{self.query}' выполнялся {self.duration:.2f} сек."


class NoIndexQuery(SuspiciousQuery):

    def get_info(self) -> str:
        return f"NO_INDEX: '{self.query}' — индекс не использован"


class InjectionQuery(SuspiciousQuery):


    def get_info(self) -> str:
        return f"INJECTION: подозрительный фрагмент в '{self.query}'"


class QueryTypeFactory:

    _registry = {
        "slow": SlowQuery,
        "noindex": NoIndexQuery,
        "injection": InjectionQuery,
    }

    @classmethod
    def create(cls, query_type: str, query: str, duration: float = 0.0) -> SuspiciousQuery:
        if query_type not in cls._registry:
            raise ValueError(f"Неизвестный тип запроса: {query_type}")
        return cls._registry[query_type](query, duration)