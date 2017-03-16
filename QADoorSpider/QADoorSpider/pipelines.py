from mysql import connector
from MySQLdb import connect
from contextlib import contextmanager
from .items import QuestionItem, AnswerItem
from .config import DB_CONFIG, QUESTION_TABLE, ANSWER_TABLE

@contextmanager
def open_mysql(db_conf):
    try:
        # conn = connector.connect(**db_conf)
        conn = connect(**db_conf)
        if conn:
            yield conn.cursor()
    except Exception as e:
        print('mysql连接错误:', e)
    finally:
        conn.commit()
        conn.close()

class QadoorspiderPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        if isinstance(item, QuestionItem):
            try:
                with open_mysql(DB_CONFIG) as cursor:
                    query_sql = "select * from %s where question_id=%s" %(QUESTION_TABLE, item['question_id'])
                    print(query_sql)
                    query_result = cursor.execute(query_sql)
                    # cursor.fetchall()
                    # print(query_result)
                    if not query_result:
                        print('问题{}不存在，准备插入questions'.format(item['question_id']))
                        inset_sql ='INSERT INTO ' + QUESTION_TABLE+ \
                                   '(question_id, reprint_link, title, content, status, answer_count, view_count, vote_count, created_date, updated_date, tags, source) ' \
                                   'VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                        print(inset_sql)
                        cursor.execute(inset_sql, (
                                item['question_id'],
                                item['reprint_link'],
                                item['title'],
                                item['content'],
                                item['status'],
                                item['answer_count'],
                                item['view_count'],
                                item['vote_count'],
                                item['created_date'],
                                item['updated_date'],
                                item['tags'],
                                item['source']
                            ))
                        print('问题插入成功')
                    else:
                        print('问题{}已存在'.format(item['question_id']))
            except Exception as e:
                print("Error %d: %s" % (e.args[0], e.args[1]))
        if isinstance(item, AnswerItem):
            try:
                with open_mysql(DB_CONFIG) as cursor:
                    query_sql = "select * from %s where question_id=%s" %(ANSWER_TABLE, item['question_id'])
                    print(query_sql)
                    query_result = cursor.execute(query_sql)
                    if not query_result:
                        print('问题{}的答案不存在，准备插入answers'.format(item['question_id']))
                        inset_sql ='INSERT INTO ' + ANSWER_TABLE+ \
                                   '(question_id, content, votes) ' \
                                   'VALUES(%s, %s, %s)'
                        print(inset_sql)
                        cursor.execute(inset_sql, (
                                item['question_id'],
                                item['content'],
                                item['votes']
                            ))
                        print('答案插入成功')
                    else:
                        print('问题{}的答案已存在'.format(item['question_id']))
            except Exception as e:
                print("Error %d: %s" % (e.args[0], e.args[1]))
        return item