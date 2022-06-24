import django
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from django.db.models import Sum
from officeapp import models

# Create your views here.
class Home(View):
    template_name = 'index.html'
    def get(self, request):
        students = models.StudentModel.objects.all()
        return render(request, self.template_name, context={'students': students})

class NewStudent(View):
    template_name = 'new-student.html'
    def get(self, request):
        courses = models.CourseModel.objects.all()
        return render(request, self.template_name, context={'courses': courses})

    def post(self, request):
        name = request.POST.get('name')
        course = request.POST.get('course')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        fees_amt = request.POST.get('fees_amt')
        photo = request.FILES.get('photo')

        try:
            new_student = models.StudentModel(name=name, course_name=course, mobile_number=mobile,
                                        email=email, course_fees=fees_amt, photo=photo)
            new_student.save()

            messages.info(request, f'New Student - "{name}" Added')
        except django.db.utils.IntegrityError:
            messages.info(request, f'Student - "{name}" Already Exist')

        return redirect('/new-student')

class EditStudent(View):
    template_name = 'new-student.html'
    def get(self, request, pk):
        student = models.StudentModel.objects.get(id=pk)
        print(student)
        courses = models.CourseModel.objects.all()
        return render(request, self.template_name, context={'student': student, 'courses': courses})
    
    def post(self, request, pk):
        name = request.POST.get('name')
        course = request.POST.get('course')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        fees_amt = request.POST.get('fees_amt')
        photo = request.FILES.get('photo')
    

        update_student = models.StudentModel.objects.get(id=pk)
        update_student.name = name
        update_student.course_name = course
        update_student.mobile_number = mobile
        update_student.email = email
        update_student.course_fees = fees_amt
        if request.FILES.get('photo'):
            update_student.photo = photo
        update_student.save()

        messages.info(request, f'New Data - "{name}" Updated..')

        return redirect('/new-student')

class DeleteStudent(View):
    def get(self, request, pk):
        delete_student = models.StudentModel.objects.get(id=pk)
        delete_student.delete()
        return redirect('/')

class PayFees(View):
    template_name = 'pay-fees.html'
    def get(self, request):
        students = models.StudentModel.objects.all()
        return render(request, self.template_name, context={'students': students})

    def post(self, request):
        name = request.POST.get('name')
        fees = request.POST.get('fees-amt')
        desc = request.POST.get('desc')

        student = models.StudentModel.objects.get(name=name)

        payfees = models.PayeFeesModel(name=student, fees_amt=fees, description=desc)
        payfees.save()

        messages.info(request, f'{name} paid - {fees}')

        return redirect('/pay-fees')

class CourseList(View):
    template_name = 'course-list.html'
    def get(self, request):
        courses = models.CourseModel.objects.all()
        return render(request, self.template_name, context={'courses': courses})

    def post(self, request):
        course_name = request.POST.get('course-name')
        course = models.CourseModel(name=course_name)
        course.save()

        messages.info(request, f'New Course - {course_name} added..')

        return redirect('/course-list')

class DeleteCourse(View):
    def get(self, request, pk):
        course = models.CourseModel.objects.get(id=pk)
        course.delete()
        return redirect('/course-list')

class FeesDetails(View):
    template_name = "fees-details.html"
    def get(self, request, pk):
        student = models.StudentModel.objects.get(id=pk)
        stu_fees = models.PayeFeesModel.objects.filter(name=student)
        total = models.PayeFeesModel.objects.filter(name=student).aggregate(Sum("fees_amt"))['fees_amt__sum']
        return render(request, self.template_name,   context={'students': stu_fees, 'stu': student, 'total': total})

class DeleteFeesDetails(View):
    def get(self, request, pk, id):
        fees = models.PayeFeesModel.objects.get(id=pk)
        fees.delete()
        return redirect(f'/fees-details/{id}')

class AddTopics(View):
    template_name = 'add-topics.html'
    def get(self, request):
        courses = models.CourseModel.objects.all()
        return render(request, self.template_name, context={'courses': courses})

    def post(self, request):
        course = request.POST.get('course')
        title = request.POST.get('topic')

        course_obj = models.CourseModel.objects.get(name=course)
        add_topic = models.CourseTopicModels(name=course_obj, topic=title)
        add_topic.save()

        messages.info(request, f'New Topic "{title}" added in {course}')
        return redirect('/add-topics')

class AddTasks(View):
    template_name = 'add-tasks.html'
    def get(self, request):
        courses = models.CourseModel.objects.all()
        topics = models.CourseTopicModels.objects.all()
        return render(request, self.template_name, context={'courses': courses, 'topics': topics})

    def post(self, request):
        course = request.POST.get('course')
        title = request.POST.get('topic')
        question = request.POST.get('question')
        sample_input = request.POST.get('sample-input')
        sample_output = request.POST.get('sample-output')

        topic_obj = models.CourseTopicModels.objects.get(topic=title)
        add_task = models.CourseTasksModel(topics=topic_obj, question=question, 
                                            sample_input=sample_input, sample_output=sample_output)
        add_task.save()

        messages.info(request, f'New Task "{title}" added in {course}')
        return redirect('/add-tasks')

class Tasks(View):
    template_name = 'office-tasks.html'
    def get(self, request, course, topic):
        courses = models.CourseModel.objects.all()
        course = models.CourseModel.objects.get(name=course)
        topics = models.CourseTopicModels.objects.filter(name=course)

        selected_topic = models.CourseTopicModels.objects.get(topic=topic.replace('%20', ' '))
        questions = models.CourseTasksModel.objects.filter(topics=selected_topic)

        total_tasks = questions.count()

        datas = {
                    'courses': courses,
                    'topics': topics,
                    'scourse': course.name,
                    'questions': questions,
                    'totaltasks': total_tasks,
                }
        return render(request, self.template_name, context=datas)