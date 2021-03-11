from api.resources import Index


def initialize_routes(api):
    api.add_resource(
        Index, '/<string:fnme>/<string:lnme>/<string:dsg>/<string:ass>/<string:dr>/<string:no>/<string:gen>/<string:em>/<string:emex>')
