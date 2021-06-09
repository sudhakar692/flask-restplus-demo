from flask_restplus import Namespace, fields, reqparse, Resource
import json

api_namespace = Namespace('Enquiry', description="Routes for todo create/read/update/delete", path='/enquiry')


# get data from query params
ENQUIRY_QUERY_PARAMS = reqparse.RequestParser()
ENQUIRY_QUERY_PARAMS.add_argument('source', type=str, required=True)

ENQUIRY_CREATE_MODEL = api_namespace.model("EnquiryRequestModel", {
        'name': fields.String(required=True),
        'email': fields.String(required=True),
        'phone': fields.String(required=True),
        'location': fields.String(required=True),
        'package_id': fields.Integer()
    })

ENQUIRY_RESPONSE_MODEL = api_namespace.model('EnquiryResponseModel', {
    'name': fields.String(required=True),
    'email': fields.String(required=True)
})

ENQUIRY_UPDATE_MODEL = api_namespace.clone('EnquiryUpdateModel', ENQUIRY_CREATE_MODEL, {
    "id": fields.Integer(required=True)
    })

ENQUIRY_UPDATE_RESPONSE_MODEL = api_namespace.clone('EnquiryUpdateResponseModel', ENQUIRY_RESPONSE_MODEL)

@api_namespace.route("")
class Enquiry(Resource):
    @api_namespace.expect(ENQUIRY_CREATE_MODEL, validate=True)
    @api_namespace.marshal_with(ENQUIRY_RESPONSE_MODEL)
    def post(self):
        api_namespace.payload.parse()
        return  {**api_namespace.payload}

    @api_namespace.expect(ENQUIRY_UPDATE_MODEL)
    @api_namespace.marshal_with(ENQUIRY_UPDATE_RESPONSE_MODEL)
    def put(self):
        name = api_namespace.payload.get('name')
        name = "{} Modified".format(name)
        return {"name": name, 'email': api_namespace.payload.get('email')}

    @api_namespace.expect(ENQUIRY_QUERY_PARAMS)
    def get(self):

        try:  # Will raise an error if date can't be parsed.
            args = ENQUIRY_QUERY_PARAMS.parse_args()  # type `dict`
            return args
        except Exception as e:  # `a_date` wasn't provided or it failed to parse arguments.
            print(e)
            return {}, 400
