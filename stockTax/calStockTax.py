#encoding=gb2312
import sys
from getopt import *
from TaxCalculator import *

def getParameter(argv, params):
    if (len(argv)<2):
        return False
    params['year'] = int(argv[0])
    params['month'] = int(argv[1])
    if params['month'] <1 or params['month']>12:
        print('Error:month should between 1 and 12')
        return False
    try:
        opts, args = getopt(argv[2:], "p:")
    except GetoptError:
        return False
    
    for opt, arg in opts:
        if (opt == '-p'):
            params['dataDir'] = arg
        
    return True

def usage():
    print('''
        calStockTax <yyyy> <mm> [-p datadir]

        such as: 
            calStockTax 2018 03 
                计算2018年3月应交税款
            calStockTax 2018 03 -p data
                在data目录下查找数据文件
    '''
    )

def process(params, cal):
    for month in range(1, params['month']+1):
        fileName = "%s/%s_%02d.csv"  % (params['dataDir'],params['year'],month)
        #print('process file %s' % fileName)
        if (processOneFile(fileName, cal) == False):
            return False

def processOneFile(fn, cal):
    print('process file : %s' % fn)
    try:
        inf = open(fn)
    except IOError:
        print("can't open file : %s" % fn)
        return False
    for line in inf.readlines()[1:]:
        cal.addOneRecord(TaxRecord(line[:-1].split(',')))
    

if __name__ == '__main__':
    params = {'dataDir':'data'}
    if (getParameter(sys.argv[1:], params) == False):
        usage()
        sys.exit(-1);
    #print(params)
    cal = TaxCalculator(params)
    process(params, cal)
    cal.output()