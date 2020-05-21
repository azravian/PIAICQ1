# Input Data
labels = ['gender', 'parental level of education', 'test preparation course', 'math score', 'reading score', 'writing score']

data = [ 
   ['female', "bachelor's degree", 'none', '72', '72', '74'], 
  ['female', 'some college', 'completed', '69', '90', '88'], 
  ['female', "master's degree", 'none', '90', '95', '93'], 
  ['male', "associate's degree", 'none', '47', '57', '44'], 
  ['male', 'some college', 'none', '76', '78', '75'], 
  ['female', "associate's degree", 'none', '71', '83', '78'], 
  ['female', 'some college', 'completed', '88', '95', '92'], 
  ['male', 'some college', 'none', '40', '43', '39'], 
  ['male', 'high school', 'completed', '64', '64', '67'], 
  ['female', 'high school', 'none', '38', '60', '50'], 
  ['male', "associate's degree", 'none', '58', '54', '52'], 
 ['male', "associate's degree", 'none', '40', '52', '43'], 
 ['female', 'high school', 'none', '65', '81', '73'], 
 ['male', 'some college', 'completed', '78', '72', '70'], 
 ['female', "master's degree", 'none', '50', '53', '58'], 
 ['female', 'some high school', 'none', '69', '75', '78'], 
 ['male', 'high school', 'none', '88', '89', '86'], 
 ['female', 'some high school', 'none', '18', '32', '28'], 
 ['male', "master's degree", 'completed', '46', '42', '46'], 
 ['female', "associate's degree", 'none', '54', '58', '61'], 
 ['male', 'high school', 'none', '66', '69', '63'], 
 ['female', 'some college', 'completed', '65', '75', '70'], 
 ['male', 'some college', 'none', '44', '54', '53'], 
 ['female', 'some high school', 'none', '69', '73', '73'], 
 ['male', "bachelor's degree", 'completed', '74', '71', '80'], 
 ['male', "master's degree", 'none', '73', '74', '72'], 
 ['male', 'some college', 'none', '69', '54', '55'], 
 ['female', "bachelor's degree", 'none', '67', '69', '75'], 
 ['male', 'high school', 'none', '70', '70', '65'], 
 ['female', "master's degree", 'none', '62', '70', '75'], 
 ['female', 'some college', 'none', '69', '74', '74'], 
 ['female', 'some college', 'none', '63', '65', '61'], 
 ['female', "master's degree", 'none', '56', '72', '65'], 
 ['male', 's6ome college', 'none', '40', '42', '38'], 
 ['male', 'some college', 'none', '97', '87', '82'], 
 ['male', "associate's degree", 'completed', '81', '81', '79'], 
 ['female', "associate's degree", 'none', '74', '81', '83'], 
 ['female', 'some high school', 'none', '50', '64', '59'], 
 ['female', "associate's degree", 'completed', '75', '90', '88'], 
]
#########################
#Q1 Solution

def females_vs_males(scoreColumn):
    femalesScoreSum    = 0
    malesScoreSum    = 0
    if scoreColumn > 2 and scoreColumn <6:
        for innerList in data:
            if innerList[0] == 'female':
                femalesScoreSum += int(innerList[scoreColumn])
            else:
                malesScoreSum += int(innerList[scoreColumn])
    else:
        print("Invalid Entry...")
    
    ############
    #Decision Making
    print("Females Score Total =", femalesScoreSum, " Male Score Total =", malesScoreSum) 

    if femalesScoreSum > malesScoreSum:
        print("Female performance is better than Males in ", labels[scoreColumn])
    elif femalesScoreSum < malesScoreSum:
        print("Males performance is better than Females in ", labels[scoreColumn])
    else:
        print("Same level of performance", labels[scoreColumn])


