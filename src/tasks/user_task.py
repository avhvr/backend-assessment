from app import celery
from datetime import datetime

@celery.task(name='user.lastlogin')
def lastlogin(username):
    return {
        u"_id": username,
        u"date": datetime.now()
    }
