from http import HTTPStatus
from uuid import uuid4
from flask import jsonify, request
from bson.objectid import ObjectId
from api.utils import ResourceView
from bson.objectid import ObjectId

from math import ceil

class RecordSearch(ResourceView):

    def __init__(self, db):
        self.db = db
        self.qs = self.db.records
    
    def head(self):
        """This returns a header NUMBER_OF_RECORDS to query the amount of RECORDS and decide if it worths
        to do the GET requestor just want to know the number of songs."""
        
        return {}, HTTPStatus.OK, {'NUMBER_OF_RECORDS': self.qs.count()}

    def get(self):

        search_term = request.args.get('q')
        min_rate = request.args.get('rate_minimum')
        verified_skills = request.args.get('verified_skills')

        return self.search_queryset(search_term, min_rate, verified_skills)

    def search_queryset(self, search_term, min_rate, verified_skills):
        if isinstance(min_rate, type(None)):
            min_rate = 0.0
        else:
            min_rate = float(min_rate)
        
        regex_seach_term = {'$regex': r'(?i){}'.format(search_term)}
        rqs = self.qs.find({
            '$or': [
                {'first_name': regex_seach_term},
                {'last_name': regex_seach_term},
                {'address': regex_seach_term},
                {'contact_email': regex_seach_term},
                {'eyeColor': regex_seach_term},
            ]
        })
        response = [self._search_id(record) for record in rqs if self._rate2float(record['min_rate']) >= min_rate] if rqs else []
        if isinstance(verified_skills, str):
            response = [self._search_id(record) for record in response if verified_skills in record['verified_skills']]
        
        return self._process_response(response, search_term.lower())
    
    def _process_response(self, response, search_term):
        return sorted([self._get_score(record, search_term, response.__len__()) for record in response],
                       key=lambda x: x['score'],
                       reverse=True)
    
    def _rate2float(self, min_rate_str):
        if isinstance(min_rate_str, str):
            return float(min_rate_str.replace('$', '').replace(',', '.'))
        return min_rate_str
    
    def _search_id(self, obj):
        obj['_id'] = uuid4().__str__()
        return obj
    
    def _get_score(self, record, search_term, qs_count):
        occurrencies = 0
        for key in record.keys():
            if isinstance(record[key], str):
                occurrencies += record[key].lower().count(search_term)
        record['score'] = round(occurrencies / qs_count, 4)
        return record