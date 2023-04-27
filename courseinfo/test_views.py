from django.test import TestCase
from django.urls import reverse

from courseinfo.models import Instructor, Course, Semester, Section, Student, Registration
from courseinfo.test_data_initialize import initialize_course_data, initialize_instructor_data, initialize_section_data, \
    initialize_semester_data, initialize_student_data, initialize_registration_data


class TestInstructorView(TestCase):
    @classmethod
    def setUpTestData(cls):
        initialize_instructor_data()

    def test_instructor_list_view_with_instructor(self):
        instructors = Instructor.objects.all()
        url = reverse('courseinfo_instructor_list_urlpattern')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/instructor_list.html')
        self.assertContains(response, 'Saoji, Saurabh, (UIUC)')
        self.assertContains(response, 'Trainor, Kevin, (UIUC)')
        for instructor in instructors:
            self.assertContains(response, '<a href="%s">%s</a>' % (instructor.get_absolute_url(), instructor)
)

    def test_instructor_list_view_without_instructor(self):
        Instructor.objects.all().delete()
        url = reverse('courseinfo_instructor_list_urlpattern')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/instructor_list.html')
        self.assertContains(response, 'There are no instructors available.')


class TestInstructorDetail(TestCase):

    def setUp(self):
        initialize_section_data()
        self.instructor = Instructor.objects.get(pk=1)

    def test_instructor_detail_view_if_url_valid(self):
        sections = Section.objects.all()
        url = reverse('courseinfo_instructor_detail_urlpattern', args=[self.instructor.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/instructor_detail.html')
        for section in sections:
            self.assertContains(response, '<a href="%s">%s</a>' % (section.get_absolute_url(), section))

    def test_instructor_detail_view_context_values(self):
        url = reverse('courseinfo_instructor_detail_urlpattern', args=[self.instructor.pk])
        response = self.client.get(url)
        contextInstructor = response.context['instructor']
        sectionList = response.context['section_list']
        expectedSectionList = list(self.instructor.sections.all())
        self.assertEqual(contextInstructor, self.instructor)
        self.assertEqual(list(sectionList), expectedSectionList)

    def test_instructor_detail_view_if_url_invalid(self):
        Section.objects.all().delete()
        Instructor.objects.all().delete()
        url = reverse('courseinfo_instructor_detail_urlpattern', args=[self.instructor.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class TestCourseView(TestCase):
    @classmethod
    def setUpTestData(cls):
        initialize_course_data()

    def test_course_list_view_with_course(self):
        courses = Course.objects.all()
        url = reverse('courseinfo_course_list_urlpattern')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/course_list.html')
        self.assertContains(response, 'IS439 - Web Development')
        self.assertContains(response, 'IS455 - Database Design and Prototyping')
        for course in courses:
            self.assertContains(response, '<a href="%s">%s</a>' % (course.get_absolute_url(), course))

    def test_course_list_view_without_course(self):
        Course.objects.all().delete()
        url = reverse('courseinfo_course_list_urlpattern')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/course_list.html')
        self.assertContains(response, 'There are no courses available.')


class TestCourseDetail(TestCase):

    def setUp(self):
        initialize_section_data()
        self.course = Course.objects.get(pk=1)

    def test_course_detail_view_if_url_valid(self):
        sections = Section.objects.all()
        url = reverse('courseinfo_course_detail_urlpattern', args=[self.course.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/course_detail.html')
        for section in sections:
            self.assertContains(response, '<a href="%s">%s</a>' % (section.get_absolute_url(), section))

    def test_course_detail_view_context_values(self):
        url = reverse('courseinfo_course_detail_urlpattern', args=[self.course.pk])
        response = self.client.get(url)
        contextCourse = response.context['course']
        sectionList = response.context['section_list']
        expectedSectionList = list(self.course.sections.all())
        self.assertEqual(contextCourse, self.course)
        self.assertEqual(list(sectionList), expectedSectionList)

    def test_course_detail_view_if_url_invalid(self):
        Section.objects.all().delete()
        Course.objects.all().delete()
        url = reverse('courseinfo_course_detail_urlpattern', args=[self.course.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class TestSectionView(TestCase):
    @classmethod
    def setUpTestData(cls):
        initialize_section_data()

    def test_section_list_view_with_section(self):
        sections = Section.objects.all()
        url = reverse('courseinfo_section_list_urlpattern')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/section_list.html')
        self.assertContains(response, 'IS439 - OAG 2022 - Spring')
        for section in sections:
            self.assertContains(response, '<a href="%s">%s</a>' % (section.get_absolute_url(), section))

    def test_section_list_view_without_section(self):
        Section.objects.all().delete()
        url = reverse('courseinfo_section_list_urlpattern')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/section_list.html')
        self.assertContains(response, 'There are no sections available.')


class TestSectionDetail(TestCase):

    def setUp(self):
        initialize_registration_data()
        self.section = Section.objects.get(pk=1)

    def test_section_detail_view_if_url_valid(self):
        course = Course.objects.first()
        semester = Semester.objects.first()
        instructor = Instructor.objects.first()
        registrations = Registration.objects.all()
        url = reverse('courseinfo_section_detail_urlpattern', args=[self.section.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/section_detail.html')
        self.assertContains(response, '<a href="%s">%s</a>' % (course.get_absolute_url(), course))
        self.assertContains(response, '<a href="%s">%s</a>' % (instructor.get_absolute_url(), instructor))
        self.assertContains(response, '<a href="%s">%s</a>' % (semester.get_absolute_url(), semester))
        for registration in registrations:
            self.assertContains(response, '<a href="%s">%s</a>' % (registration.get_absolute_url(), registration.student))


    def test_section_detail_view_context_values(self):
        url = reverse('courseinfo_section_detail_urlpattern', args=[self.section.pk])
        response = self.client.get(url)
        contextCourse = response.context['course']
        contextSemester = response.context['semester']
        contextInstructor = response.context['instructor']
        registrationList = response.context['registration_list']
        expectedRegistrationList = list(self.section.registrations.all())
        self.assertEqual(contextCourse, self.section.course)
        self.assertEqual(contextSemester, self.section.semester)
        self.assertEqual(contextInstructor, self.section.instructor)
        self.assertEqual(list(registrationList), expectedRegistrationList)

    def test_section_detail_view_if_url_invalid(self):
        Registration.objects.all().delete()
        Section.objects.all().delete()
        url = reverse('courseinfo_section_detail_urlpattern', args=[self.section.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class TestSemesterView(TestCase):
    @classmethod
    def setUpTestData(cls):
        initialize_semester_data()

    def test_semester_list_view_with_semester(self):
        semesters = Semester.objects.all()
        url = reverse('courseinfo_semester_list_urlpattern')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/semester_list.html')
        self.assertContains(response, '022 - Spring')
        self.assertContains(response, '2022 - Summer')
        for semester in semesters:
            self.assertContains(response, '<a href="%s">%s</a>' % (semester.get_absolute_url(), semester))

    def test_semester_list_view_without_semester(self):
        Semester.objects.all().delete()
        url = reverse('courseinfo_semester_list_urlpattern')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/semester_list.html')
        self.assertContains(response, 'There are no semesters available.')


class TestSemesterDetail(TestCase):

    def setUp(self):
        initialize_section_data()
        self.semester = Semester.objects.get(pk=1)

    def test_semester_detail_view_if_url_valid(self):
        sections = Section.objects.all()
        url = reverse('courseinfo_semester_detail_urlpattern', args=[self.semester.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/semester_detail.html')
        for section in sections:
            self.assertContains(response, '<a href="%s">%s</a>' % (section.get_absolute_url(), section))

    def test_semester_detail_view_context_values(self):
        url = reverse('courseinfo_semester_detail_urlpattern', args=[self.semester.pk])
        response = self.client.get(url)
        contextSemester = response.context['semester']
        sectionList = response.context['section_list']
        expectedSectionList = list(self.semester.sections.all())
        self.assertEqual(contextSemester, self.semester)
        self.assertEqual(list(sectionList), expectedSectionList)

    def test_semester_detail_view_if_url_invalid(self):
        Section.objects.all().delete()
        Semester.objects.all().delete()
        url = reverse('courseinfo_semester_detail_urlpattern', args=[self.semester.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class TestStudentView(TestCase):
    @classmethod
    def setUpTestData(cls):
        initialize_student_data()

    def test_student_list_view_with_student(self):
        students = Student.objects.all()
        url = reverse('courseinfo_student_list_urlpattern')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/student_list.html')
        self.assertContains(response, 'Saoji, Saurabh, (UIUC)')
        self.assertContains(response, 'Trainor, Kevin, (UIUC)')
        for student in students:
            self.assertContains(response, '<a href="%s">%s</a>' % (student.get_absolute_url(), student))

    def test_student_list_view_without_student(self):
        Student.objects.all().delete()
        url = reverse('courseinfo_student_list_urlpattern')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/student_list.html')
        self.assertContains(response, 'There are no students available.')


class TestStudentDetail(TestCase):

    def setUp(self):
        initialize_registration_data()
        self.student = Student.objects.get(pk=1)

    def test_student_detail_view_if_url_valid(self):
        registrations = Registration.objects.all()
        url = reverse('courseinfo_student_detail_urlpattern', args=[self.student.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/student_detail.html')
        for registration in registrations:
            self.assertContains(response, '<a href="%s">%s</a>' % (registration.get_absolute_url(), registration.section))

    def test_student_detail_view_context_values(self):
        url = reverse('courseinfo_student_detail_urlpattern', args=[self.student.pk])
        response = self.client.get(url)
        contextStudent = response.context['student']
        registrationList = response.context['registration_list']
        expectedRegistrationList = list(self.student.registrations.all())
        self.assertEqual(list(registrationList), expectedRegistrationList)
        self.assertEqual(contextStudent, self.student)

    def test_student_detail_view_if_url_invalid(self):
        Registration.objects.all().delete()
        Student.objects.all().delete()
        url = reverse('courseinfo_student_detail_urlpattern', args=[self.student.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class TestRegistrationView(TestCase):
    @classmethod
    def setUpTestData(cls):
        initialize_registration_data()

    def test_registration_list_view_with_registration(self):
        registrations = Registration.objects.all()
        url = reverse('courseinfo_registration_list_urlpattern')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/registration_list.html')
        self.assertContains(response, 'S439 - OAG 2022 - Spring / Saoji, Saurabh, (UIUC)')
        for registration in registrations:
            self.assertContains(response, '<a href="%s">%s</a>' % (registration.get_absolute_url(), registration))

    def test_registration_list_view_without_registration(self):
        Registration.objects.all().delete()
        url = reverse('courseinfo_registration_list_urlpattern')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/registration_list.html')
        self.assertContains(response, 'There are no registrations available.')


class TestRegistrationDetail(TestCase):

    def setUp(self):
        initialize_registration_data()
        self.registration = Registration.objects.get(pk=1)

    def test_registration_detail_view_if_url_valid(self):
        registration = Registration.objects.first()
        section = registration.section
        url = reverse('courseinfo_registration_detail_urlpattern', args=[self.registration.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertTemplateUsed(response, 'courseinfo/registration_detail.html')
        self.assertContains(response, '<a href="%s">%s</a>' % (section.get_absolute_url(), section))

    def test_registration_detail_view_context_values(self):
        url = reverse('courseinfo_registration_detail_urlpattern', args=[self.registration.pk])
        response = self.client.get(url)
        contextStudent = response.context['student']
        contextSection = response.context['section']
        self.assertEqual(contextSection, self.registration.section)
        self.assertEqual(contextStudent, self.registration.student)

    def test_registration_detail_view_if_url_invalid(self):
        Registration.objects.all().delete()
        url = reverse('courseinfo_registration_detail_urlpattern', args=[self.registration.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
