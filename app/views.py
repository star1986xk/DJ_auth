#!/usr/bin python3
# coding: utf-8
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
import requests
from rsa_class import rsa_class
import base64

class testApi(ModelViewSet):

    def get(self, request, *args, **kwargs):
        rsa_obj = rsa_class()
        pub = b'-----BEGIN RSA PUBLIC KEY-----\nMIGPAoGHMWGkl/NQ36tB4waykokDK/vlFmqYv/eqODyWc104aujfpjrkgBnAuWHd\nOAfwMMvJJk3ubrLwgLjZhei338E7+CGEsaNetWhO2Swg1iSNozEA9kXuH2PUxXUW\nXqmTxKrAuHSLzX/BGOhe/QcrdJ0ySfNFCtQuPETx4/g8CFnwvGn1BzcouLXpAgMB\nAAE=\n-----END RSA PUBLIC KEY-----\n'
        pri = b'-----BEGIN RSA PRIVATE KEY-----\nMIICfgIBAAKBhzFhpJfzUN+rQeMGspKJAyv75RZqmL/3qjg8lnNdOGro36Y65IAZ\nwLlh3TgH8DDLySZN7m6y8IC42YXot9/BO/ghhLGjXrVoTtksINYkjaMxAPZF7h9j\n1MV1Fl6pk8SqwLh0i81/wRjoXv0HK3SdMknzRQrULjxE8eP4PAhZ8Lxp9Qc3KLi1\n6QIDAQABAoGHJiU4IMyq32yKY9XroXhHQ/W8PDmxrzCgg/qBebI7/5HOGbmKg03h\naxKm8T5okzkINBelJEwDrlucZG2lhCnfnxUyxkjZv9fZXbc//4LTX9/kvr+PzCuE\nU0eeQ6q2qZRCiI4Qv4zdVz59WQJMfVwGKiFhcuJc4vn6cOeaKC9nstDsDg2OUoyF\nAkgOf36T6o8sqJ2yvSudTlvT58U4Y6yPAUxdiEwajUn2ByGL8pTEp+jKQgzAmqDg\nScQJrEoRNCcXqCbe6YeLeXebU5vLNosbznsCQANn9MmMOBBzmuhSWYCor609mt9W\nFRsi93FLZtGPhH1HholMAXiszut96BtkkSrKqwQD8yUspJnyWrePDp20EesCSAWi\nP5LFNEvbXiSF5DvlpkNrLjVibjzH+V/jRgePXe1QChYy9uKQiSKHliMGM3vUzmwf\n2kxjIsnLmwdGYlito+/lBoZqNJZinwJAAZxGjoFhBM5UYSKGtSGNJuFo985Q3mrT\nClt3ewBbyYxnHUW1sGQs1gXLGCCdztjSsWxYq6wHC88ee4oFhCVfDwJICEObaKKY\nMPNKR6PXdZAltHimQfrm8lXNcKOJDqmT3Ee8xfbqRCrtdC6/p9IVajBvetIMMZT6\nyE6f9dB6NCFjjyfQ2U7zBapN\n-----END RSA PRIVATE KEY-----\n'

        response = requests.get('http://quan.suning.com/getSysTime.do')
        tmp = response.json()['sysTime1'][:12]
        tmp = rsa_obj.encrypt(tmp,pub)
        return Response({'tmp': tmp})
