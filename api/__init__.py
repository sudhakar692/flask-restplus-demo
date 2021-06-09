from flask_restplus import Api
from . import enquiry
from flask import current_app as app

# doc = False
# if app.env != 'prod':
# 	doc = True
doc=True
api = Api(doc=doc)
api.add_namespace(enquiry.api_namespace)