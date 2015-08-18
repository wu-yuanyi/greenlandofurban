#-*- coding:utf-8 -*-

from http.server import BaseHTTPRequestHandler
import urllib.parse
import base
import greenland
import economy
import society
import total
import json


class GetHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        #print (parsed_path.query)
        
        Qc = 0.625
        Tc = 1024.125
        Qo2 = 1.667
        Po2 = 650
        tree = greenland.conifer_broadleaf['conandbro']
        R = 4
        P = 1317.3
        E = 697.4
        C = 0.2
        t = 0.038
        W = 0.012
        p = 0.462
        T = 600
        x1 = 0.6
        x2 = 0.3
        x3 = 0.1
        y1 = 0.4
        y2 = 0.15
        y3 = 0.45
        
        str_arg = parsed_path.query
        if not str_arg == '':
            print('*************************')
            list_arg = str_arg.split('&')
            list_to_dict = []
            for item in list_arg:
                list_to_dict.append(item.split('='))
            dict_arg = {}
            for item in list_to_dict:
                dict_arg[item[0]] = item[1]

            Qc = float(dict_arg['Qc'])
            Tc = float(dict_arg['Tc'])
            Qo2 = float(dict_arg['Qo2'])
            Po2 = float(dict_arg['Po2'])
            tree = greenland.conifer_broadleaf[dict_arg['tree']]
            R = float(dict_arg['R'])
            P = float(dict_arg['P'])
            E = float(dict_arg['E'])
            C = float(dict_arg['C'])
            t = float(dict_arg['t'])
            W = float(dict_arg['W'])
            p = float(dict_arg['p'])
            T = float(dict_arg['T'])
            x1 = float(dict_arg['x1'])
            x2 = float(dict_arg['x2'])
            x3 = float(dict_arg['x3'])
            callback = dict_arg['callback']

        #print (type(Qc))
        #print (type(Tc))
        #print (type(Qo2))
        #print (type(Po2))


        result1=total.urban_greenland_ecology(Qc , Tc , Qo2, Po2, tree, \
                                              R, P, E,C, t, W, p, T)
        result2=total.urban_greenland_economy(x1, x2, x3)
        result3=total.urban_greenland_society()
        result4=total.urban_greenland_complex(y1, y2 ,y3)
        
        RESULT=[result1,result2,result3,result4]
        json_result = json.dumps(RESULT)
        json_result = callback + '({"data":' + json_result + '})'
        json_result = json_result.encode('utf-8')
       
        #json_result='{"data":1}'.encode('utf-8') 
        
        self.wfile.write(json_result)
        
        return

    #def do_SPAM(self):
        
if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('127.0.0.1', 8080), GetHandler)
    print ('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
    GetHandler.do_Get()
