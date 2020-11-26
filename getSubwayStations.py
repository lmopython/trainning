import urllib.request
import json
import sys, getopt

urlBase = 'https://api-ratp.pierre-grimaud.fr/v4/stations/metros/'
##Example : result with de url https://api-ratp.pierre-grimaud.fr/v4/stations/metros/3b
#{
#    "result": {
#        "stations": [
#            {
#                "name": "Porte des Lilas",
#                "slug": "porte+des+lilas"
#            },
#            {
#                "name": "Saint-Fargeau",
#                "slug": "saint+fargeau"
#            },
#            {
#                "name": "Pelleport",
#                "slug": "pelleport"
#            },
#            {
#                "name": "Gambetta",
#                "slug": "gambetta"
#            }
#        ]
#    },
#    "_metadata": {
#        "call": "GET /stations/metros/3b",
#        "date": "2019-06-02T20:07:24+02:00",
#        "version": 4
#    }
#}


def response(url):
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        return response.read()


def main(argv):
    number=""
    if len(argv) <= 1:
       print (argv[0] +' -n <Subway Line Number>')
       sys.exit(2)

    try:
       opts, args = getopt.getopt(argv[1:],"hn:",["help", "number="])
    except getopt.GetoptError:
       print (argv[0] +' -n <Subway Line Number>')
       sys.exit(2)
    for opt, arg in opts:
       if opt in ('-h', '--help'):
          print (argv[0] +' -n <Subway Line Number>')
          sys.exit()
       elif opt in ('-n', '--number'):
          number = arg



    res = response(urlBase+number)

    ##parsing response
    cont = json.loads(res.decode('utf-8'))

    counter = 0
    ##parcing json
    for item in cont['result']['stations']:
        counter += 1
        print("Name:", item['name'], "\n")

    ##print formated
    #print (json.dumps(cont, indent=4, sort_keys=True))
    print("Number of stations: ", counter)



if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv)

