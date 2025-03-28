import os 
import random
from timeit import default_timer as timer


def generateData(file_path,size,max_value):
    with open(file_path,"w") as file_out:
        for i in range(size-1):
            number = random.randint(1,max_value)
            file_out.write(str(number)+"\n")
            if i % 100_00 == 0:
                print(f"{i} of {size}")
        number = random.randint(1,max_value)
        file_out.write(str(number))


def divide_file(file_path,size,working_directory):
    with open(file_path,"r") as file_data:
        file_number = 1
        end = False

        while not end:
            file_out_name = f"data_{file_number}.dat"
            file_out_path = os.path.join(working_directory,file_out_name)
            file_number+=1
            counter = 0

            line = file_data.readline().strip()
            if not line:
                break
            with open(file_out_path,"w") as file_out:
                file_out.write(line)
                counter +=1

                while counter < size:
                    line = file_data.readline().strip()
                    if not line:
                        end = True 
                        break
                    file_out.write("\n"+line)
                    counter+=1
            if file_number % 10 == 0:
                print(f"{file_number} of {size}")

def getAllFilesInDirectory(working_directory):
    files=[]
    for file in os.listdir(working_directory):
        file_path = os.path.join(working_directory,file)

        if not os.path.isdir(file_path):
            files.append(file)

    return files
def sortDataInDirectory(working_directory):
    files = getAllFilesInDirectory(working_directory)
    c = 1
    nuberOfFiles = len(files)
    for file in files:
        file_path = os.path.join(working_directory,file)
        data = None 
        with open(file_path,"r") as source_file:
            data = [int(line.strip()) for line in source_file]
        data.sort()
        with open(file_path,"w") as result_file:
            for i in range(len(data)-1):
                result_file.write(str(data[i])+"\n")
            result_file.write(str(data[-1]))
        if c % 10 == 0:
            print(f"{c} of {nuberOfFiles}")
        c+=1

def merge_two_file(working_directory,file_in_1_name,file_in_2_name,file_out_name):
    file_in_1_path = os.path.join(working_directory,file_in_1_name)
    file_in_2_path = os.path.join(working_directory,file_in_2_name)
    file_out_path = os.path.join(working_directory,file_out_name)

    with open(file_in_1_path,"r") as file_in_1:
        with open(file_in_2_path,"r") as file_in_2:
            with open(file_out_path,"w") as file_out:
                line_1 = file_in_1.readline().strip()
                line_2 = file_in_2.readline().strip()

                while True:
                    if line_1 and line_2:
                        v1 = int(line_1)
                        v2 = int(line_2)

                        if v1 < v2:
                            file_out.write(str(v1))
                            line_1 = file_in_1.readline().strip()
                        else:
                            file_out.write(str(v2))
                            line_2 = file_in_2.readline().strip()
                    elif line_1 and not line_2:
                        file_out.write(line_1)
                        line_1 = file_in_1.readline().strip()
                    elif not line_1 and line_2:
                        file_out.write(line_2)
                        line_2 = file_in_2.readline().strip()
                    else:
                        break
                    if line_1 or line_2:
                        file_out.write("\n")



def mergeOneIteration(working_directory,files,iteration,removeSourveFiles =True):
    dim = 2
    list_of_pairs = [files[i:i+dim]for i in range(0,len(files),dim)]
    p = 1 
    for pair in list_of_pairs:
        if len(pair)==dim:
            file_in_1_name = pair[0]
            file_in_2_name = pair[1]
            file_out_name = f"{iteration}_{p}.dat"
            merge_two_file(working_directory,file_in_1_name,file_in_2_name,file_out_name)
        else:
            path_current = os.path.join(working_directory,pair[0])
            path_new = os.path.join(working_directory,f"{iteration}_{p}.dat")
            os.rename(path_current,path_new)
        p +=1

    if removeSourveFiles:
        for file in files:
            file_path = os.path.join(working_directory,file)
            if not os.path.isdir(file_path):
                if os.path.exists(file_path):
                    os.remove(file_path)

def merge_all_files(working_directory):
    files = getAllFilesInDirectory(working_directory)
    numberOfFiles = len(files)
    iteration = 1
    safe = 10 

    while (numberOfFiles > 1 and safe>0):
        safe -=1
        mergeOneIteration(working_directory,files,iteration,True)
        files = getAllFilesInDirectory(working_directory)
        numberOfFiles = len(files)
        iteration +=1


# def computeTwoFiles(file_name_1,file_name_2):
#     counter_1 =0
#     counter_2 = 0
    
#     file_name_1 = os.path.join("/home/u335867/Pulpit/semIV/BigData/source/", file_name_1)
#     file_name_2 = os.path.join("/home/u335867/Pulpit/semIV/BigData/source/",file_name_2)

#     print(file_name_1)

#     num_count = defaultdict(int)
#     with open(file_name_1,"r") as file:
#         for line in file:
#             number = line.strip()
#             num_count["number"] = counter_1 + 1 
            
            
            
#     with open(file_name_2,"r") as file:
#         for line in file:
#             counter_2+=1
#     if counter_2 == counter_1:
#         print("True")
#         return True
#     print("false")
#     return False




def main():
     begin = timer()
    # generateData("data.dat",50_000,2_000)
     end = timer()
    # print(f"Czas generowania: {end - begin}")


    # begin = timer()
    # divide_file("data.dat",1_000,"work")
    # end = timer()
    # print(f"Czas dzielenia {end - begin}")

    # begin = timer()
    # sortDataInDirectory("work")
    # end = timer()
    # print(f"Czas sortowania {end - begin}")
    # #merge_two_file("work","data_1.dat","data_2.dat","data_1_2.dat")
    # begin = timer()
    # merge_all_files("work")
    # end=timer()
    # print(f"Czas scalania: {end - begin}")

   # computeTwoFiles("data.dat","work/6_1.dat")

if __name__ == "__main__":
    main()