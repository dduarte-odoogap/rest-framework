# -*- coding: utf-8 -*-
# Copyright 2024 ERPGAP/PROMPTEQUATION LDA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import graphene
import logging
from odoo.addons.graphql_alokai_sale.graphql.sale_order import SaleOrderType
from .res_partner import PartnerType

_logger = logging.getLogger(__name__)


def resolve_partner_id(root, info):
    return root.partner_id


SaleOrderType._meta.fields["partner_id"] = graphene.Field(
    PartnerType,
    resolver=resolve_partner_id,
)
