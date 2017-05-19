from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from bug_report_tool.users.models import User

# Create your models here.


@python_2_unicode_compatible
class Project(models.Model):
    TYPE_OF_PROJECT = (
        ('Kanban', 'Kanban'),
        ('Scrum', 'Scrum'),
    )
    project_name = models.CharField(max_length=100, blank=False)
    tester = models.ForeignKey(User)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    staging_site = models.CharField(max_length=100, blank=True, null=True)
    production_site = models.CharField(max_length=100, blank=True, null=True)
    type_of_project = models.CharField(max_length=10, choices=TYPE_OF_PROJECT,
                                       default='Scrum')

    def __str__(self):
        return self.project_name


@python_2_unicode_compatible
class BugDetail(models.Model):
    BUG_TYPE = (
        ('UI', 'User Interface'),
        ('functional', 'Functional'),
        ('recurring', 'Recurring'),
    )
    project_name = models.ForeignKey(Project, related_name='project')
    name = models.CharField(max_length=100, blank=False)
    bug_description = models.TextField(blank=True)
    steps_to_replicate = models.TextField(blank=True)
    actual_output = models.TextField(blank=True)
    expected_output = models.TextField(blank=True)
    date_reported = models.DateField(blank=True, null=True)
    bug_type = models.CharField(max_length=15, choices=BUG_TYPE,
                                default='functional')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class BugClassification(models.Model):
    SEVERITY = (
        ('Blocker', 'Blocker'),
        ('Critical', 'Critical'),
        ('Major', 'Major'),
        ('Minor', 'Minor'),
        ('Trivial', 'Trivial'),
        ('Enhancement', 'Enhancement'),
    )
    PRIORITY = (
        ('Critical', 'Critical'),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    STATUS = (
        ('to_do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('for_testing', 'For Testing'),
        ('test_in_progress', 'Testing in Progress'),
        ('has_issues', 'Still has issues'),
        ('done', 'Done'),
        ('on_dev', 'On Dev'),
    )
    DEVICE = (
        ('android', 'Android'),
        ('ios', 'iOS'),
        ('na', 'Not Applicable'),
    )
    BROWSER = (
        ('firefox', 'Firefox'),
        ('chrome', 'Chrome'),
        ('others', 'Others'),
        ('na', 'Not Applicable'),
    )

    bug = models.ForeignKey(BugDetail)
    bug_severity = models.CharField(max_length=20, choices=SEVERITY,
                                    default='Critical')
    bug_priority = models.CharField(max_length=20, choices=PRIORITY,
                                    default='Critical')
    status = models.CharField(max_length=50, choices=PRIORITY,
                              default='For Testing')
    device = models.CharField(max_length=10, choices=DEVICE,
                              default='na')
    browser = models.CharField(max_length=10, choices=BROWSER,
                               default='na')

    def __str__(self):
        return self.bug.name


@python_2_unicode_compatible
class ReportedBy(models.Model):
    bug = models.ForeignKey(BugDetail)
    user = models.ForeignKey(User, related_name='tester')
    tester_note = models.TextField(blank=True)

    def __str__(self):
        return self.bug.name


@python_2_unicode_compatible
class AssignedTo(models.Model):
    bug = models.ForeignKey(BugDetail)
    user = models.ForeignKey(User, related_name='developer')
    dev_notes = models.TextField(blank=True)

    def __str__(self):
        return self.bug.name


@python_2_unicode_compatible
class BugReport(models.Model):
    bug = models.ForeignKey(BugDetail)
    project = models.ForeignKey(Project)
    num_of_issues = models.IntegerField()
    num_of_fixed = models.IntegerField()
    num_for_testing = models.IntegerField()
    num_of_unresolved = models.IntegerField()

    def __str__(self):
        return self.bug.name
