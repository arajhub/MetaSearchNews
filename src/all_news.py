class AllNews:
    def __init__(self, summary, title, category, date_time, rank, src, meta_rank=0):
        self.title = title
        self.summary = summary
        self.category = category
        self.date_time = date_time
        self.src = src
        self.rank = rank
        self.meta_rank = meta_rank

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
