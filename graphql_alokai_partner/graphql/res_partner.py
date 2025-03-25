# -*- coding: utf-8 -*-
# Copyright 2024 ERPGAP/PROMPTEQUATION LDA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import graphene
from odoo import _
from odoo.addons.graphql_base import OdooObjectType
from odoo.addons.graphql_alokai.graphql.registry import query_collection


class PartnerType(OdooObjectType):
    name = graphene.String(required=True)
    street = graphene.String(required=True)


class PartnerQuery(graphene.ObjectType):
    all_partners = graphene.List(PartnerType, required=True)

    @staticmethod
    def resolve_all_sale_orders(root, info):
        env = info.context["env"]
        return env["sale.order"].search([])


query_collection.append(PartnerQuery)
