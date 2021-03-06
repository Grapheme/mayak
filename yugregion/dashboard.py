# -*- coding: utf-8 -*-

"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'yugregion.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'yugregion.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for yugregion.
    """

    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            _('Quick links'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_(u'Маяк'), reverse('mayak_index')],
                [_(u'Шансон'), reverse('shanson_index')],
                [_('Change password'),
                 reverse('%s:password_change' % site_name)],
                [_('Log out'), reverse('%s:logout' % site_name)],
            ]
        ))

        # Администрирование
        self.children.append(modules.Group(
            title=u"Администрирование",
            display="tabs",
            children=[
                modules.ModelList(
                    title=u'Администрирование',
                    models=(
                        'planb.feedback.models.*',
                        'planb.gallery.models.*',
                        'planb.structure.models.*',
                    ),
                ),
                modules.ModelList(
                    title=u'Настройки',
                    models=(
                        'constance.*',
                    ),
                ),
            ]
        ))

        # append a recent actions module
        self.children.append(
            modules.RecentActions(_('Recent Actions'), 5)
        )

        # Сайты
        self.children.append(modules.Group(
            title=u"Сайты",
            display="tabs",
            children=[
                modules.ModelList(
                    title = u'Маяк',
                    models=(
                        'yugregion.mayak_nucleum.models.*',
                        'yugregion.mayak_consultation.models.*',
                        'yugregion.mayak_news.models.*',
                        'yugregion.mayak_advertisers.models.*',
                        'yugregion.mayak_video.models.*',
                    ),
                ),
                modules.ModelList(
                    title = u'Шансон',
                    models=(
                        'yugregion.shanson_nucleum.models.*',
                        'yugregion.shanson_advertisers.models.*',
                        'yugregion.shanson_news.models.*',
                    ),
                ),
            ]
        ))


        # # append an app list module for "Applications"
        # self.children.append(modules.AppList(
        #     _('Applications'),
        #     exclude=('django.contrib.*',),
        # ))

        # # append an app list module for "Administration"
        # self.children.append(modules.AppList(
        #     _('Administration'),
        #     models=('django.contrib.*',),
        # ))

        # # append a feed module
        # self.children.append(modules.Feed(
        #     _('Latest Django News'),
        #     feed_url='http://www.djangoproject.com/rss/weblog/',
        #     limit=5
        # ))

        # # append another link list module for "support".
        # self.children.append(modules.LinkList(
        #     _('Support'),
        #     children=[
        #         {
        #             'title': _('Django documentation'),
        #             'url': 'http://docs.djangoproject.com/',
        #             'external': True,
        #         },
        #         {
        #             'title': _('Django "django-users" mailing list'),
        #             'url': 'http://groups.google.com/group/django-users',
        #             'external': True,
        #         },
        #         {
        #             'title': _('Django irc channel'),
        #             'url': 'irc://irc.freenode.net/django',
        #             'external': True,
        #         },
        #     ]
        # ))


class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for yugregion.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomAppIndexDashboard, self).init_with_context(context)
