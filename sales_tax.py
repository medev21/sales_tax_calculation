class read_file(object):
    def __init__(self, file):
        self.file = file

    def read(self):
        try:
            # do something
            f = open(self.file, 'r') #opens file
            file_contents = f.read()    #read contents of file
            print(file_contents)
            f.close() #close the file
        except:
            # do something
            print('something went wrong')

    def get_sales_tax(self):
        # do something

    def get_total_amount(self):
        # do something 


tax_input1 = read_file('salesTaxInput1.txt')

tax_input1.read()
