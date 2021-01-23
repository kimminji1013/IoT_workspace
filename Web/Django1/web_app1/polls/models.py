from django.db import models

class Question(models.Model):
    # class 멤버 변수
    #   - class 안에서 self 와 무관하게 정의되는 멤버 변수
    #   - 인스턴스와 무관하게 존재하며 모든 인스턴스가 공유하는 정보
    question_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
