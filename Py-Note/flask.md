flask-admin，自定义视图参数设置。

```python
# modelview可修改的属性
can_create  # 是否可以新建，value: True/False
can_edit  # 是否可以编辑, value: True/False
can_delete  # 是否可以删除, value: True/False
can_view_details  # 是否显示详情, value: True/False
can_export  # 是否可以导出, value: True/False
# jinjia2模板
list_template  # 列表模板的路径, value: 'admin/model/list.html'
edit_template  # 编辑的模板路径, value: 'admin/model/edit.html'
create_template  # 新建的模板路径, value: 'admin/model/create.html'
details_template  # 详情的模板路径, value: 'admin/model/details.html'
# 动态模板
edit_modal_template  # 动态编辑模板, value: 'admin/model/modals/edit.html'
create_modal_template  # 动态创建模板, value: 'admin/model/modals/create.html'
details_modal_template  # 动态详情模板, value: 'admin/model/modals/details.html'
# 动态模式设置
edit_modal  # 是否使用动态编辑, value: True/False
create_modal  # 是否使用动态创建, value: True/False
details_modal  # 是否使用动态详情, value: True/False
# 自定义设置
column_list = ObsoleteAttr('column_list', 'list_columns', None)
'''
自定义在列表显示的字段
例:
    column_list = ('name', 'last_name', 'email')
    column_list = ('name', User.last_name)
'''
column_exclude_list = ObsoleteAttr('column_exclude_list',
                                   'excluded_list_columns', None)
# 在列表排除的字段名，用法和上条一样
column_details_list = None
# 详情视图显示的字段名集合，如果不设置，默认值是None，显示所有的字段名
column_details_exclude_list = None
# 详情视图隐藏的字段名集合，如果不设置，显示所有的字段名
column_export_list = None
# 设置导出的字段名列表，如果不设置，导出所有的字段名
column_export_exclude_list = None
# 设置导出时排除的字段名，如果不设置，导出所有的字段名
column_formatters = ObsoleteAttr('column_formatters', 'list_formatters', dict())
# 一个字典，格式化字段，定义字段的显示方式
column_formatters_export = None
# 定义导出的字段格式
column_formatters_detail = None
# 详情视图的列表格式化程序的字典
column_type_formatters = ObsoleteAttr('column_type_formatters', 'list_type_formatters', None)
# 要在列表视图中使用的值类型格式化程序字典
column_type_formatters_export = None
# 要在导出中使用的值类型格式化程序的字典
column_type_formatters_detail = None
# 要在详细信息视图中使用的值类型格式化程序字典
column_labels = ObsoleteAttr('column_labels', 'rename_columns', None)
# 自定义列名的显示
column_descriptions = None
# 字典，其中键是列名，值是“列表视图”列或添加/编辑表单字段的说明
column_sortable_list = ObsoleteAttr('column_sortable_list',
                                    'sortable_columns',
                                    None)
# 列表视图的可排序列的集合。如果设置为“None”，将从模型中获取它们
column_default_sort = None
# 默认排序列
column_searchable_list = ObsoleteAttr('column_searchable_list',
                                      'searchable_columns',
                                      None)
# 可搜索列的集合
column_editable_list = None
#  可从列表视图编辑的列的集合
column_choices = None
# 将选项映射到列表视图中的列
column_filters = None
# 列筛选器的集合
named_filter_urls = False
# 设置为True可在URL参数中对筛选器使用人类可读的名称
column_display_pk = ObsoleteAttr('column_display_pk',
                                 'list_display_pk',
                                 False)
# 控制是否应在列表视图中显示主键
column_display_actions = True
# 控制行操作（编辑、删除、详细信息等）的显示
column_extra_row_actions = None
# 行操作列表
simple_list_pager = False
# 启用或禁用简单列表。如果启用，模型接口将不运行计数查询，只显示上一页/下一页按钮
form = None
# 表单类。如果要对模型使用自定义窗体，则重写
form_base_class = BaseForm
# 基本窗体类。将在创建模型窗体时由窗体脚手架函数使用
form_args = None
# 表单域参数字典。请参阅WTForms文档以了解可能的选项列表
form_columns = None
# 窗体的模型字段名的集合
form_excluded_columns = ObsoleteAttr('form_excluded_columns',
                                     'excluded_form_columns',
                                     None)
# 排除的表单字段名的集合
form_overrides = None
# 表单列重写字典
form_widget_args = None
# 表单部件参数
form_extra_fields = None
# 附加字段字典
form_ajax_refs = None
# 使用AJAX加载外键模型
form_rules = None
# 模型创建窗体的呈现规则列表
form_edit_rules = None
# 编辑表单的自定义规则。如果存在，则重写“表单规则”
form_create_rules = None
# 创建表单的自定义规则。如果存在，则重写“表单规则”

# Actions
action_disallowed_list = ObsoleteAttr('action_disallowed_list',
                                      'disallowed_actions',
                                      [])
#  一组不允许的操作名
# Export settings
export_max_rows = 0
# 允许导出的最大行数
export_types = ['csv']
# 可用导出文件类型的列表
"""
data.export('csv')
data.export('json')
data.export('yaml')
data.export('xls')
data.export('df')
data.export('xlsx')????
"""
# Pagination settings
page_size = 20
# 默认分页大小
can_set_page_size = False
# 是否可以设置分页大小，可选20，50，100
# method
@expose('/')
def index_view(self):
# 列表视图方法
@expose('/new/', methods=('GET', 'POST'))
def create_view(self):
# 新建视图方法
@expose('/edit/', methods=('GET', 'POST'))
def edit_view(self):
# 修改试图方法
@expose('/details/')
def details_view(self):
# 查看详情视图方法
@expose('/delete/', methods=('POST',))
def delete_view(self):
# 删除视图方法
@expose('/action/', methods=('POST',))
def action_view(self):
# 自定义显示操作
@expose('/export/<export_type>/')
def export(self, export_type):
# 导出视图方法
```