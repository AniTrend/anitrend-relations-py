from serde import Model, fields


class XemContainerEntity(Model):
    result = fields.Str()
    data = fields.Dict()
    message = fields.Str()


class RelationSeasonEntity(Model):
    season = fields.Str()
    year = fields.Optional(fields.Int())


class RelationDataEntity(Model):
    sources = fields.Optional(fields.List(fields.Str()))
    title = fields.Str()
    type = fields.Str()
    episodes = fields.Optional(fields.Int())
    status = fields.Str()
    animeSeason = fields.Optional(fields.Nested(RelationSeasonEntity))
    picture = fields.Optional(fields.Str())
    thumbnail = fields.Optional(fields.Str())
    synonyms = fields.Optional(fields.List(fields.Str()))
    relations = fields.Optional(fields.List(fields.Str()))
    tags = fields.Optional(fields.List(fields.Str()))


class RelationContainerEntity(Model):
    data = fields.List(fields.Nested(RelationDataEntity))
