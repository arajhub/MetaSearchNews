class AllNews:
    def __init__(self, summary, title, category, date_time, rank, src):
        self.summary = summary
        self.title = title
        self.category = category
        self.date_time = date_time
        self.rank = rank
        self.src = src

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
