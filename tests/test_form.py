from django.test import TestCase
from todo.forms import TaskForm, TagForm
from todo.models import Tag


class TaskFormTest(TestCase):
    def test_task_form_valid_data(self):
        form_data = {
            "title": "Test Task",
            "content": "Test Content",
            "deadline": "2024-04-02",
            "tags": Tag.objects.all().values_list(
                "id", flat=True
            ),  # Add tags using their IDs
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid_data(self):
        form_data = {
            "title": "",  # title is required, so it's left empty to make the form invalid
            "content": "Test Content",
            "deadline": "2024-04-02",
            "tags": Tag.objects.all().values_list("id", flat=True),
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())


class TagFormTest(TestCase):
    def test_tag_form_valid_data(self):
        form_data = {"name": "Test Tag"}
        form = TagForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_tag_form_invalid_data(self):
        form_data = {
            "name": ""  # name is required, so it's left empty to make the form invalid
        }
        form = TagForm(data=form_data)
        self.assertFalse(form.is_valid())
