from django.test import TestCase
from todo.models import Task, Tag
from django.utils import timezone


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.tag1 = Tag.objects.create(name="Tag1")
        cls.tag2 = Tag.objects.create(name="Tag2")
        cls.task = Task.objects.create(
            title="Test Task",
            content="Test Content",
            deadline=timezone.now(),
            is_done=False,
        )
        cls.task.tags.add(cls.tag1, cls.tag2)

    def test_task_title(self):
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.title, "Test Task")

    def test_task_content(self):
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.content, "Test Content")

    def test_task_deadline(self):
        task = Task.objects.get(id=self.task.id)
        self.assertIsNotNone(task.deadline)

    def test_task_is_done(self):
        task = Task.objects.get(id=self.task.id)
        self.assertFalse(task.is_done)

    def test_task_tags(self):
        task = Task.objects.get(id=self.task.id)
        self.assertEqual(task.tags.count(), 2)
        self.assertIn(self.tag1, task.tags.all())
        self.assertIn(self.tag2, task.tags.all())


class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.tag = Tag.objects.create(name="Test Tag")

    def test_tag_name(self):
        tag = Tag.objects.get(id=self.tag.id)
        self.assertEqual(tag.name, "Test Tag")
