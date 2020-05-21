# Structure of CSV File
# Headers = [gender,parental level of education,test preparation course,math score,reading score,writing score]

import csv
from tkinter import filedialog


GENDER_COL = 0
PARENT_EDUCATION_LEVEL_COL = 1
TEST_PREPARATION_COL = 2
MATH_SUBJECT_COL = 3
READING_SUBJECT_COL = 4
WRITING_SCORE_COL = 5
File_Read = False
Quit= False

def Read_File(File_Path):
    """
    Args:
    File_Path: Path of File
    Open_Mode: File being opened for, (Default Value, "r")
    Returns:
    A List from CSV File
    """
    DataFromFile = [] 
    with open(File_Path) as CSV_DATAFile:
        DataFromFile = list(csv.reader(CSV_DATAFile))
        return DataFromFile[1:]

def FindAverage(Data_List, AVG_Column, Search_Column, Search_Key):
    """
    Analyzes the performance of specific gender in a particular subject
    Args:
    Data_List:      Data which can be used to find average.
    AVG_Column:     Which column to be used for average calculation.
    Search_Column:  Column to be taken as reference for average calculation.
    Search_Key:     used for sorting and finding average for specific value.
    Returns:
    Average_marks:  A tuple of Average, 
                    Average at 0 index is based on Search_Key
                    Avearge at 1 index is based on entries other than Search_Key
    """
    Sum_WRT_SearchKey = 0
    Sum_Except_SearchKey = 0

    count_WRT_SearchKey = 0
    count_Except_SearchKey = 0
    print(Search_Column, Search_Key)
    print("Avg Col.", AVG_Column)
    for each_Data in Data_List:
        if each_Data[Search_Column] == Search_Key:
            Sum_WRT_SearchKey += int(each_Data[AVG_Column])
            count_WRT_SearchKey += 1
        else:
            Sum_Except_SearchKey += int(each_Data[AVG_Column])
            count_Except_SearchKey += 1
    print(f"count: {count_WRT_SearchKey}, sum: {Sum_WRT_SearchKey}")
    Average_WRT_key = round((Sum_WRT_SearchKey / count_WRT_SearchKey), 2)
    Average_Except_key = round((Sum_Except_SearchKey / count_Except_SearchKey), 2) 
    return (Average_WRT_key, Average_Except_key)

def Analyze_Performace_Based_on_gender(Student_data, Gender, Subject):
    """
    Analyzes the performance of specific gender in a particular subject
    Args:
    Student_Data:   Data of students.
    Gender:         The required gender which is to be analyzed w.r.t to other gender
    Subject:        The Subject which is to be considered for analysation.
    Returns:
    """
    Opposite_of_GenderA = {"female":"male","male":"female"}
    Average_GenderA_Students, Average_GenderB_Students = FindAverage(Student_data[:], Subject, GENDER_COL, Gender)

    if Average_GenderA_Students > Average_GenderB_Students:
        print(f"""\tResult: 
        {Gender.title()} students perform better than {Opposite_of_GenderA[Gender.lower()]}s because the have higher average."
        The average of {Gender.title()}s is {Average_GenderA_Students:.2f} as compared to {Average_GenderB_Students:.2f} of {Opposite_of_GenderA[Gender.lower()]}s""")
    elif Average_GenderA_Students < Average_GenderB_Students:
        print(f"""\tResult:
        {Gender.title()} students didn't performed better than {Opposite_of_GenderA[Gender.lower()]}s because the have lower average.
        The average of {Gender.title()}s is {Average_GenderA_Students:.2f} as compared to {Average_GenderB_Students:.2f} of {Opposite_of_GenderA[Gender.lower()]}s""")
    else:
        print("Both gender have performed equally well.")    

def Analyze_Performace_Based_on_Parental_degree(Student_Data, degree, Subject):
    """
    Analyzes the performance on the basis of Parental Degree in a particular subject
    Args:
    Student_Data:   Data of students.
    degree:         Parental Degree
    Subject:        The Subject which is to be considered for analysation.
    Returns:
    """
    # CatA_Students: student whose parents have specified degree
    # CatB_Students: student whose parents have other degrees
    print("Subject: ",Subject)
    
    Average_CatA_Students, Average_CatB_Students = FindAverage(Student_Data[:], Subject, PARENT_EDUCATION_LEVEL_COL,degree)

    if Average_CatA_Students > Average_CatB_Students:
        print(f"""\tResult: 
        Students whose parents have {degree.title()} performed better than other students because the have higher average."
        The average of these student is {Average_CatA_Students:.2f} as compared to {Average_CatB_Students:.2f} of others""")
    elif Average_CatA_Students < Average_CatB_Students:
        print(f"""\tResult:
        Students whose parents have {degree.title()} didn't perform better than other students because the have higher average."
        The average of these student is {Average_CatA_Students:.2f} as compared to {Average_CatB_Students:.2f} of others""")
    else:
        print("Student have performed equally well.")

def Analyze_Performace_Based_on_Preparation(Student_Data, PreparationStatus, Subject):
    """
    Analyzes the performance on the basis of Parental Degree in a particular subject
    Args:
    Student_Data:   Data of students.
    degree:         Parental Degree
    Subject:        The Subject which is to be considered for analysation.
    Returns:
    """
    # CatA_Students: student who have completed preparation
    # CatB_Students: student who have not done preparation
    
    Average_CatA_Students, Average_CatB_Students = FindAverage(Student_Data[:], Subject, TEST_PREPARATION_COL, PreparationStatus)

    if Average_CatA_Students > Average_CatB_Students:
        print(f"""\tResult: 
        Students whose have {PreparationStatus} preparation performed better than other students because the have higher average."
        The average of these student is {Average_CatA_Students:.2f} as compared to {Average_CatB_Students:.2f} of others""")
    elif Average_CatA_Students < Average_CatB_Students:
        print(f"""\tResult:
        Students whose have {PreparationStatus} preparation didn't perform better than other students because the have higher average."
        The average of these student is {Average_CatA_Students:.2f} as compared to {Average_CatB_Students:.2f} of others""")
    else:
        print("Student have performed equally well.")

