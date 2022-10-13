from typing import List, Optional
from wordcloud import WordCloud
from io import BytesIO
from pathlib import Path
from .database import Record

source_han_sans = Path().resolve() / "data" / "fonts" / "SourceHanSans.otf"


class ChatRecorder:
    @staticmethod
    def write_record(**kwargs):
        """
        user_id:int
        group_id:int
        message:str
        timestamp
        """
        Record.create(**kwargs)

    @staticmethod
    def generate_wordcloud(date: str, group_id: int, user_id: Optional[int] = None):
        if user_id:
            records: List[Record] = Record.select(Record.message).where(
                (Record.date == date)
                & (Record.group_id == group_id)
                & (Record.user_id == user_id)
            )
        else:
            records: List[Record] = Record.select(Record.message).where(
                (Record.date == date) & (Record.group_id == group_id)
            )
        messages = " ".join((i.message for i in records))  # type: ignore
        wordcloud = WordCloud(
            font_path=str(source_han_sans),
            background_color="white",
            width=1920,
            height=1200,
        ).generate(messages)
        image = wordcloud.to_image()
        buffer = BytesIO()
        image.convert("RGB").save(buffer, "jpeg")
        return buffer
