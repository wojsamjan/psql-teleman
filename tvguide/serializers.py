from rest_framework import serializers

from . import models


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'daily_channel': {'read_only': True}
        }
        fields = (
            'id',
            'tvguide',
            'name',
            'quote_page',
            'daily_channel',
        )
        model = models.Channel


class TvGuideSerializer(serializers.ModelSerializer):
    channels = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        fields = (
            'id',
            'name',
            'date_at',
            'created_at',
            'updated_at',
            'channels',
        )
        model = models.TvGuide
