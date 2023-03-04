

file_for_doctors = 'doctors.txt'
list_of_doctors = []

file_for_facilities = 'facilities.txt'
list_of_facilities = []

file_for_laboratories = 'laboratories.txt'
list_of_laboratories = []

file_for_patients = 'patients.txt'

# just pass the list from read method


# Doctor class has 6 attributes, 10 methods
class Doctor:

    def __init__(self, pid=-1, name='', specialization='', working_time='', qualification='', room_number=-1):
        if pid != -1:
            self.pid = pid
        if name != '':
            self.name = name
        if specialization != '':
            self.specialization = specialization
        if working_time != '':
            self.working_time = working_time
        if qualification != '':
            self.qualification = qualification
        if room_number != -1:
            self.room_number = room_number

    # formats each doctor's information (properties) in the same format used in the .txt file (has underscores between values)
    def formatDrInfo(self, txt_to_format):
        formatted = '_'.join(txt_to_format)
        return formatted


    # asks the user to enter doctor properties (listed in the properties point)
    def enterDrInfo(self):
        self.readDoctorsFile()
        self.pid = int(input("Enter the doctor’s ID: \n"))
        self.name = input("Enter the doctor’s name: \n")
        self.specialization = input("Enter the doctor’s speciality: \n")
        self.working_time = input("Enter the doctor’s timing (e.g., 7am-10pm): \n")
        self.qualification = input("Enter the doctor’s qualification: \n")
        self.room_number = int(input("Enter the doctor’s room number: \n"))
        list_of_doctors.append([str(self.pid), self.name, self.specialization, self.working_time, self.qualification, str(self.room_number)])
        self.addDrToFile([str(self.pid), self.name, self.specialization, self.working_time, self.qualification, str(self.room_number)])

    # reads from "doctors.txt" file and fills the doctor objects in a list
    def readDoctorsFile(self):
        file = open(file_for_doctors, 'r')
        for each_line in file:
            list_of_doctors.append(each_line.rstrip().split('_'))
        file.close()

    # searches whether the doctor is in the list of doctors/file using the doctor ID that the user enters
    def searchDoctorById(self):
        id_number = int(input("Enter the Doctor's ID: \n"))
        total_rows = len(list_of_doctors)
        current_row = 1
        last_row = total_rows - 1
        doctor_found = ''
        while current_row < total_rows:
            if str(id_number) == list_of_doctors[current_row][0]:
                print(f'{"ID":<5}' + f'{"Name":<15}' + f'{"Specialty":<15}' + f'{"Timing":<15}' + f'{"Qualification":<17}' + 'Room Number')
                print(f'{list_of_doctors[current_row][0]:<5}' + f'{list_of_doctors[current_row][1]:<15}' + f'{list_of_doctors[current_row][2]:<15}' + f'{list_of_doctors[current_row][3]:<15}' + f'{list_of_doctors[current_row][4]:<17}' + list_of_doctors[current_row][5])
                doctor_found = 'yes'
            if doctor_found != 'yes' and current_row == last_row:
                print("Can't find the doctor with the same ID on the system")
            current_row += 1


    # searches whether the doctor is in the list of doctors/file using the doctor name that the user enters
    def searchDoctorByName(self):
        search_doctor = input("Enter the Doctor's name: \n")
        total_rows = len(list_of_doctors)
        current_row = 1
        last_row = total_rows - 1
        doctor_found = ''
        while current_row < total_rows:
            compare_doctor = list_of_doctors[current_row][1]
            compare_doctor = compare_doctor.replace(' ', '').lower()
            search_doctor = search_doctor.replace(' ', '').lower()
            if search_doctor == compare_doctor:
                print(
                    f'{"ID":<5}' + f'{"Name":<15}' + f'{"Specialty":<15}' + f'{"Timing":<15}' + f'{"Qualification":<17}' + 'Room Number')
                print(
                    f'{list_of_doctors[current_row][0]:<5}' + f'{list_of_doctors[current_row][1]:<15}' + f'{list_of_doctors[current_row][2]:<15}' + f'{list_of_doctors[current_row][3]:<15}' + f'{list_of_doctors[current_row][4]:<17}' + list_of_doctors[current_row][5])
                doctor_found = 'yes'
            if doctor_found != 'yes' and current_row == last_row:
                print("Can't find the doctor with the same name on the system")
            current_row += 1

    # displays doctor information on different lines, as a list
    def displayDoctorInfo(self):
        for each_row in list_of_doctors:
            print(each_row)

    # asks the user to enter the ID of the doctor to change their information, and then the user can enter the new doctor information
    def editDoctorInfo(self):
        id_number = int(input("Please enter the id of the doctor that you want to edit their information: \n"))
        self.pid = id_number
        total_rows = len(list_of_doctors)
        current_row = 1
        last_row = total_rows - 1
        doctor_found = ''
        self.name = input("Enter new Name: \n")
        self.specialization = input("Enter new Specialist in: \n")
        self.working_time = input("Enter new Timing: \n")
        self.qualification = input("Enter new Qualification: \n")
        self.room_number = int(input("Enter new Room number: \n"))
        while current_row < total_rows:
            if str(id_number) == list_of_doctors[current_row][0]:
                list_of_doctors[current_row][1] = self.name
                list_of_doctors[current_row][2] = self.specialization
                list_of_doctors[current_row][3] = self.working_time
                list_of_doctors[current_row][4] = self.qualification
                list_of_doctors[current_row][5] = str(self.room_number)
                doctor_found = 'yes'
            if doctor_found != 'yes' and current_row == last_row:
                print("Can't find the doctor with the same ID on the system")
            current_row += 1
        self.writeListOfDoctorsToFile()


    # displays all the doctor's information, read from the file, as a report/table
    def displayDoctorsList(self):
        total_rows = len(list_of_doctors)
        current_row = 1
        print(f'{"ID":<10}' + f'{"Name":<15}' + f'{"Specialty":<15}' + f'{"Timing":<15}' + f'{"Qualification":<17}' + 'Room Number')
        while current_row < total_rows:
            print(f'{list_of_doctors[current_row][0]:<10}' + f'{list_of_doctors[current_row][1]:<15}' + f'{list_of_doctors[current_row][2]:<15}' + f'{list_of_doctors[current_row][3]:<15}' + f'{list_of_doctors[current_row][4]:<17}' + list_of_doctors[current_row][5])
            current_row += 1


    # writes the list of doctors to the doctors.txt file after formatting it correctly
    def writeListOfDoctorsToFile(self):
        self.readDoctorsFile()
        doctors_file = open(file_for_doctors, 'w')
        for each_line in list_of_doctors:
            line = each_line
            line = self.formatDrInfo(line)
            doctors_file.write(line)
            doctors_file.write('\n')
        doctors_file.close()

    # writes doctors to the doctors.txt file after formatting in correctly
    def addDrToFile(self, new_doctor):
        self.readDoctorsFile()
        doctors_file = open(file_for_doctors, 'a')
        add_line = self.formatDrInfo(new_doctor)
        doctors_file.write(add_line)
        doctors_file.write('\n')
        doctors_file.close()

