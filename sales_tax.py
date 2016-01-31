# books, food, medical products are exempt, other products are taxed 10%
# imported items are taxed 5%

class read_file(object):

    def __init__(self, file):
        self.file = file

    def get_content(self):
        try:
            # shorter way to open and close file
            with open(self.file) as f:
                file_lines = f.readlines() #read each line

            return file_lines

        except:
            # print error message
            print('something went wrong')

    def get_sales_tax(self):
        lines = self.get_content()

        # for line in lines:

        print(lines)

    def calculate(self):

        lines = self.get_content()

        for line in lines:
            if self.is_imported(line):
                pass
        pass

    def is_imported(self, line): #takes line(a string) as param
        bool = False #start with false boolean
        split_line = line.split() #split line string into an array

        if any("imported" in s for s in split_line):  #check the array if contains imported
            bool = True #set boolean to true
        # print(bool)
        return bool

    def is_exempted(self, line):
        bool = False
        print(bool)
        return bool

    # def get_total_amount(self):
        # do something



tax_input1 = read_file('salesTaxInput1.txt')

# tax_input1.get_content()
tax_input1.is_imported("1 imported box of chocolates at 10.00")
