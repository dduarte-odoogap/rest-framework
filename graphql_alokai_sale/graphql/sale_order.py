# -*- coding: utf-8 -*-
# Copyright 2024 ERPGAP/PROMPTEQUATION LDA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import graphene
from odoo import _
from odoo.addons.graphql_base import OdooObjectType
from odoo.addons.graphql_alokai.graphql.registry import query_collection, mutation_collection


class SaleOrderType(OdooObjectType):
    name = graphene.String(required=True)
    amount_total = graphene.Float(required=True)


class SaleQuery(graphene.ObjectType):
    all_sale_orders = graphene.List(SaleOrderType, required=True)

    @staticmethod
    def resolve_all_sale_orders(root, info):
        env = info.context["env"]
        return env["sale.order"].search([])


# 3) Optionally define partial mutation
class ConfirmSaleOrder(graphene.Mutation):
    class Arguments:
        sale_id = graphene.Int(required=True)

    Output = SaleOrderType

    @staticmethod
    def mutate(root, info, sale_id):
        env = info.context["env"]
        sale = env["sale.order"].browse(sale_id)
        if not sale:
            return None
        sale.action_confirm()
        return sale


class SaleMutation(graphene.ObjectType):
    confirm_sale_order = ConfirmSaleOrder.Field()


# 4) Register these partial classes
query_collection.append(SaleQuery)
mutation_collection.append(SaleMutation)