# Facility class has 1 property and 3 methods
class Facility:
    def __init__(self, facility_name=''):
        if facility_name != '':
            self.facility_name = facility_name

    # adds and writes the facility to the file
    def addFacility(self):
        additional_facility = input("Enter Facility name: \n")
        facilities_file = open('facilities.txt', 'a')
        facilities_file.write('\n')
        facilities_file.write(additional_facility)
        facilities_file.close()
        list_of_facilities.append(additional_facility)

    # displays the list of facilities
    def displayFacilities(self):
        facilities_file = open(file_for_facilities, 'r')
        for each_line in facilities_file:
            print(each_line)
        facilities_file.close()

    # writes the facilities list to facilities.txt
    def writeListOfFacilitiesToFile(self):
        facilities_file = open(file_for_facilities, 'w')
        for each_line in list_of_facilities:
            line = each_line
            facilities_file.write(line)
            facilities_file.write('\n')
        facilities_file.close()

# Laboratory class has 2 properties and 6 methods
class Laboratory:
    def __init__(self, lab_name='', cost=''):
        if lab_name != '':
            self.lab_name = lab_name
        if cost != '':
            self.cost = cost

    # adds and writes the lab name to the file in the format of the data that is in the file
    def addLabToFile(self, new_lab):
        self.readLaboratoriesFile()
        laboratories_file = open(file_for_laboratories, 'a')
        add_line = self.formatLabInfo(new_lab)
        laboratories_file.write(add_line)
        laboratories_file.write('\n')
        laboratories_file.close()


    # writes the list of labs into the file laboratories.txt
    def writeListOfLabsToFile(self):
        self.readLaboratoriesFile()
        laboratories_file = open(file_for_laboratories, 'w')
        for each_line in list_of_laboratories:
            line = each_line
            line = self.formatLabInfo(line)
            laboratories_file.write(line)
            laboratories_file.write('\n')
        laboratories_file.close()

    # displays the list of laboratories
    def displayLabsList(self):
        self.readLaboratoriesFile()
        total_rows = len(list_of_laboratories)
        print('how many after: ' + str(total_rows))
        current_row = 0
        while current_row < total_rows:
            print(
                f'{list_of_laboratories[current_row][0]:<12}' + list_of_laboratories[current_row][1])
            current_row += 1

    # formats the Laboratory object similar to the laboratories.txt file
    def formatLabInfo(self, txt_to_format):
        formatted = '_'.join(txt_to_format)
        return formatted

    # asks the user to enter lab name and cost and forms a Laboratory object
    def enterLaboratoryInfo(self):
        self.lab_name = input("Enter Laboratory facility:\n")
        self.cost = int(input("Enter Laboratory cost:\n"))
        new_lab = [self.lab_name, str(self.cost)]
        self.addLabToFile(new_lab)

    # reads the laboratories.txt file and fills its contents in a list of Laboratory objects
    def readLaboratoriesFile(self):
        file = open(file_for_laboratories, 'r')
        for each_line in file:
            list_of_laboratories.append(each_line.rstrip().split('_'))
        file.close()

