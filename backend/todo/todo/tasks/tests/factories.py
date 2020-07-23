from typing import Any, Sequence

from django.contrib.auth.models import User

import factory
import factory.fuzzy
from factory import post_generation

from ..models import Task


class UserFactory(factory.DjangoModelFactory):
    username = factory.Faker("user_name")
    email = factory.Faker("email")

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = (
            extracted
            if extracted
            else factory.Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).generate(extra_kwargs={})
        )
        self.set_password(password)

    class Meta:
        model = User
        django_get_or_create = ["username"]


class TaskFactory(factory.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    body = factory.Faker(
        "paragraph", nb_sentences=3, variable_nb_sentences=True
    )
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Task
