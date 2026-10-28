class SuspiciousQueryLogger:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, query_type: str, query: str) -> str:
        entry = f"[{query_type}] {query}"
        self.logs.append(entry)
        return entry

    def get_all_logs(self) -> list:
        return self.logs

    def clear(self):
        self.logs.clear()