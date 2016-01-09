def open_file_extract_data(filename):
    cohort_data = open(filename)

    individual_info = []

    for item in cohort_data:
        new_item = item.rstrip()
        each_person = new_item.split('|')
        individual_info.append(each_person)

    cohort_data.close()

    return individual_info


         
def unique_houses():
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])

    """

    houses = set()

    for each_person in cohort_data:
        if each_person[2] != "":
            houses.add(each_person[2])

    return houses


def sort_by_cohort():
    """TODO: Sort students by cohort.

    Iterates over individual_info to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]

    """

    
    winter_15 = []
    spring_15 = [] 
    summer_15 = [] 
    tas = []
    all_students = [winter_15, spring_15, summer_15, tas]

    # Code goes here

    for each_person in cohort_data:
        full_name = each_person[0] + " " + each_person[1]
        if each_person[-1] == "TA":
            tas.append(full_name)
        elif each_person[-1] == "Winter 2015":
            winter_15.append(full_name)
        elif each_person[-1] == "Spring 2015":
            spring_15.append(full_name)
        elif each_person[-1] == "Summer 2015":
            summer_15.append(full_name)
    
    winter_15.sort()
    spring_15.sort()
    summer_15.sort()
    tas.sort()

    return all_students


def students_by_house():
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas"
    and instructors in to a list called "instructors".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. all_students = [ hufflepuff,
                        gryffindor,
                        ravenclaw,
                        slytherin,
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas,
                        instructors
            ]
    """

    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []
    instructors = []

    # all_students = [gryffindor, 
    #                 hufflepuff, 
    #                 slytherin, 
    #                 dumbledores_army, 
    #                 order_of_the_phoenix,
    #                 ravenclaw,
    #                 tas,
    #                 instructors]

    # Code goes here

    for each_person in cohort_data:
        if each_person[-1] == "TA":
            tas.append(each_person[1])
        elif each_person[-1] == "I":
            instructors.append(each_person[1])
        else:
            if each_person[2] == "Gryffindor":
                gryffindor.append(each_person[1])
            elif each_person[2] == "Hufflepuff":
                hufflepuff.append(each_person[1])
            elif each_person[2] == "Slytherin":
                slytherin.append(each_person[1])
            elif each_person[2] == "Dumbledore's Army":
                dumbledores_army.append(each_person[1])
            elif each_person[2] == "Order of the Phoenix":
                order_of_the_phoenix.append(each_person[1])
            elif each_person[2] == "Ravenclaw":
                ravenclaw.append(each_person[1])

    gryffindor.sort()
    hufflepuff.sort()
    slytherin.sort()
    dumbledores_army.sort()
    order_of_the_phoenix.sort()
    ravenclaw.sort()
    tas.sort()
    instructors.sort()


    #return all_students


def all_students_tuple_list():
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """

    student_list = []

    for each_person in cohort_data:
        full_name = each_person[0] + " " + each_person[1]
        student_list.append((full_name, each_person[2], each_person[3], each_person[4]))

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    # Code goes here

    student_name = raw_input("Student's full name: ")

    #all_students = all_students_tuple_list("cohort_data.txt")

    for i in range(len(student_list)):
        if student_list[i][0] == student_name and \
        student_list[i][-1] != "I" and \
        student_list[i][-1] != "TA":
            return student_list[i][-1]

    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates():
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Sarah"])

    """

    duplicate_names = set()

    # Code goes here

    winter_15 = set()
    spring_15 = set() 
    summer_15 = set() 

    for each_person in cohort_data:
        if each_person[-1] == "Winter 2015":
            winter_15.add(each_person[0])
        elif each_person[-1] == "Spring 2015":
            spring_15.add(each_person[0])
        elif each_person[-1] == "Summer 2015":
            summer_15.add(each_person[0])

    duplicates_1 = winter_15 & spring_15
    duplicates_2 = spring_15 & summer_15
    duplicates_3 = summer_15 & winter_15
    duplicate_names = duplicates_1 | duplicates_2 | duplicates_3


    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and returns everyone in their house that's in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function that,
    when given a student's first and last name, returns students that are in both that
    student's cohort and that student's house."""

    # Code goes here

    return


#########################################################################################

# Here is some useful code to run these functions!
cohort_data = open_file_extract_data("cohort_data.txt")
# print unique_houses()
# print sort_by_cohort()
print students_by_house()
# all_students_data = all_students_tuple_list("cohort_data.txt")
# print all_students_data
# print find_cohort_by_student_name(all_students_data)
# print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)
