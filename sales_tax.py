# books, food, medical products are exempt, other products are taxed 10%
# imported items are taxed 5%

# import pdb; pdb.set_trace()


class Sales_Tax(object):

    def __init__(self, file):
        self.file = file
        self.import_tax = 0.05
        self.nonexemp_tax = 0.10

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
        tax_arr = [] #empty tax array
        for line in self.get_array_lines():
            tax_arr.append(self.calculate_tax(line)) #added calulated taxes in array

        # import pdb; pdb.set_trace()
        return tax_arr #return tax arrays

    def get_total_amount(self):
        amount_arr = []
        for line in self.get_array_lines():
            amount_arr.append(self.calculate_amount(line)) #added calulated taxes in array

        total_amount = map(sum, zip(amount_arr, self.get_sales_tax()))

        return total_amount #return tax arrays

    def calculate_amount(self, line):
        # split_line = line.split() #split the line into an array
        # product_price = float(split_line[len(split_line) - 1]) #get last item in the array

        product_price = self.get_contents_from_line(line)

        import pdb; pdb.set_trace()
        return product_price

    def calculate_tax(self, line):
        split_line = line.split()
        quantity = int(split_line[0]) #get first item in the array
        product_price = float(split_line[len(split_line) - 1]) #get last item in the array
        if self.is_imported(line) and not self.is_exempted(line):
            sales_tax = quantity * product_price * (self.import_tax + self.nonexemp_tax)#sales_tax is a float type
        elif self.is_imported(line):
            sales_tax = quantity * product_price * self.import_tax
        elif not self.is_exempted(line):
            sales_tax = quantity * product_price * self.nonexemp_tax
        else:
            sales_tax = 0
        return sales_tax

    def is_imported(self, line): #takes line(a string) as param
        bool = False #start with false boolean
        split_line = line.split() #split line string into an array

        if any("imported" in s for s in split_line):  #check the array if contains imported
            bool = True #set boolean to true
        # print(bool)
        return bool

    def is_exempted(self, line):
        bool = False
        exempt_products = ["chocolates", "chocolate", "pills", "book"]

        for product in exempt_products:
            if product in line:
                bool = True

        # import pdb; pdb.set_trace()
        return bool

    def get_array_lines(self):
        lines = self.get_content()  #call get_content method for file_lines

        return lines #return each line in an array

    def get_contents_from_line(self, line):
        # lines = self.get_content()

        # for line in lines:
        #     split_line = line.split()
        #     quantity = int(split_line[0]) #first item is qty
        #     description = ' '.join(split_line[1:-1]) #decription, remove first and last item
        #     price = float(split_line[len(split_line) - 1])  #last item is the price

        split_line = line.split()
        quantity = int(split_line[0]) #first item is qty
        description = ' '.join(split_line[1:-1]) #decription, remove first and last item
        price = float(split_line[len(split_line) - 1])  #last item is the price

        import pdb; pdb.set_trace()

        return quantity, description, price

    


    # def check_line(self):
    #
    #     for line in self.get_array_lines():
    #         if self.is_imported(line):
    #             return calculate_tax(line)
    #             # pass
    #     pass



tax_input1 = Sales_Tax('salesTaxInput3.txt')

# tax_input1.get_single_lines()
# tax_input1.get_content()
# tax_input1.is_imported("1 imported box of chocolates at 10.00")
# tax_input1.calculate_tax("1 imported box of chocolates at 10.00")
# tax_input1.get_sales_tax()
# tax_input1.is_exempted("1 imported box of chocolates at 10.00")
# tax_input1.get_total_amount()

tax_input1.calculate_amount("1 box of imported chocolates at 11.25")
