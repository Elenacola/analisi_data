from configparser import ConfigParser

def config(filename="database.ini", section="postgresql"):
    #create parsen 
    
    parsen = ConfigParser()
parsen.read(filename)

#itero sul nome del file e restituisco ogni elemento all'interno di qsto quindi creo un dizionario vuoto

db={}
if parsen.has_section(section):
    params =parser.items(section)
    for param in params:
        db[param[0]] = param [1]
else:
    raise Exception('Section{0}') is not found in {1}
    file.'.format(section,filename)
    
print (db)


config()


connection=psycopg2.connect(host='168.119.35.175', port='xxxx')
database="auto", user="candidato",password="xxxxx"
