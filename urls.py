#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

==================================================== CLIPPBOT SITEMAP ===================================================

-------------------------------------------------------------------------------------------------------------------------
|URI																|HANDLER				|METHOD			|PRONTO?	|
|																	|						-----------------			|
|																	|						|GET	|POST	|			|
|------------------------------------------------------------------------------------------------------------------------
|/																	|views.index			|YES	|NO		|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|..../teams 														|views.item 			|YES	|YES	|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|..../<item_key> 													|views.teams 			|YES	|YES	|0%			|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|..../team/<team_key>												|views.team_home 		|YES	|NO		|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|......../team/<team_key>/join										|views.team_join 		|YES	|YES	|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|......../team/<team_key>/edit										|views.team_edit 		|YES	|YES	|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|......../team/<team_key>/exit										|views.team_exit 		|YES	|YES	|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|......../team/<team_key>/members									|views.team_members 	|YES	|NO		|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|......../team/<team_key>/channels									|views.team_channels 	|YES	|YES	|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|............/team/<team_key>/channels/<channel_key>				|views.channel 			|YES	|YES	|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|......../team/<team_key>/categories								|views.team_categories 	|YES	|YES	|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|............/team/<team_key>/categories/<category_key>				|views.category 		|YES	|YES	|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|............/team/<team_key>/categories/<category_key>/items		|views.category_items	|YES	|YES	|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|..../profile														|views.my_profile 		|YES	|YES	|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|......../profile/<profile_key>										|views.profile 			|YES	|NO		|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|..../help															|views.help 			|YES	|NO		|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|......../help/<topic>												|views.help				|YES	|NO		|100%		|
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|..../search 														|views.search 			|YES	|NO		|0%			| DESATIVADO POR ENQUANTO
|-------------------------------------------------------------------|-----------------------|-------|-------|-----------|
|..../issue															|views.issue 			|YES	|NO		|100%		|
-------------------------------------------------------------------------------------------------------------------------
"""

from django.conf.urls.defaults import *

urlpatterns = patterns(
	'',
	(r'^$','views.index'),
	(r'^teams$','views.teams'),
	(r'^search$','views.search'),
	(r'^search/(?P<query>[\S]+)$','views.search'),
	(r'^team/(?P<team_key>[a-zA-Z0-9_.-]+)$','views.team_home'),
	(r'^team/(?P<team_key>[a-zA-Z0-9_.-]+)/join$','views.team_join'),
	(r'^team/(?P<team_key>[a-zA-Z0-9_.-]+)/edit$','views.team_edit'),
	(r'^team/(?P<team_key>[a-zA-Z0-9_.-]+)/exit$','views.team_exit'),
	(r'^team/(?P<team_key>[a-zA-Z0-9_.-]+)/members$','views.team_members'),
	(r'^team/(?P<team_key>[a-zA-Z0-9_.-]+)/channels$','views.team_channels'),
	(r'^team/(?P<team_key>[a-zA-Z0-9_.-]+)/channels/(?P<channel_key>[a-zA-Z0-9_.-]+)$$','views.channel'),
	(r'^team/(?P<team_key>[a-zA-Z0-9_.-]+)/categories$','views.team_categories'),
	(r'^team/(?P<team_key>[a-zA-Z0-9_.-]+)/categories/(?P<category_key>[a-zA-Z0-9_.-]+)$','views.category'),
	(r'^team/(?P<team_key>[a-zA-Z0-9_.-]+)/categories/(?P<category_key>[a-zA-Z0-9_.-]+)/contacts$','views.contacts'),
	(r'^team/(?P<team_key>[a-zA-Z0-9_.-]+)/categories/(?P<category_key>[a-zA-Z0-9_.-]+)/items$','views.category_items'),
	(r'^profile$','views.profile'),
	(r'^profile/(?P<profile_key>[a-zA-Z0-9_.-]+)$','views.profile'),
	(r'^help$','views.help'),
	(r'^help/(?P<topic>[a-zA-Z0-9_.-]+)$','views.help'),
	(r'^issue$','views.issue'),
	(r'^(?P<item_key>[\S]+)/edit$','views.item_edit'),
	(r'^(?P<item_key>[\S]+)$','views.item'),
)