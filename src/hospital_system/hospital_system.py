#This is a very basic hospital entree system for both patients and also doctors. Using classes for object oriented programming, 
#and also inheritence for defining the subsections. 

class Person:
    def __init__(self, title, given_name, middle_name, family_name, birth_day, gender, address, phone):
        self.title = title
        self.given_name = given_name
        self.middle_name = middle_name
        self.family_name = family_name
        self.birth_day = birth_day
        self.gender = gender
        self.address = address
        self.phone = phone

    def get_full_name(self):
        return f"{self.title} {self.given_name} {self.middle_name} {self.family_name}"

    def get_address(self): return self.address
    def get_name(self): return self.given_name
    def get_title(self): return self.title
    def get_phone(self): return self.phone
    def get_middle_name(self): return self.middle_name
    def get_family_name(self): return self.family_name
    def get_birth_day(self): return self.birth_day
    def get_gender(self): return self.gender

    def set_middle_name(self, middle_name): self.middle_name = middle_name
    def set_family_name(self, family_name): self.family_name = family_name
    def set_birth_day(self, birth_day): self.birth_day = birth_day
    def set_gender(self, gender): self.gender = gender
    def set_address(self, address): self.address = address
    def set_name(self, name): self.given_name = name
    def set_title(self, title): self.title = title
    def set_phone(self, phone): self.phone = phone


class Patient(Person):
    def __init__(self, title, given_name, middle_name, family_name, birth_day, gender, address, phone,
                 patient_id, age, accepted, sickness, prescriptions, allergies, special_reqs):
        super().__init__(title, given_name, middle_name, family_name, birth_day, gender, address, phone)
        self.patient_id = patient_id
        self.age = age
        self.accepted = accepted
        self.sickness = sickness
        self.prescriptions = prescriptions
        self.allergies = allergies
        self.special_reqs = special_reqs

    def get_patient_id(self): return self.patient_id
    def get_age(self): return self.age
    def get_accepted(self): return self.accepted
    def get_sickness(self): return self.sickness
    def get_prescriptions(self): return self.prescriptions
    def get_allergies(self): return self.allergies
    def get_special_reqs(self): return self.special_reqs

    def set_patient_id(self, patient_id): self.patient_id = patient_id
    def set_age(self, age): self.age = age
    def set_accepted(self, accepted): self.accepted = accepted
    def set_sickness(self, sickness): self.sickness = sickness
    def set_prescriptions(self, prescriptions): self.prescriptions = prescriptions
    def set_allergies(self, allergies): self.allergies = allergies
    def set_special_reqs(self, special_reqs): self.special_reqs = special_reqs


class Staff(Person):
    def __init__(self, title, given_name, middle_name, family_name, birth_day, gender, address, phone,
                 joined, education, certification, languages):
        super().__init__(title, given_name, middle_name, family_name, birth_day, gender, address, phone)
        self.joined = joined
        self.education = education
        self.certification = certification
        self.languages = languages

    def get_day_joined(self): return self.joined
    def get_education(self): return self.education
    def get_certification(self): return self.certification
    def get_languages(self): return self.languages

    def set_joined(self, joined): self.joined = joined
    def set_education(self, education): self.education = education
    def set_certification(self, certification): self.certification = certification
    def set_languages(self, languages): self.languages = languages


class OperationsStaff(Staff):
    def __init__(self, title, given_name, middle_name, family_name, birth_day, gender, address, phone,
                 joined, education, certification, languages, size, availability):
        super().__init__(title, given_name, middle_name, family_name, birth_day, gender, address, phone,
                         joined, education, certification, languages)
        self.size = size
        self.availability = availability

    def get_size(self): return self.size
    def get_availability(self): return self.availability

    def set_size(self, size): self.size = size
    def set_availability(self, availability): self.availability = availability


class Doctor(OperationsStaff):
    def __init__(self, title, given_name, middle_name, family_name, birth_day, gender, address, phone, joined,
                 education, certification, languages, size, availability, speciality, locations):
        super().__init__(title, given_name, middle_name, family_name, birth_day, gender, address, phone,
                         joined, education, certification, languages, size, availability)
        self.speciality = speciality
        self.locations = locations

    def get_speciality(self): return self.speciality
    def get_locations(self): return self.locations

    def set_speciality(self, speciality): self.speciality = speciality
    def set_locations(self, locations): self.locations = locations


