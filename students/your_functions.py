from django.db import close_old_connections

from funboost import boost, BoosterParams, BrokerEnum
from students.models import Student


def close_old_connections_deco(f):
    def _inner(*args, **kwargs):
        close_old_connections()
        res = f(*args, **kwargs)
        close_old_connections()
        return res

    return _inner


@boost(BoosterParams(queue_name='create_student_queue',
                     broker_kind=BrokerEnum.REDIS_ACK_ABLE,
                     consumin_function_decorator=close_old_connections_deco)
       )
def create_student(name, age, ):
    ''' 在funboost 后台进程中去操作 dajngo  orm'''
    student = Student.objects.create(name=name, age=age, )
    print(f"Created student: {student.name}")


if __name__ == '__main__':
    ''' 如果你想直接运行create_student函数,就必须设置环境变量 DJANGO_SETTINGS_MODULE ,并且执行django.setup() '''
    import os

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'funboost_django_orm_demo.settings')

    import django

    django.setup()

    ### 上面这四行是必须要做的,如果脱离了web上下文环境,在独立的函数或者在funboost celery 后台中运行,一定先要设置好配置文件环境变量,并执行 django.setup()

    create_student('xiaomin', 16)
