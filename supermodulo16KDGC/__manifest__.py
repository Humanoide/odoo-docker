# -*- coding: utf-8 -*-
{
    'name': "supermodulo16KDGC",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends':[
'account_edi_ubl_cii',
'account_edi',
'account_payment_invoice_online_payment_patch',
'account_payment',
'account_qr_code_sepa',
'account_sequence',
'account',
'analytic',
'auth_signup',
'auth_totp_mail',
'auth_totp_portal',
'auth_totp',
'auto_backup',
'base_address_extended',
'base_iban',
'base_import',
'base_install_request',
'base_location_geonames_import',
'base_location',
'base_setup',
'base_technical_features',
'base_vat',
'base',
'bus',
'calendar_sms',
'calendar',
'contacts',
'crm_sms',
'crm',
'digest',
'gamification_sale_crm',
'gamification',
'google_gmail',
'http_routing',
'iap_crm',
'iap_mail',
'iap',
'l10n_es_toponyms',
'l10n_es',
'link_tracker',
'login_user_detail',
'mail_bot',
'mail',
'mass_mailing_crm',
'mass_mailing_sale',
'mass_mailing_themes',
'mass_mailing',
'note',
'partner_autocomplete',
'payment',
'phone_validation',
'portal',
'privacy_lookup',
'product',
'resource',
'sale_crm',
'sale_management',
'sale_product_configurator',
'sale_product_template_tags',
'sale_sms',
'sale',
'sales_team',
'show_db_name',
'sms',
'snailmail_account',
'snailmail',
'social_media',
'spreadsheet_account',
'spreadsheet_dashboard_account',
'spreadsheet_dashboard_sale',
'spreadsheet_dashboard',
'spreadsheet',
'survey',
'uom',
'utm',
'web_editor',
'web_kanban_gauge',
'web_no_bubble',
'web_responsive',
'web_tour',
'web_unsplash',
'web',    
    ],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
