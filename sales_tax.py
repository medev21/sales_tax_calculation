class read_file(object):
    def __init__(self, file):
        self.file = file

    def get_content(self):
        try:
            # return file contents
            # f = open(self.file, 'r') #opens file
            # file_contents = f.read()    #read contents of file
            # # print(file_contents)    #print contents in the terminal
            # f.close() #close the file

            # shorter way to open and close file
            with open(self.file) as f:
                # file_contents = f.read()
                file_lines = f.readlines()

            return file_lines

        except:
            # print error message
            print('something went wrong')

    def get_sales_tax(self):
        line = self.get_content()
        print(line)

    # def get_total_amount(self):
        # do something



tax_input1 = read_file('salesTaxInput1.txt')

# tax_input1.get_content()
tax_input1.get_sales_tax()