# Patient class has 5 properties and 9 methods
class Patient:
    def __init__(self, pid=-1, name='', disease='', gender='', age=-1):
        if pid != -1:
            self.pid = pid
        if name != '':
            self.name = name
        if disease != '':
            self.disease = disease
        if gender != '':
            self.gender = gender
        if age != -1:
            self.age = age

    # formats patient information to be added to the file
    def formatPatientInfo(self, txt_to_format):
        # print("formats patient information to be added to the file")
        formatted = '_'.join(txt_to_format)
        return formatted

    # asks the user to enter the patient info
    def enterPatientInfo(self):
        self.pid = int(input("Enter patients’s ID: \n"))
        self.name = input("Enter patient’s name: \n")
        self.disease = input("Enter patient's disease: \n")
        self.gender = input("Enter patient's gender: \n")
        self.age = int(input("Enter patient's age: \n"))
        return [str(self.pid), self.name, self.disease, self.gender, str(self.age)]


    # reads from file patients.txt
    def readPatientsFile(self):
        # print("reads from file patients.txt")
        file = open(file_for_patients, 'r')
        list_of_patients = []
        for each_line in file:
            list_of_patients.append(each_line.rstrip().split('_'))
        file.close()
        return list_of_patients

    # searches for a patient using their ID
    def searchPatientByID(self):
        # print("searches for a patient using their ID")
        id_number = int(input("Enter the Patient's ID: \n"))
        list_of_patients = self.readPatientsFile()
        total_rows = len(list_of_patients)
        current_row = 1
        last_row = total_rows - 1
        patient_found = ''
        while current_row < total_rows:
            if str(id_number) == list_of_patients[current_row][0]:
                print(f'{"ID":<10}' + f'{"Name":<15}' + f'{"Disease":<15}' + f'{"Gender":<15}' + "Age")
                print(f'{list_of_patients[current_row][0]:<10}' + f'{list_of_patients[current_row][1]:<15}' + f'{list_of_patients[current_row][2]:<15}' + f'{list_of_patients[current_row][3]:<15}' + list_of_patients[current_row][4])
                patient_found = 'yes'
            if patient_found != 'yes' and current_row == last_row:
                print("Can't find the patient with the same ID on the system")
            current_row += 1

    # displays patient info
    def displayPatientInfo(self):
        # print("displays patient info")
        list_of_patients = self.readPatientsFile()
        total_rows = len(list_of_patients)
        current_row = 1
        print(f'{"ID":<10}' + f'{"Name":<15}' + f'{"Disease":<15}' + f'{"Gender":<15}' + "Age")
        while current_row < total_rows:
            print(
                f'{list_of_patients[current_row][0]:<10}' + f'{list_of_patients[current_row][1]:<15}' + f'{list_of_patients[current_row][2]:<15}' + f'{list_of_patients[current_row][3]:<15}' + list_of_patients[current_row][4])
            current_row += 1

    # writes a list of patients into the patients.txt file
    def writeListOfPatientsToFile(self, list_of_patients):
        print("writes a list of patients into the patients.txt file")
        patients_file = open(file_for_patients, 'w')
        for each_line in list_of_patients:
            add_line = self.formatPatientInfo(each_line)
            patients_file.write(add_line)
            patients_file.write('\n')
        patients_file.close()

    # adds a new patient into the patients.txt file
    def addPatientToFile(self):
        list_of_patients = self.readPatientsFile()
        self.writeListOfPatientsToFile(list_of_patients)
        patient_to_add = self.enterPatientInfo()
        patients_file = open(file_for_patients, 'a')
        patients_file.write(self.formatPatientInfo(patient_to_add))
        patients_file.write('\n')
        patients_file.close()

