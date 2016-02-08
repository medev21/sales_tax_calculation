# books, food, medical products are exempt, other products are taxed 10%
# imported items are taxed 5%

# import pdb; pdb.set_trace()
import sys

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
            print('something went wrong')   #print error message

    def write_results(self):
        name = "salesTaxOutput3.txt"
        try:
            file = open(name, 'w')

            for line in self.get_output():
                file.write(line +  "\n")

            file.close()

        except:
            print('Something went wrong! Can\'t tell what?')
            sys.exit(0) # quit Python

    def get_sales_tax(self):
        tax_arr = [] #empty tax array
        for line in self.get_array_lines():
            tax_arr.append(round(self.calculate_tax(line), 2)) #added calulated taxes in array

        # import pdb; pdb.set_trace()

        return tax_arr #return tax arrays

    def get_sum_of_taxes(self):
        tax_sum = 0
        for tax in self.get_sales_tax():
            tax_sum += tax

        import pdb; pdb.set_trace()

        return tax_sum

    def get_total_amount(self):
        amount_arr = []
        for line in self.get_array_lines():
            amount_arr.append(self.get_price(line)) #added calulated taxes in array

        total_amount = map(sum, zip(amount_arr, self.get_sales_tax()))

        return total_amount #return each product price w/ tax - array

    def get_output(self):
        output = [] #empty output array
        i = 0 #start a zero for loop
        for line in self.get_array_lines():
            output.append(str(self.get_quantity(line)) + " "+ self.get_description(line) + ": " + str(self.get_total_amount()[i]))
            i += 1

        return output

    def calculate_tax(self, line):
        description = self.get_description(line)
        quantity = self.get_quantity(line)
        product_price = self.get_price(line)

        if self.is_imported(description) and not self.is_exempted(description):
            sales_tax = quantity * product_price * (self.import_tax + self.nonexemp_tax)#sales_tax is a float type
        elif self.is_imported(description):
            sales_tax = quantity * product_price * self.import_tax
        elif not self.is_exempted(description):
            sales_tax = quantity * product_price * self.nonexemp_tax
        else:
            sales_tax = 0

        return sales_tax

    def is_imported(self, line): #takes line(a string) as param
        bool = False #start with false boolean

        if "imported" in line:  #if imported is in the sentence
            bool = True

        return bool

    def is_exempted(self, line):
        bool = False
        exempt_products = ["chocolates", "chocolate", "pills", "book"]

        for product in exempt_products:
            if product in line:
                bool = True

        return bool

    def get_array_lines(self):
        lines = self.get_content()  #call get_content method for file_lines

        return lines #return each line in an array

    def get_contents_from_line(self, line):

        split_line = line.split() #splint string into an array
        quantity = int(split_line[0]) #first item is qty
        description = ' '.join(split_line[1:-2]) #decription, remove first and last item
        price = float(split_line[len(split_line) - 1])  #last item is the price

        return quantity, description, price

    def get_quantity(self, line):

        return self.get_contents_from_line(line)[0] #returns an int

    def get_description(self, line):

        return self.get_contents_from_line(line)[1] #returns a string


    def get_price(self, line):

        return self.get_contents_from_line(line)[2] #returns a float



##############################################################################


tax_input1 = Sales_Tax('salesTaxInput3.txt')

# tax_input1.get_single_lines()
# tax_input1.get_content()
# tax_input1.is_imported("1 imported box of chocolates at 10.00")
# tax_input1.calculate_tax("1 imported box of chocolates at 10.00")
# tax_input1.get_sales_tax()
# tax_input1.is_exempted("1 imported box of chocolates at 10.00")
# tax_input1.get_total_amount()
# tax_input1.get_output("1 imported box of chocolates at 10.00")
# tax_input1.get_output()
# tax_input1.write_results()
tax_input1.get_sum_of_taxes()
