class BaseRepository:
    class Meta:
        abstract = True

    @staticmethod
    def search():
        return NotImplemented

    @staticmethod
    def fetch():
        return NotImplemented

    @staticmethod
    def save(obj_id):
        return NotImplemented