class Surgeon(Doctor):
    def __init__(self, title, given_name, middle_name, family_name, birth_day, gender, address, phone, joined,
                 education, certification, languages, size, availability, speciality, locations, surgeries_done):
        super().__init__(title, given_name, middle_name, family_name, birth_day, gender, address, phone, joined,
                         education, certification, languages, size, availability, speciality, locations)
        self.surgeries_done = surgeries_done

    def get_surgeries_done(self): return self.surgeries_done
    def set_surgeries_done(self, surgeries_done): self.surgeries_done = surgeries_done

def main():
    current_patient = None
    current_doctor = None
    current_surgeon = None

    while True:
        print("\n--- Hospital System Menu ---")
        print("1. Create Patient")
        print("2. Create Doctor")
        print("3. Create Surgeon")
        print("4. View Patient Info")
        print("5. View Doctor Info")
        print("6. View Surgeon Info")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            print("\nEnter patient details:")
            current_patient = Patient(
                input("Title: "),
                input("Given Name: "),
                input("Middle Name: "),
                input("Family Name: "),
                input("Birth Date (YYYY-MM-DD): "),
                input("Gender: "),
                input("Address: "),
                input("Phone: "),
                input("Patient ID: "),
                int(input("Age: ")),
                input("Accepted (True/False): ").strip().lower() == "true",
                input("Sickness: "),
                input("Prescriptions (comma-separated): ").strip().split(","),
                input("Allergies (comma-separated): ").strip().split(","),
                input("Special Requirements: ")
            )
            print("✅ Patient created!")
            print("Name:", current_patient.get_full_name())

        elif choice == "2":
            print("\nEnter doctor details:")
            current_doctor = Doctor(
                input("Title: "),
                input("Given Name: "),
                input("Middle Name: "),
                input("Family Name: "),
                input("Birth Date (YYYY-MM-DD): "),
                input("Gender: "),
                input("Address: "),
                input("Phone: "),
                input("Joined Date (YYYY-MM-DD): "),
                input("Education: "),
                input("Certification: "),
                input("Languages (comma-separated): ").strip().split(","),
                int(input("Team Size: ")),
                input("Availability (True/False): ").strip().lower() == "true",
                input("Speciality: "),
                input("Locations (comma-separated): ").strip().split(",")
            )
            print("✅ Doctor created!")
            print("Name:", current_doctor.get_full_name())

        elif choice == "3":
            print("\nEnter surgeon details:")
            current_surgeon = Surgeon(
                input("Title: "),
                input("Given Name: "),
                input("Middle Name: "),
                input("Family Name: "),
                input("Birth Date (YYYY-MM-DD): "),
                input("Gender: "),
                input("Address: "),
                input("Phone: "),
                input("Joined Date (YYYY-MM-DD): "),
                input("Education: "),
                input("Certification: "),
                input("Languages (comma-separated): ").strip().split(","),
                int(input("Team Size: ")),
                input("Availability (True/False): ").strip().lower() == "true",
                input("Speciality: "),
                input("Locations (comma-separated): ").strip().split(","),
                int(input("Number of Surgeries Done: "))
            )
            print("✅ Surgeon created!")
            print("Name:", current_surgeon.get_full_name())

        elif choice == "4":
            if current_patient:
                print("\nPatient Information")
                print("Name:", current_patient.get_full_name())
                print("Sickness:", current_patient.get_sickness())
                print("Age:", current_patient.get_age())
                print("Accepted:", current_patient.get_accepted())
            else:
                print("⚠ No patient created yet.")

        elif choice == "5":
            if current_doctor:
                print("\nDoctor Information")
                print("Name:", current_doctor.get_full_name())
                print("Speciality:", current_doctor.get_speciality())
                print("Locations:", ", ".join(current_doctor.get_locations()))
            else:
                print("⚠ No doctor created yet.")

        elif choice == "6":
            if current_surgeon:
                print("\nSurgeon Information")
                print("Name:", current_surgeon.get_full_name())
                print("Speciality:", current_surgeon.get_speciality())
                print("Surgeries Done:", current_surgeon.get_surgeries_done())
                print("Availability:", current_surgeon.get_availability())
                print("Locations:", ", ".join(current_surgeon.get_locations()))
            else:
                print("No surgeon created yet.")

        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()

    
