# -*- encoding: utf-8 -*-
from search.models import Site
from haystack import indexes
class SiteIndex(indexes.SearchIndex, indexes.Indexable):
    # 文章内容
    text = indexes.CharField(document=True, use_template=True)
    # 对title字段进行索引
    title = indexes.CharField(model_attr='title')
    def get_model(self):
        return Site
    def index_queryset(self, using=None):
        return self.get_model().objects.all()