from django.contrib import admin

from . import models


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'tester']
    fields = (
        'project_name',
        'tester',
        'start_date',
        'end_date',
        'staging_site',
        'production_site',
        'type_of_project',
    )


class BugClassificationInline(admin.TabularInline):
    model = models.BugClassification
    max_num = 1
    can_delete = False


class ReportedByInline(admin.TabularInline):
    model = models.ReportedBy
    max_num = 1
    can_delete = False


class AssignedToInline(admin.TabularInline):
    model = models.AssignedTo
    max_num = 1
    can_delete = False


class BugReportAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'name', 'date_reported')
    inlines = [BugClassificationInline, ReportedByInline, AssignedToInline]
    fields = (
        'project_name',
        'name',
        'bug_type',
        'bug_description',
        'steps_to_replicate',
        'actual_output',
        'expected_output',
        'date_reported',
    )

admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.BugDetail, BugReportAdmin)
