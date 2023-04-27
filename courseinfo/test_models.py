from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Period, Course, Student, Instructor, Year, Semester, Section, Registration
from .test_data_initialize import initialize_year_data, initialize_period_data, initialize_course_data, \
    initialize_student_data, initialize_instructor_data, initialize_semester_data, initialize_section_data, \
    initialize_registration_data


class PeriodModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        initialize_period_data()

    def test_is_period_name_unique(self):
        period2 = Period(period_sequence=4, period_name='Fall')
        with self.assertRaisesMessage(
                ValidationError,
                'Period with this Period name already exists.',
        ):
            period2.full_clean()

    def test_ordering(self):
        periods = Period.objects.all()
        self.assertEquals(periods[0].period_sequence, 1)
        self.assertEquals(periods[1].period_sequence, 2)
        self.assertEquals(periods[2].period_sequence, 3)


class YearModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        initialize_year_data()

    def test_year_ordering(self):
        year = Year.objects.all()
        self.assertEqual(year[0].year, 2021)
        self.assertEqual(year[1].year, 2022)


class CourseModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        initialize_course_data()

    def test_is_course_unique_constraint(self):
        courseNew = Course(course_number='IS439', course_name='Web Development')
        with self.assertRaisesMessage(
                ValidationError,
                'Course with this Course number and Course name already exists.',
        ):
            courseNew.full_clean()

    def test_course_ordering(self):
        courses = Course.objects.all()
        self.assertEqual(courses[0].course_number, 'IS439')
        self.assertEqual(courses[1].course_number, 'IS455')


class StudentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        initialize_student_data()

    def test_is_student_unique_constraint(self):
        studentNew = Student(first_name='Saurabh', last_name='Saoji', disambiguator='UIUC')
        with self.assertRaisesMessage(
                ValidationError,
                'Student with this Last name, First name and Disambiguator already exists.',
        ):
            studentNew.full_clean()

class InstructorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        initialize_instructor_data()

    def test_is_instructor_unique_constraint(self):
        instructorNew = Instructor(first_name='Saurabh', last_name='Saoji', disambiguator='UIUC')
        with self.assertRaisesMessage(
                ValidationError,
                'Instructor with this Last name, First name and Disambiguator already exists.',
        ):
            instructorNew.full_clean()


class SemesterModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        initialize_semester_data()


    def test_is_semester_unique(self):
        year1 = Year.objects.get(year=2022)
        period1 = Period.objects.get(period_sequence=1)
        semester = Semester(year=year1, period=period1)
        with self.assertRaisesMessage(
                ValidationError,
                'Semester with this Year and Period already exists.',
        ):
            semester.full_clean()


class SectionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        initialize_section_data()


    def test_is_section_unique(self):
        period1 = Period.objects.get(period_sequence=1)
        year1 = Year.objects.get(year=2022)
        semester = Semester.objects.get(year=year1, period=period1)
        instructor = Instructor.objects.get(first_name='Saurabh', last_name='Saoji', disambiguator='UIUC')
        course1 = Course.objects.get(course_number='IS439', course_name='Web Development')
        section = Section(section_name='OAG', semester=semester, course=course1, instructor=instructor)
        with self.assertRaisesMessage(
                ValidationError,
                'Section with this Semester, Course and Section name already exists.',
        ):
            section.full_clean()


class RegistrationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        initialize_registration_data()


    def test_is_registration_unique(self):
        period1 = Period.objects.get(period_sequence=1)
        year1 = Year.objects.get(year=2022)
        semester = Semester.objects.get(year=year1, period=period1)
        instructor = Instructor.objects.get(first_name='Saurabh', last_name='Saoji', disambiguator='UIUC')
        course1 = Course.objects.get(course_number='IS439', course_name='Web Development')
        section1 = Section.objects.get(section_name='OAG', semester=semester, course=course1, instructor=instructor)
        student = Student.objects.get(first_name='Saurabh', last_name='Saoji', disambiguator='UIUC')
        registration = Registration(section=section1, student=student)
        with self.assertRaisesMessage(
                ValidationError,
                'Registration with this Section and Student already exists.',
        ):
            registration.full_clean()






