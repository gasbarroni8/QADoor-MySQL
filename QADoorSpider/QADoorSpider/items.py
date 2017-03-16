from scrapy import Item, Field


class QuestionItem(Item):
    # id = Field()
    # user_id = Field()
    question_id = Field()
    reprint_link = Field()
    title = Field()
    content = Field()
    status = Field()
    answer_count = Field()
    view_count = Field()
    vote_count = Field()
    tags = Field()
    source = Field()
    created_date = Field()
    updated_date = Field()

class AnswerItem(Item):
    # id = Field()
    question_id = Field()
    content = Field()
    # user_id = Field()
    votes = Field()
    created_date = Field()
    updated_date = Field()
