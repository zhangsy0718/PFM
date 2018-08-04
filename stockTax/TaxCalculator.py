class TaxRecord:
    def __init__(self,data):
        self.id = data[0]
        self.name = data[1]
        self.stock = float(data[2])

    def getId(self):
        return self.id
    
    def getName(self):
        return self.name

    
    def getStock(self):
        return self.stock

class TaxInfo:
    def __init__(self, taxRecord):
        self.sum = taxRecord
        self.current = taxRecord
        self.tax = 0
    
    def addRec(self, taxRecord):
        self.current = taxRecord
        self.sum.stock += taxRecord.getStock()
    
    def getId(self):
        return self.sum.id

    def getName(self):
        return self.sum.name

    def calculator(self):
        taxRate1 = 0.2
        taxRate2 = 0.2
        self.tax = self.sum.stock * taxRate2 - (self.sum.stock - self.current.stock) * taxRate1
        return self.tax

    def getTax(self):
        return self.tax

    def __str__(self):
        return "sum:\nid:%s, name:%s: stock:%.2f\tcurrent: stock:%.2f\n" % \
            (self.sum.id,self.sum.name,self.sum.stock,self.current.stock)
class TaxCalculator:
    def __init__(self, params):
        self.records = {}
        self.params = params
        
    def addOneRecord(self, rec):
        if (rec.getId() in self.records.keys()):
            self.records[rec.getId()].addRec(rec)
        else:
            self.records[rec.getId()] = TaxInfo(rec)

    def output(self):
        outfn = "%s/%d_%02d_result.csv" % (self.params['dataDir'],self.params['year'],self.params['month'])
        print('write result into %s' % outfn)
        outf = open(outfn, "w")
        outf.write("%s,%s,%s\n" % ('id','name','tax'))
        for v in self.records.values():
            outf.write("%s,%s,%.2f\n" % (v.getId(), v.getName(), v.calculator()))
            #print(v)
        outf.close()