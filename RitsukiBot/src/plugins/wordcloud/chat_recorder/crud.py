from .database import Record


class ChatRecorder:
    @staticmethod
    def write(**kwargs):
        """
        user_id:int
        group_id:int
        message:str
        timestamp
        """
        Record.create(**kwargs)

    @staticmethod
    def get(**kwargs):
        """
        user_id:int
        group_id:int
        message:str
        timestamp
        """
        Record.select().where(**kwargs)
