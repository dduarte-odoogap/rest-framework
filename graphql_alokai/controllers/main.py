# -*- coding: utf-8 -*-
# Copyright 2024 ERPGAP/PROMPTEQUATION LDA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import http

from odoo.addons.graphql_base import GraphQLControllerMixin

from ..graphql.schema import build_alokai_schema

class GraphQLController(http.Controller, GraphQLControllerMixin):
    _graphql_schema = False

    def __init__(self):
        super(GraphQLController, self).__init__()
        self._graphql_schema = build_alokai_schema().graphql_schema

    @http.route("/graphiql/alokai", auth="user")
    def graphiql(self, **kwargs):
        return self._handle_graphiql_request(self._graphql_schema)

    @http.route("/graphql/alokai", auth="user", csrf=False)
    def graphql(self, **kwargs):
        return self._handle_graphql_request(self._graphql_schema)
