# Create your models here.
from django.db import models

from problem.models import Problem
from submission.config import Verdict
from user.models import User


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='submissions')
    code = models.TextField()
    verdict = models.CharField(max_length=10, default=Verdict.PENDING, choices=Verdict.VERDICT_CHOICES)
    lang = models.CharField(max_length=10, null=False)
    create_time = models.DateTimeField(auto_now_add=True)
    last_rejudge_time = models.DateTimeField(default=None, null=True)
    time_spend = models.IntegerField(null=True)
    memory_spend = models.IntegerField(null=True)
    time_cost = models.IntegerField(null=True)
    memory_cost = models.IntegerField(null=True)
    # 程序编译运行的时候返回的一些错误信息和编译失败的错误信息
    additional_info = models.JSONField(default=None, null=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f'<Submission>id:{self.id} problem: {self.problem.id} verdict: {self.verdict}'

    class Meta:
        ordering = ['-id']
