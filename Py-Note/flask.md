flask-admin，自定义视图参数设置。

```python
# 许可类
    can_create = True
    """是否可以新建"""

    can_edit = True
    """是否可以编辑"""

    can_delete = True
    """是否可以编辑"""

    can_view_details = False
    """是否显示详情，如果你设置了不显示，可以设置是否使用详情显示未显示的内容。 """

    can_export = False
    """是否可以导出"""

    # jinjia2模板
    list_template = 'admin/model/list.html'
    """列表模板的路径"""

    edit_template = 'admin/model/edit.html'
    """编辑的模板路径"""

    create_template = 'admin/model/create.html'
    """新建的模板路径"""

    details_template = 'admin/model/details.html'
    """详情的模板路径"""

    # 动态模板
    edit_modal_template = 'admin/model/modals/edit.html'
    """动态编辑模板"""

    create_modal_template = 'admin/model/modals/create.html'
    """动态创建模板"""

    details_modal_template = 'admin/model/modals/details.html'
    """动态详情模板"""

    # 动态模式设置
    edit_modal = False
    """是否使用动态编辑"""

    create_modal = False
    """是否使用动态创建"""

    details_modal = False
    """是否使用动态详情"""

    # 自定义设置
    column_list = ObsoleteAttr('column_list', 'list_columns', None)
    """自定义在列表显示的字段"""
    """
        例:
            column_list = ('name', 'last_name', 'email')
            column_list = ('name', User.last_name)

        如果使用sqlalchemy定义了relationship，那么可以这样设置:
            column_list = ('<relationship>.<related column name>',)
    """

    column_exclude_list = ObsoleteAttr('column_exclude_list',
                                       'excluded_list_columns', None)
    """ 在列表排除的字段名，用法和上条一样 """

    column_details_list = None
    """ 详情视图显示的字段名集合，如果不设置，默认值是None，显示所有的字段名 """

    column_details_exclude_list = None
    """ 详情视图隐藏的字段名集合，如果不设置，显示所有的字段名 """

    column_export_list = None
    """ 设置导出的字段名列表，如果不设置，导出所有的字段名 """

    column_export_exclude_list = None
    """ 设置导出时排除的字段名，如果不设置，导出所有的字段名  """

    column_formatters = ObsoleteAttr('column_formatters', 'list_formatters', dict())
    """ 显示视图的格式化显示，没看懂啊"""
    """
        For example, if you want to show price multiplied by
        two, you can do something like this::

            class MyModelView(BaseModelView):
                column_formatters = dict(price=lambda v, c, m, p: m.price*2)

        or using Jinja2 `macro` in template::

            from flask_admin.model.template import macro

            class MyModelView(BaseModelView):
                column_formatters = dict(price=macro('render_price'))

            # in template
            {% macro render_price(model, column) %}
                {{ model.price * 2 }}
            {% endmacro %}

        The Callback function has the prototype::

            def formatter(view, context, model, name):
                # `view` is current administrative view
                # `context` is instance of jinja2.runtime.Context
                # `model` is model instance
                # `name` is property name
                pass
    """

    column_formatters_export = None
    """同样没看懂"""
    """
        Dictionary of list view column formatters to be used for export.

        Defaults to column_formatters when set to None.

        Functions the same way as column_formatters except
        that macros are not supported.
    """

    column_formatters_detail = None
    """同样没看懂"""
    """
        Dictionary of list view column formatters to be used for the detail view.

        Defaults to column_formatters when set to None.

        Functions the same way as column_formatters except
        that macros are not supported.
    """

    column_type_formatters = ObsoleteAttr('column_type_formatters', 'list_type_formatters', None)
    """要在列表视图中使用的值类型格式化程序字典。"""
    """
        Dictionary of value type formatters to be used in the list view.

        By default, three types are formatted:

        1. ``None`` will be displayed as an empty string
        2. ``bool`` will be displayed as a checkmark if it is ``True``
        3. ``list`` will be joined using ', '

        If you don't like the default behavior and don't want any type formatters
        applied, just override this property with an empty dictionary::

            class MyModelView(BaseModelView):
                column_type_formatters = dict()

        If you want to display `NULL` instead of an empty string, you can do
        something like this. Also comes with bonus `date` formatter::

            from datetime import date
            from flask_admin.model import typefmt

            def date_format(view, value):
                return value.strftime('%d.%m.%Y')

            MY_DEFAULT_FORMATTERS = dict(typefmt.BASE_FORMATTERS)
            MY_DEFAULT_FORMATTERS.update({
                    type(None): typefmt.null_formatter,
                    date: date_format
                })

            class MyModelView(BaseModelView):
                column_type_formatters = MY_DEFAULT_FORMATTERS

        Type formatters have lower priority than list column formatters.

        The callback function has following prototype::

            def type_formatter(view, value):
                # `view` is current administrative view
                # `value` value to format
                pass
    """

    column_type_formatters_export = None
    """要在导出中使用的值类型格式化程序的字典。 """
    """
        Dictionary of value type formatters to be used in the export.

        By default, two types are formatted:

        1. ``None`` will be displayed as an empty string
        2. ``list`` will be joined using ', '

        Functions the same way as column_type_formatters.
    """

    column_type_formatters_detail = None
    """要在详细信息视图中使用的值类型格式化程序字典。 """
    """
        Dictionary of value type formatters to be used in the detail view.

        By default, two types are formatted:

        1. ``None`` will be displayed as an empty string
        2. ``list`` will be joined using ', '

        Functions the same way as column_type_formatters.
    """

    column_labels = ObsoleteAttr('column_labels', 'rename_columns', None)
    """自定义列名的显示："""
    """
        例：
        class MyModelView(BaseModelView):
            column_labels = dict(name='Name', last_name='Last Name')
        例2:  可以把custom_field放在别的文件，统一更改
        custom_field={
            'name':'姓名',
            'last_name':'姓氏'
        }
        column_labels = custom_field
    """

    column_descriptions = None
    """字典，其中键是列名，值是“列表视图”列或添加/编辑表单字段的说明。 """
    """
         没明白

        For example::

            class MyModelView(BaseModelView):
                column_descriptions = dict(
                    full_name='First and Last name'
                )
    """

    column_sortable_list = ObsoleteAttr('column_sortable_list',
                                        'sortable_columns',
                                        None)
    """列表视图的可排序列的集合。如果设置为“None”，将从模型中获取它们。 """
    """
        例:
            class MyModelView(BaseModelView):
                column_sortable_list = ('name', 'last_name')

        如果要显式指定排序时要使用的字段/列，可以使用元组:
            class MyModelView(BaseModelView):
                column_sortable_list = ('name', ('user', 'user.username'))

        还可以指定排序时要使用的多个字段： :
            class MyModelView(BaseModelView):
                column_sortable_list = (
                    'name', ('user', ('user.first_name', 'user.last_name')))

        使用SQLAlchemy模型时，可以使用模型属性而不是字符串： :
            class MyModelView(BaseModelView):
                column_sortable_list = ('name', ('user', User.username))
    """

    column_default_sort = None
    """默认排序列。"""
    """
        Default sort column if no sorting is applied.

        Example::

            class MyModelView(BaseModelView):
                column_default_sort = 'user'

        You can use tuple to control ascending descending order. In following example, items
        will be sorted in descending order::

            class MyModelView(BaseModelView):
                column_default_sort = ('user', True)

        If you want to sort by more than one column,
        you can pass a list of tuples::

            class MyModelView(BaseModelView):
                column_default_sort = [('name', True), ('last_name', True)]
    """

    column_searchable_list = ObsoleteAttr('column_searchable_list',
                                          'searchable_columns',
                                          None)
    """可搜索列的集合"""
    """
        A collection of the searchable columns. It is assumed that only
        text-only fields are searchable, but it is up to the model
        implementation to decide.

        Example::

            class MyModelView(BaseModelView):
                column_searchable_list = ('name', 'email')
    """

    column_editable_list = None
    """ 可从列表视图编辑的列的集合。 """
    """
        Collection of the columns which can be edited from the list view.

        For example::

            class MyModelView(BaseModelView):
                column_editable_list = ('name', 'last_name')
    """

    column_choices = None
    """ 将选项映射到列表视图中的列 """
    """
        Map choices to columns in list view

        Example::

            class MyModelView(BaseModelView):
                column_choices = {
                    'my_column': [
                        ('db_value', 'display_value'),
                    ]
                }
    """

    column_filters =
    """列筛选器的集合"""
    """
        Collection of the column filters.

        Can contain either field names or instances of :class:`~flask_admin.model.filters.BaseFilter` classes.

        Example::

            class MyModelView(BaseModelView):
                column_filters = ('user', 'email')
    """

    named_filter_urls = False
    """ 设置为True可在URL参数中对筛选器使用人类可读的名称。 """
    """
        Set to True to use human-readable names for filters in URL parameters.

        False by default so as to be robust across translations.

        Changing this parameter will break any existing URLs that have filters.
    """

    column_display_pk = ObsoleteAttr('column_display_pk',
                                     'list_display_pk',
                                     False)
    """控制是否应在列表视图中显示主键"""
    """
        Controls if the primary key should be displayed in the list view.
    """

    column_display_actions = True
    """控制行操作（编辑、删除、详细信息等）的显示"""
    """
        Controls the display of the row actions (edit, delete, details, etc.)
        column in the list view.

        Useful for preventing a blank column from displaying if your view does
        not use any build-in or custom row actions.

        This column is not hidden automatically due to backwards compatibility.

        Note: This only affects display and does not control whether the row
        actions endpoints are accessible.
    """

    column_extra_row_actions = None
    """行操作列表"""
    """
        List of row actions (instances of :class:`~flask_admin.model.template.BaseListRowAction`).

        Flask-Admin will generate standard per-row actions (edit, delete, etc)
        and will append custom actions from this list right after them.

        For example::

            from flask_admin.model.template import EndpointLinkRowAction, LinkRowAction

            class MyModelView(BaseModelView):
                column_extra_row_actions = [
                    LinkRowAction('glyphicon glyphicon-off', 'http://direct.link/?id={row_id}'),
                    EndpointLinkRowAction('glyphicon glyphicon-test', 'my_view.index_view')
                ]
    """

    simple_list_pager = False
    """启用或禁用简单列表。"""

    """如果启用，模型接口将不运行计数查询，只显示上一页/下一页按钮。 """
    """
        Enable or disable simple list pager.
        If enabled, model interface would not run count query and will only show prev/next pager buttons.
    """

    form = None
    """表单类。如果要对模型使用自定义窗体，则重写。"""
    """
        Form class. Override if you want to use custom form for your model.
        Will completely disable form scaffolding functionality.
    
        For example::
    
            class MyForm(Form):
                name = StringField('Name')
    
            class MyModelView(BaseModelView):
                form = MyForm
    """

    form_base_class = BaseForm
    """基本窗体类。将在创建模型窗体时由窗体脚手架函数使用。 """
    """
        Base form class. Will be used by form scaffolding function when creating model form.
    
        Useful if you want to have custom constructor or override some fields.
    
        Example::
    
            class MyBaseForm(Form):
                def do_something(self):
                    pass
    
            class MyModelView(BaseModelView):
                form_base_class = MyBaseForm
    
    """

    form_args = None
    """表单域参数字典。请参阅WTForms文档以了解可能的选项列表。 """
    """
        Dictionary of form field arguments. Refer to WTForms documentation for
        list of possible options.
    
        Example::
    
            from wtforms.validators import DataRequired
            class MyModelView(BaseModelView):
                form_args = dict(
                    name=dict(label='First Name', validators=[DataRequired()])
                )
    """

    form_columns = None
    """窗体的模型字段名的集合"""
    """
        Collection of the model field names for the form. If set to `None` will
        get them from the model.
    
        Example::
    
            class MyModelView(BaseModelView):
                form_columns = ('name', 'email')
    
        (Added in 1.4.0) SQLAlchemy model attributes can be used instead of
        strings::
    
            class MyModelView(BaseModelView):
                form_columns = ('name', User.last_name)
    
        SQLA Note: Model attributes must be on the same model as your ModelView
        or you will need to use `inline_models`.
    """

    form_excluded_columns = ObsoleteAttr('form_excluded_columns',
                                         'excluded_form_columns',
                                         None)
    """排除的表单字段名的集合"""
    """
        Collection of excluded form field names.
    
        For example::
    
            class MyModelView(BaseModelView):
                form_excluded_columns = ('last_name', 'email')
    """

    form_overrides = None
    """表单列重写字典"""
    """
        Dictionary of form column overrides.
    
        Example::
    
            class MyModelView(BaseModelView):
                form_overrides = dict(name=wtf.FileField)
    """

    form_widget_args = None
    """表单部件参数"""
    """
        Dictionary of form widget rendering arguments.
        Use this to customize how widget is rendered without using custom template.
    
        Example::
    
            class MyModelView(BaseModelView):
                form_widget_args = {
                    'description': {
                        'rows': 10,
                        'style': 'color: black'
                    },
                    'other_field': {
                        'disabled': True
                    }
                }
    
        Changing the format of a DateTimeField will require changes to both form_widget_args and form_args.
    
        Example::
    
            form_args = dict(
                start=dict(format='%Y-%m-%d %I:%M %p') # changes how the input is parsed by strptime (12 hour time)
            )
            form_widget_args = dict(
                start={
                    'data-date-format': u'yyyy-mm-dd HH:ii P',
                    'data-show-meridian': 'True'
                } # changes how the DateTimeField displays the time
            )
    """

    form_extra_fields = None
    """附加字段字典"""
    """
        Dictionary of additional fields.
    
        Example::
    
            class MyModelView(BaseModelView):
                form_extra_fields = {
                    'password': PasswordField('Password')
                }
    
        You can control order of form fields using ``form_columns`` property. For example::
    
            class MyModelView(BaseModelView):
                form_columns = ('name', 'email', 'password', 'secret')
    
                form_extra_fields = {
                    'password': PasswordField('Password')
                }
    
        In this case, password field will be put between email and secret fields that are autogenerated.
    """

    form_ajax_refs = None
    """使用AJAX加载外键模型。"""
    """
        Use AJAX for foreign key model loading.
    
        Should contain dictionary, where key is field name and value is either a dictionary which
        configures AJAX lookups or backend-specific `AjaxModelLoader` class instance.
    
        For example, it can look like::
    
            class MyModelView(BaseModelView):
                form_ajax_refs = {
                    'user': {
                        'fields': ('first_name', 'last_name', 'email'),
                        'placeholder': 'Please select',
                        'page_size': 10,
                        'minimum_input_length': 0,
                    }
                }
    
        Or with SQLAlchemy backend like this::
    
            class MyModelView(BaseModelView):
                form_ajax_refs = {
                    'user': QueryAjaxModelLoader('user', db.session, User, fields=['email'], page_size=10)
                }
    
        If you need custom loading functionality, you can implement your custom loading behavior
        in your `AjaxModelLoader` class.
    """

    form_rules = None
    """ 模型创建窗体的呈现规则列表。 """
    """
        List of rendering rules for model creation form.
    
        This property changed default form rendering behavior and makes possible to rearrange order
        of rendered fields, add some text between fields, group them, etc. If not set, will use
        default Flask-Admin form rendering logic.
    
        Here's simple example which illustrates how to use::
    
            from flask_admin.form import rules
    
            class MyModelView(ModelView):
                form_rules = [
                    # Define field set with header text and four fields
                    rules.FieldSet(('first_name', 'last_name', 'email', 'phone'), 'User'),
                    # ... and it is just shortcut for:
                    rules.Header('User'),
                    rules.Field('first_name'),
                    rules.Field('last_name'),
                    # ...
                    # It is possible to create custom rule blocks:
                    MyBlock('Hello World'),
                    # It is possible to call macros from current context
                    rules.Macro('my_macro', foobar='baz')
                ]
    """

    form_edit_rules = None
    """编辑表单的自定义规则。如果存在，则重写“表单规则”。 """
    """
        Customized rules for the edit form. Override `form_rules` if present.
    """

    form_create_rules = None
    """"创建表单的自定义规则。如果存在，则重写“表单规则”。 """
    """
        Customized rules for the create form. Override `form_rules` if present.
    """

    # Actions
    action_disallowed_list = ObsoleteAttr('action_disallowed_list',
                                          'disallowed_actions',
                                          [])
    """ 一组不允许的操作名。 """
    """
        Set of disallowed action names. For example, if you want to disable
        mass model deletion, do something like this:
    
            class MyModelView(BaseModelView):
                action_disallowed_list = ['delete']
    """

    # Export settings
    export_max_rows = 0
    """允许导出的最大行数。 """
    """
        Maximum number of rows allowed for export.
    
        Unlimited by default. Uses `page_size` if set to `None`.
    """

    export_types = ['csv']
    """  可用导出文件类型的列表 """
    """
    data.export('csv')
    data.export('json')
    data.export('yaml')
    data.export('xls')
    data.export('df')
    data.export('xlsx')????
    """
    """
        A list of available export filetypes. `csv` only is default, but any
        filetypes supported by tablib can be used.
    
        Check tablib for https://github.com/kennethreitz/tablib/blob/master/README.rst
        for supported types.
    """

    # Pagination settings
    page_size = 20
    """默认分页大小"""
    """
        Default page size for pagination.
    """

    can_set_page_size = False
    """是否可以设置分页大小，可选20，50，100"""
    """
        Allows to select page size via dropdown list
    """
```