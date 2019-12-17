import time

import factory
from django.db import connection, models
from django.utils import timezone
from django.test import TestCase
from unittest import skip

from sandbox.model_performance.models import Parent, Child


class ParentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Parent

    created_at = timezone.now()


class ChildFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Child

    created_at = timezone.now()
    parent = factory.SubFactory(ParentFactory)


class ModelPerformanceTest(TestCase):

    @skip
    def test_compare_query_performance(self):
        batch_size = 1000000
        parent = ParentFactory()
        children = ChildFactory.create_batch(batch_size, parent=parent)

        def by_orm():
            start_time = time.time()
            children = list(Child.objects.all())
            self.assertEqual(len(children), batch_size)
            return time.time() - start_time

        def by_raw_query():
            with connection.cursor() as cursor:
                start_time = time.time()
                cursor.execute('SELECT * FROM model_performance_child')
                rows = cursor.fetchall()
                self.assertEqual(len(rows), batch_size)
                return time.time() - start_time

        def by_orm_with_values():
            start_time = time.time()
            rows = list(Child.objects.all().values('pk', 'created_at'))
            self.assertEqual(len(rows), batch_size)
            return time.time() - start_time

        def by_orm_with_values_list():
            start_time = time.time()
            rows = list(Child.objects.all().values_list('pk', 'created_at'))
            self.assertEqual(len(rows), batch_size)
            return time.time() - start_time

        time_by_orm = by_orm()
        time_by_raw_query = by_raw_query()
        time_by_orm_with_values = by_orm_with_values()
        time_by_orm_with_values_list = by_orm_with_values_list()

        print('')
        print('by ORM: %.3f seconds.' % time_by_orm)  # by ORM: 26.702 seconds.
        print('by raw query: %.3f seconds.' % time_by_raw_query)  # by raw query: 5.662 seconds.
        print('by ORM with values(): %.3f seconds.' % time_by_orm_with_values)  # by ORM with values(): 12.013 seconds.
        print('by ORM with values_list(): %.3f seconds.' % time_by_orm_with_values_list) # by ORM with values_list(): 10.888 seconds.
        print('')

        self.assertTrue(time_by_orm > time_by_orm_with_values)
        self.assertTrue(time_by_orm_with_values > time_by_orm_with_values_list)
        self.assertTrue(time_by_orm_with_values_list > time_by_raw_query)

        # queryset = Parent.objects.all()\
        #     .prefetch_related(models.Prefetch(
        #         'child_set',
        #         queryset=Child.objects.all()
        #         .values('pk')
        #         .order_by('created_at')
        #     ))
        #
        # ValueError: Prefetch querysets cannot use values().
