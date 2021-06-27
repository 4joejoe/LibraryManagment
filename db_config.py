from configparser import ConfigParser
from filepath import filepath
def config(section='postgresql'):
    parser = ConfigParser()
    file = filepath()
    parser.read(file)
    db={}
    if parser.has_section(section):
        params=parser.items(section)
        for param in params:
            db[param[0]]=param[1]
    # return if param is not listed in ini file
    else:
        raise Exception('Section {0} is not found in {1} file'.format(section,file))
    return db
