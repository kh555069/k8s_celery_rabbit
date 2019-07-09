import os
broker_service_host = os.environ.get('RABBITMQ_SERVICE_SERVICE_HOST')
broker_url = 'amqp://guest@{}:5672//'.format(broker_service_host)

imports = ('tasks',)
task_default_queue='tasks'
