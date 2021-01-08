class AllNews:
    def __init__(self, summary, title, category, date_time, rank, src):
        self.title = title
        self.summary = summary
        self.category = category
        self.date_time = date_time
        self.src = src
        self.rank = rank

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
