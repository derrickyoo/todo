import factory
import factory.fuzzy

from ..models import Task


class TaskFactory(factory.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    body = factory.Faker(
        "paragraph", nb_sentences=3, variable_nb_sentences=True
    )

    class Meta:
        model = Task