def Master_Parental_Degree(scoreColumn):
    masterScoreSum    = 0
    otherScoreSum    = 0
    if scoreColumn > 2 and scoreColumn <6:
        for innerList in data:
            if innerList[1] == "master's degree":
                masterScoreSum += int(innerList[scoreColumn])
            else:
                otherScoreSum += int(innerList[scoreColumn])
    else:
        print("Invalid Entry...")
    
    ############
    #Decision Making
    print("Student with Master's Parental degrees Total =", masterScoreSum)
    print("Student with other Parental degrees Total =", otherScoreSum) 

    if masterScoreSum > otherScoreSum:
        print("Student whose parents have master's degree has better performance than other in ", labels[scoreColumn])
    elif masterScoreSum < otherScoreSum:
        print("Student whose parents have master's degree doesn't has better performance than other in ", labels[scoreColumn])
    else:
        print("Same level of performance", labels[scoreColumn])


def Bachelors_Parental_Degree(scoreColumn):
    BachelorScoreSum    = 0
    otherScoreSum    = 0
    if scoreColumn > 2 and scoreColumn <6:
        for innerList in data:
            if innerList[1] == "bachelor's degree":
                BachelorScoreSum += int(innerList[scoreColumn])
            else:
                otherScoreSum += int(innerList[scoreColumn])
    else:
        print("Invalid Entry...")
    
    ############
    #Decision Making
    print("Student with Bachelor's Parental degrees Total =", BachelorScoreSum)
    print("Student with other Parental degrees Total =", otherScoreSum) 

    if BachelorScoreSum > otherScoreSum:
        print("Student whose parents have bachelor's degree has better performance than other in ", labels[scoreColumn])
    elif BachelorScoreSum < otherScoreSum:
        print("Student whose parents have bachelor's degree doesn't has better performance than other in ", labels[scoreColumn])
    else:
        print("Same level of performance", labels[scoreColumn])


def Degree_Count(scoreColumn):
    MastersDegree = 0
    BachelorsDegree = 0
    SomeCollegeDegree = 0
    for innerList in data:
        if innerList[1] == "master's degree":
            MastersDegree += 1
        elif innerList[1] == "bachelor's degree":
            BachelorsDegree += 1
        elif innerList[1] == "some college":
            SomeCollegeDegree += 1
        
    print("Numbers of parents with master's degree: ", MastersDegree)
    print("Numbers of parents with bachelor's degree: ", BachelorsDegree)
    print("Numbers of parents with Some college degree: ", SomeCollegeDegree)    
    

def Gender_of_Topper(scoreColumn):
    maxNum = 0
    StudentWithMaxMarks = []
    for student in data:
        if int(student[scoreColumn]) > maxNum:
            maxNum = int(student[scoreColumn])
            StudentWithMaxMarks = student.copy()
    
    if StudentWithMaxMarks[0] == "female":
        print("The highest marks obtained a female.")
    elif StudentWithMaxMarks[0] == "male":
        print("The highest marks obtained a male.")

def CompareReadingWriting():
    #how many students have good in reading (> 75) but not good in writing( < 70)
    NumOfStudent = 0
    for student in data:
        if int(student[4]) > 75 and int(student[5]) < 70:
            NumOfStudent += 1 

    print(f"{NumOfStudent} students have good in reading (> 75) but not good in writing( < 70)")

    
    

# Processing

ScoreColumn = int(input("score Column (3= math,4=reading 5= writing): "))

# Females vs Males comparison
print("="*120, end= " ")
print(end="\n\n")

print("Analyze based on Gender")
females_vs_males(ScoreColumn)

print(end="\n\n")

# Parental Master's degree analysis
print("="*120, end= " ")
print(end="\n\n")

print("Analysis based on Master's parental degree")
Master_Parental_Degree(ScoreColumn)

print(end="\n\n")

# bachelor's degree analysis
print("="*120, end= " ")
print(end="\n\n")

print("Analysis based on Bachelor's parental degree")
Bachelors_Parental_Degree(ScoreColumn)


print(end="\n\n")

# Degree Count
print("="*120, end= " ")
print(end="\n\n")

print("Counting Parental Degree")
Degree_Count(ScoreColumn)

print(end="\n\n")


# Gender of Highest Marks
print("="*120, end= " ")
print(end="\n\n")

print("Finding Topper's Gender")
Gender_of_Topper(ScoreColumn)

print(end="\n\n")


# how many students have good in reading (> 75) but not good in writing( < 70)
print("="*120, end= " ")
print(end="\n\n")

print("Finding no. of students good in reading (>75) but not good in writing(<70)")
CompareReadingWriting()

print(end="\n\n")


