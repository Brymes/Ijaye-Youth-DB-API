from flask_restful import Resource
from api.models import Db

from http import HTTPStatus


class Index(Resource):
    def get(self):
        return "Hello, World!"

    def post(self, fnme, lnme, dsg, ass, dr, no, gen, em, emex):

        assemblies = {
            'ij': 'Ijaye',
            'aj': 'Ajegunle',
            'ag': 'Aguda',
            'sh': 'Shiaba',
            'if': 'Ifeloju',
            'or': 'Orile',
            'al': 'Alausa',
            'og': 'Ogo Oluwa'
        }

        drs = {
            'ag': 'Agege',
            'or': 'Orile-Agege',
            'og': 'Oregun'
        }

        genders = {
            'f': 'Female',
            'm': 'Male'
        }

        email_extensions = {
            'g': '@gmail.com',
            'y': '@yahoo.com',
            'i': '@icloud.com'
        }

        dsgs = {
            'b': 'Bro',
            'e': 'Elder',
            's': 'Sis',
            'ds': 'Deaconess',
            'dc': 'Deacon'
        }

        x = email_extensions[emex]
        data = Db(
            designation=dsgs[dsg],
            full_name=f'{fnme} {lnme}',
            assembly=assemblies[ass],
            district=drs[dr],
            phone_no=f'{no}',
            email=em + x,
            gender=genders[gen]
        )

        data.save()

        del x

        return HTTPStatus.OK
