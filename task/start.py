from tasks import *
import celeryconfig
app.config_from_object(celeryconfig)

crawler.delay()
