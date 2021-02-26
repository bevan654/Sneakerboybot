import requests
import json
import time

#7nvpkr0w:IoaYztfBXSPu9FJA_country-Australia_session-FBeTBy9S@34.193.87.244:31112


#username:password@ip:port
#https://iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-PWuQYJzd@proxy.btwproxy.io:8080

proxies = [
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-282YM4BS',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-elGyWsZF',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-CfaiDnft',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-gWTlgiIu',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-hXZvpTBi',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-fWva4JtS',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-xCv6Qzt8',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-YIfJgXez',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-s23eFSYj',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-sX7lfHw9',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-LRxCzyhP',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-C3p1SJB7',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-EmagQWOM',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-a6f24LtG',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-28B3GOpC',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-0Oz4kvMM',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-nz7crrrj',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-y1tRwfPz',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-FzS56CDU',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-mZrh5tTu',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-Y3xT6jED',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-IdLaa1qP',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-ufysjPFI',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-ruMRju58',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-kEzhyrmj',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-fiqjEp8H',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-KqPUxmPl',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-ckoJNs3v',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-xlciQYiq',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-zda7NiOL',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-Q282AYCV',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-GR3iZWGH',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-H1jxN5gr',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-fEqFXWQo',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-xm5umeFy',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-K2lDoPgo',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-JpnKJI15',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-cIJiXzKi',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-zSf6k5nj',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-baxJNDYy',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-JdTRYOqA',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-oUPL0xwP',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-o3r9dwQ7',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-Wvd8cPl3',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-IVFIB1nx',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-Kp3tGb7a',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-ljta4qBc',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-aFhmCrQb',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-6qrJ5cgC',
    'iiscaevhbtw:V8wUCKXl4OJsHdo3_country-Australia_session-lhRwvhJr'
]



def getProxy(rand):
    proxy = proxies[rand]

    return proxy