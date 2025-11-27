from rest_framework import serializers

# User Serializer
class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    team = serializers.CharField(max_length=100)

# Team Serializer
class TeamSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.CharField())

# Activity Serializer
class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = serializers.CharField(max_length=100)
    type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    date = serializers.DateField()

# Leaderboard Serializer
class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    team = serializers.CharField(max_length=100)
    points = serializers.IntegerField()

# Workout Serializer
class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    difficulty = serializers.CharField(max_length=50)
