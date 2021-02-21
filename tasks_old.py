# import celeryconfig
# from celery import Celery

# # celery with config together
# app = Celery('tasks',backend='rpc://', broker='pyamqp://guest@localhost//')

# ## celery with config file
# # app=Celery()
# # app.config_from_object(celeryconfig)


# @app.task
# def add(x, y):
#     return x + y