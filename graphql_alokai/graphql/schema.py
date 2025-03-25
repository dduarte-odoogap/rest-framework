# -*- coding: utf-8 -*-
# Copyright 2024 ERPGAP/PROMPTEQUATION LDA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import graphene
from .registry import query_collection, mutation_collection

class BaseQuery(graphene.ObjectType):
    """Empty base query; extension modules can add fields."""

class BaseMutation(graphene.ObjectType):
    """Empty base mutation; extension modules can add mutations."""

def build_alokai_schema():
    """
    Dynamically build the final GraphQL schema by inheriting
    from all partial query and mutation classes in the registry.
    """

    Query = type(
        "Query",
        tuple(query_collection + [BaseQuery]),
        {}
    )

    Mutation = type(
        "Mutation",
        tuple(mutation_collection + [BaseMutation]),
        {}
    )

    return graphene.Schema(query=Query, mutation=Mutation)

