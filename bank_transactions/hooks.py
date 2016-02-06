# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "bank_transactions"
app_title = "Bank Transactions"
app_publisher = "Wayzon"
app_description = "App for bank transactions"
app_icon = "icon-random"
app_color = "yellow"
app_email = "info@wayzon.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bank_transactions/css/bank_transactions.css"
# app_include_js = "/assets/bank_transactions/js/bank_transactions.js"

# include js, css files in header of web template
# web_include_css = "/assets/bank_transactions/css/bank_transactions.css"
# web_include_js = "/assets/bank_transactions/js/bank_transactions.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "bank_transactions.install.before_install"
# after_install = "bank_transactions.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bank_transactions.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"bank_transactions.tasks.all"
# 	],
# 	"daily": [
# 		"bank_transactions.tasks.daily"
# 	],
# 	"hourly": [
# 		"bank_transactions.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bank_transactions.tasks.weekly"
# 	]
# 	"monthly": [
# 		"bank_transactions.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "bank_transactions.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bank_transactions.event.get_events"
# }