def FindHighestMarks():
    """
    Finds and print the student with highest marks
    Args:
    Returns:
    """
    max_Marks = 0
    student_with_Highest_Marks=[]
    if File_Read:
        print(("-" * 40))
        print("""Find Highest marks by subect
        Select Subect:
        1. For Math
        2. For Reading
        3. For writing""")
        
        Subject_Key = {1:3,2:4,3:5}
        print(("-" * 40),end="\n\n")
        #input desired Subject.
        Subject_Req = int(input("Select Sbject: ")) 
        if Subject_Req in Subject_Key.keys():
            Subject_Key = {1:3,2:4,3:5}
            for Each_students in Student_Data_Read:
                if max_Marks < int(Each_students[Subject_Key[Subject_Req]]):
                    max_Marks = int(Each_students[Subject_Key[Subject_Req]])
                    student_with_Highest_Marks = Each_students
            print(f"The highest marks are obtained by {student_with_Highest_Marks[0]} with a score of {max_Marks}")
        else:
            print("Invalid entry, Try again...")
    else:
        print("File Not read yet, please import your data first")


def performGenderBasedAnalysis():
    if File_Read:
        print(("-" * 40))
        print("""Analyzing performance of student based on subject
        1. For Female
        2. For Male""")
        print(("-" * 40),end="\n\n")
        # input gender choice
        Gender_req = input("Select gender: ")
        Genders = {"1":"female","2":"male",}
        print(("-" * 40))
        print("""Analyzing performance of student based on subject
        Select Subect
        3. For Math
        4. For Reading
        5. For writing""")
        print(("-" * 40),end="\n\n")
        #input desired Subject.
        Subject_Req = int(input("Select Sbject: ")) 
        if Gender_req in Genders.keys() and Subject_Req in [3,4,5]:
            Analyze_Performace_Based_on_gender(Student_Data_Read[:], Genders[Gender_req], Subject_Req)
        else:
            print("Invalid entry, Try again...")
    else:
        print("File Not read yet, please import your data first")

def performParentalDegreeBasedAnalysis():
    if File_Read:
        print(("-" * 40))
        print("""Analyzing performance of student based on Parental Degree
        1. Associate's Degree
        2. bachelor's degree 
        3. high School
        4. master's degree
        5. Some College
        6. Some High School""")
        degree_req= int(input("Enter your Choice: "))
        
        Degree_Keys = {
            1: "associate's degree",
            2: "bachelor's degree", 
            3: "high school",
            4: "master's degree",
            5: "some college",
            6: "Some high school"
        }
        
        print(("-" * 40),end="\n\n")
        print(("-" * 40))
        print("""
        Select Subect
        3. For Math
        4. For Reading
        5. For writing""")
        print(("-" * 40),end="\n\n")
        #input desired Subject.
        Subject_Req = int(input("Select Sbject: ")) 
        if degree_req in Degree_Keys.keys() and Subject_Req in [3,4,5]:
            Analyze_Performace_Based_on_Parental_degree(Student_Data_Read[:], Degree_Keys[degree_req],Subject_Req)
        else:
            print("Invalid entry, Try again...")
    else:
        print("File Not read yet, please import your data first")

def performPreparationBasedAnalysis():
    if File_Read:
        print(("-" * 40))
        print("""Analyzing performance of student based on Preparation
        1. Preparation Completed
        2. No Preparation""")
        print(("-" * 40),end="\n\n")
        # input gender choice
        Prep_req = input("Select gender: ")
        Prep_Keys = {"1":"completed","2":"none",}
        print(("-" * 40))
        print("""Select subject
        Select Subect
        3. For Math
        4. For Reading
        5. For writing""")
        print(("-" * 40),end="\n\n")
        #input desired Subject.
        Subject_Req = int(input("Select Sbject: ")) 
        if Prep_req in Prep_Keys.keys() and Subject_Req in [3,4,5]:
            Analyze_Performace_Based_on_Preparation(Student_Data_Read[:], Prep_Keys[Prep_req], Subject_Req)
        else:
            print("Invalid entry, Try again...")
    else:
        print("File Not read yet, please import your data first")


while not Quit:
    print(""" 
    1. Import Data From File.
    2. Analysis Based on Gender and Subject.
    3. Analysis Based on Parental Degree Level.
    4. Analysis Based on Preparation.
    5. Find Highest Marks by Subject.
    5. Enter Q to Quit "help" for help.
    """)

    operation=input("Enter the Required opetration: ")

    if operation.lower() == "q":
        Quit=True
    
    elif operation == "1":
        FilePath = filedialog.askopenfilename(title = "Select file")
        Student_Data_Read = Read_File(FilePath)
        if not Student_Data_Read == []:
            File_Read = True
            #print(Student_Data_Read)
        else:
            File_Read = False

    elif operation == "2":
        performGenderBasedAnalysis()  

    elif operation == "3":
        performParentalDegreeBasedAnalysis()

    elif operation == "4":
        performPreparationBasedAnalysis()

    elif operation == "5":
        FindHighestMarks()
    else:
        print("Invalid Entry.... Please Enter 4 for help")
        continue

