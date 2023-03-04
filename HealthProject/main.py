from AlbertaHospital import Doctor, Facility, Laboratory, Patient
# Questions:
# can I make file and list global variables?

# Global Variables
my_doctor = Doctor()
# my_doctor.writeListOfDoctorsToFile()

my_facility = Facility()

my_laboratory = Laboratory()
# my_laboratory.displayLabsList()
# my_laboratory.enterLaboratoryInfo()
# my_laboratory.displayLabsList()
my_patient = Patient()
my_patient.addPatientToFile()
# doctors_txt = 'doctors.txt'

class Management:
    def DisplayMenu(self):
        menu_option = int(input("Welcome to Alberta Hospital (AH) Management system \nSelect from the following options, or select 0 to stop:\n1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients\n"))
        if menu_option == 1:
            doctors_menu = int(input("Doctor Menu:\n1 - Display Doctors List\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n"))
            if doctors_menu == 1:
                my_doctor.displayDoctorsList()
                print("\nBack to the previous Menu")
                doctors_menu = int(input(
                    "Doctor Menu:\n1 - Display Doctors List\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n"))
            elif doctors_menu == 2:
                my_doctor.searchDoctorById()
                print("\nBack to the previous Menu")
                doctors_menu = int(input(
                    "Doctor Menu:\n1 - Display Doctors List\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n"))
            elif doctors_menu == 3:
                my_doctor.searchDoctorByName()
                print("\nBack to the previous Menu")
                doctors_menu = int(input(
                    "Doctor Menu:\n1 - Display Doctors List\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n"))
            elif doctors_menu == 4:
                my_doctor.enterDrInfo()
                print("\nBack to the previous Menu")
                doctors_menu = int(input(
                    "Doctor Menu:\n1 - Display Doctors List\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n"))
            elif doctors_menu == 5:
                my_doctor.editDoctorInfo()
                doctors_menu = int(input(
                    "Doctor Menu:\n1 - Display Doctors List\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n"))
            elif doctors_menu == 6:
                menu_option = int(input(
                    "Welcome to Alberta Hospital (AH) Management system \nSelect from the following options, or select 0 to stop:\n1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients\n"))
        elif menu_option == 2:
            facilities_menu = int(input("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n"))
            if facilities_menu == 1:
                my_facility.displayFacilities()
                print("\nBack to the previous Menu")
                facilities_menu = int(input(
                    "Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n"))
            elif facilities_menu == 2:
                my_facility.addFacility()
                print("\nBack to the previous Menu")
                facilities_menu = int(input(
                    "Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n"))
            elif facilities_menu == 3:
                menu_option = int(input(
                    "Welcome to Alberta Hospital (AH) Management system \nSelect from the following options, or select 0 to stop:\n1 - Doctors\n2 - Facilities\n3 - Laboratories\n4 - Patients\n"))
        elif menu_option == 3:
            laboratories_menu = int(input("Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n"))
        elif menu_option == 4:
            patients_menu = int(input("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n"))


# my_management = Management()
# my_management.DisplayMenu()