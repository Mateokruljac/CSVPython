import csv

class PythonCSVConverter:
    
    def __init__ (self,first_csv_file,second_csv_file):
        """
        This init function receive two csv file as parmater.
        Carrier-plans.csv and resale-plans.csv
        Args:
            first_csv_file(carrier-plans.csv)
            second_csv_file(resale-plans.csv) 
        """
        self.first_csv_file = first_csv_file
        self.second_csv_file = second_csv_file

        
    def load_data_carrier_plans(self):
        carrier_plans_body = []
        with open(self.first_csv_file) as carrier_plans:
            carrier_plans_data = csv.reader(carrier_plans,delimiter = ",") #columns are separated by comma
            # next(carrier_plans_data) # skip a header
            carrier_plans_header = {"customer":0,"mdn":1,"sprint_plan":2,"socs":3}
            for row in carrier_plans_data:
                carrier_plans_body.append(row)
            
        return carrier_plans_header,carrier_plans_body
      
      
    def load_data_resale_plans(self):
        resale_plans_body = []
        with open(self.second_csv_file) as resale_plans:
            resale_plans_data = csv.reader(resale_plans,delimiter = ",") #columns are separated by comma
            next(resale_plans_data) # skip a header
            # get header
            resale_plans_header = {"mdn":0,"resale_plan":1}
            
            #get body
            for row in resale_plans_data:
                resale_plans_body.append(row)
        return resale_plans_header,resale_plans_body
            
                       
    def first_case(self):
        """ 
        it is necessary to create a File with all related data and fields: 
        MDN, Resale Plan, Sprint Plan and SOCs.
        """
        resale_plans_header, resale_plans_body = self.load_data_resale_plans()
        carrier_plans_header, carrier_plans_body = self.load_data_carrier_plans()
        #get mdn 
        mdn = []
        for x in resale_plans_body[0:len(resale_plans_body)-1]:
            mdn.append(x[0])
        final_list = []
        counter = 0
        for number in mdn:
            for row_c in carrier_plans_body:
                for row_p in resale_plans_body: 
                  if number in row_c and number in row_p: 
                    final_list.append([row_c[carrier_plans_header["sprint_plan"]],row_c[carrier_plans_header["socs"]],row_p[resale_plans_header["mdn"]],row_p[resale_plans_header["resale_plan"]]])
            counter +=1
            if counter == 5:
                break
        
        final_list.insert(0,["sprint plan","socs","MDN","resale plan"])           
        # print(final_list)
        
        #write data in new file
        with open("firstCase.csv","w") as write_data:
            write_data = csv.writer(write_data, delimiter = ",")
            
            for row in final_list:
                write_data.writerow(row)
                
                
                 
    def second_case(self):
        """ 
        it is necessary to create a file with related data and fields: 
        MDN, Resale Plan, Sprint Plan and the field 'LTE SOC' whose value
        is set to the value 'Y' or 'N', depending on whether the SOCs field
        in the input file contains the value ' DSMLTESOC'
        """
        resale_plans_header, resale_plans_body = self.load_data_resale_plans()
        carrier_plans_header, carrier_plans_body = self.load_data_carrier_plans()
        #get mdn 
        mdn = []
        for x in resale_plans_body[15:len(resale_plans_body)-1]:
            mdn.append(x[0])
        final_list = []
        counter = 0
        for number in mdn:
            for row_c in carrier_plans_body:
                for row_p in resale_plans_body: 
                  if number in row_c and number in row_p: 
                      if "DSMLTESOC" in  row_c[carrier_plans_header["socs"]]:
                         final_list.append([row_c[carrier_plans_header["sprint_plan"]],row_p[resale_plans_header["mdn"]],row_p[resale_plans_header["resale_plan"]],"Y"])
                      else:
                         final_list.append([row_c[carrier_plans_header["sprint_plan"]],row_p[resale_plans_header["mdn"]],row_p[resale_plans_header["resale_plan"]],"N"])
                      print(final_list)
            counter +=1
            if counter == 5:
                break
        
        final_list.insert(0,["sprint plan","MDN","resale plan","LTE SOC"])           
        # print(final_list)
        
        #write data in new file
        with open("secondCase.csv","w") as write_data:
            write_data = csv.writer(write_data, delimiter = ",")
            
            for row in final_list:
                write_data.writerow(row)
                
                
    
    def third_case(self):
        """ 
        it is necessary to create a file with the distribution of subscribers by resolution plan,
        how many subscribers are on which resolution plan.
        """
        
        resale_plans_header, resale_plans_body = self.load_data_resale_plans()
        carrier_plans_header, carrier_plans_body = self.load_data_carrier_plans()
        #get mdn 
        resale_plans = []
        for x in resale_plans_body[0:len(resale_plans_body)-1]:
            if x[1] not in resale_plans:
              resale_plans.append(x[1])
              
        # print("*"*21) 
        # print(resale_plans)
        
        resale_plans_sum = []
        counter = 0
        for x in resale_plans:
            for users in resale_plans_body[0:len(resale_plans_body)-1]:
                if x in users:
                    counter += 1
            resale_plans_sum.append(counter)
            counter = 0
        
        # print(resale_plans_sum)
        final_list = [list(a) for a in zip(resale_plans,resale_plans_sum)]
        
        final_list.insert(0,["resale plan","Num of Devices"])           
        # print(final_list)
        #write data in new file
        with open("thirdCase.csv","w") as write_data:
            write_data = csv.writer(write_data, delimiter = ",")
            
            for row in final_list:
                write_data.writerow(row)
                

                
#run                 
CSVPyConverter = PythonCSVConverter("carrier-plans.csv","resale-plans.csv")

CSVPyConverter.first_case()
CSVPyConverter.second_case()
CSVPyConverter.third_case()

