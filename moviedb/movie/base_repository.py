class BaseRepository:
    class Meta:
        abstract = True

    @staticmethod
    def search(title, mtype, year, page):
        return NotImplemented

    @staticmethod
    def fetch(imdbid, title, mtype, year, plot):
        return NotImplemented

    @staticmethod
    def save(obj_id):
        return NotImplemented
