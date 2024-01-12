import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'funboost_django_orm_demo.settings')

import django

django.setup()

### 上面这四行是必须要做的非常非常重要,如果脱离了web上下文环境,在独立的函数或者在funboost celery 后台中运行,一定先要设置好 DJANGO_SETTINGS_MODULE 环境变量,并执行 django.setup()


from students.your_functions import create_student

if __name__ == '__main__':
    create_student.consume()
