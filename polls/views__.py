from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

def index(request):
    return render(request, 'polls/index.html')

def winter_winnpy(request):
    return redirect('http://winterai.herokuapp.com')

def winter_univer(request):
    return redirect('http://winnpysoft.pythonanywhere.com')

def face_recognition(request):
    return redirect('http://winter-x-face.herokuapp.com')

def about(request):
    return render(request, 'polls/about.html')

def contact(request):
    return render(request, 'polls/contact.html')

# def question(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
class QuestionView(generic.ListView):
    template_name = 'polls/question.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not include those set to be
        publised in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'

#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id, pub_date__lte=timezone.now())
    
    choices = question.choice_set.all()
    
    # next_q = Question.objects.filter(pub_date__gt=question.pub_date).order_by('pub_date').first()
    # prev_q = Question.objects.filter(pub_date__lt=question.pub_date).order_by('pub_date').first()
    
    try:
        prev_q = question.get_previous_by_pub_date(pub_date__lte=timezone.now())
        prev_id = prev_q.id
    except:
        prev_id = 0

    try:
        next_q = question.get_next_by_pub_date(pub_date__lte=timezone.now())
        next_id = next_q.id
    except:
        next_id = 0
    
    context = {
            'question': question,
            'choices': choices,
            'prev_id': prev_id,
            'next_id': next_id
        }
    
    return render(request, 'polls/detail.html', context)


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        """
        Return the last five published questions (not include those set to be
        publised in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
