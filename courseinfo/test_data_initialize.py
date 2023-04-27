from courseinfo.models import Course, Period, Year, Student, Instructor, Semester, Section, Registration


def initialize_year_data():
    Year.objects.create(year=2022)
    Year.objects.create(year=2021)


def initialize_period_data():
    Period.objects.create(period_sequence=1, period_name='Spring')
    Period.objects.create(period_sequence=2, period_name='Summer')
    Period.objects.create(period_sequence=3, period_name='Fall')


def initialize_course_data():
    Course.objects.create(course_number='IS439', course_name='Web Development')
    Course.objects.create(course_number='IS455', course_name='Database Design and Prototyping')


def initialize_student_data():
    Student.objects.create(first_name='Saurabh', last_name='Saoji', disambiguator='UIUC')
    Student.objects.create(first_name='Kevin', last_name='Trainor', disambiguator='UIUC')


def initialize_instructor_data():
    Instructor.objects.create(first_name='Saurabh', last_name='Saoji', disambiguator='UIUC')
    Instructor.objects.create(first_name='Kevin', last_name='Trainor', disambiguator='UIUC')


def initialize_semester_data():
    period1 = Period.objects.create(period_sequence=1, period_name='Spring')
    period2 = Period.objects.create(period_sequence=2, period_name='Summer')
    year1 = Year.objects.create(year=2022)
    Semester.objects.create(year=year1, period=period1)
    Semester.objects.create(year=year1, period=period2)


def initialize_section_data():
    period1 = Period.objects.create(period_sequence=1, period_name='Spring')
    year1 = Year.objects.create(year=2022)
    semester1 = Semester.objects.create(year=year1, period=period1)
    instructor1 = Instructor.objects.create(first_name='Saurabh', last_name='Saoji', disambiguator='UIUC')
    course1 = Course.objects.create(course_number='IS439', course_name='Web Development')
    Section.objects.create(section_name='OAG', semester=semester1, course=course1, instructor=instructor1)


def initialize_registration_data():
    period1 = Period.objects.create(period_sequence=1, period_name='Spring')
    year1 = Year.objects.create(year=2022)
    semester1 = Semester.objects.create(year=year1, period=period1)
    instructor1 = Instructor.objects.create(first_name='Saurabh', last_name='Saoji', disambiguator='UIUC')
    course1 = Course.objects.create(course_number='IS439', course_name='Web Development')
    student = Student.objects.create(first_name='Saurabh', last_name='Saoji', disambiguator='UIUC')
    section1 = Section.objects.create(section_name='OAG', semester=semester1, course=course1, instructor=instructor1)
    Registration.objects.create(section=section1, student=student)
